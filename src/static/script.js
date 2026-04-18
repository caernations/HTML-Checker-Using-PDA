const editor = document.getElementById("editor");
const gutter = document.getElementById("gutter");
const samplePicker = document.getElementById("samplePicker");
const pdaPicker = document.getElementById("pdaPicker");
const checkBtn = document.getElementById("checkBtn");
const clearBtn = document.getElementById("clearBtn");
const status = document.getElementById("status");
const summary = document.getElementById("summary");
const verdict = document.getElementById("verdict");
const finalState = document.getElementById("finalState");
const stackOut = document.getElementById("stackOut");
const tokensEl = document.getElementById("tokens");
const tokenCount = document.getElementById("tokenCount");

function setStatus(cls, label) {
  status.className = `status ${cls}`;
  status.querySelector(".label").textContent = label;
}

function updateGutter() {
  const lines = editor.value.split("\n").length || 1;
  gutter.textContent = Array.from({ length: lines }, (_, i) => i + 1).join("\n");
}

editor.addEventListener("input", updateGutter);
editor.addEventListener("scroll", () => {
  gutter.scrollTop = editor.scrollTop;
});

async function loadSamples() {
  const res = await fetch("/api/samples");
  const files = await res.json();
  files.forEach((f) => {
    const opt = document.createElement("option");
    opt.value = f;
    opt.textContent = f;
    samplePicker.appendChild(opt);
  });
}

async function loadPdas() {
  const res = await fetch("/api/pdas");
  const files = await res.json();
  files.forEach((f) => {
    const opt = document.createElement("option");
    opt.value = f;
    opt.textContent = f;
    pdaPicker.appendChild(opt);
  });
}

samplePicker.addEventListener("change", async (e) => {
  const name = e.target.value;
  if (!name) { editor.value = ""; updateGutter(); return; }
  const res = await fetch(`/api/sample/${encodeURIComponent(name)}`);
  const data = await res.json();
  editor.value = data.content || "";
  updateGutter();
});

clearBtn.addEventListener("click", () => {
  editor.value = "";
  samplePicker.value = "";
  updateGutter();
  resetResult();
});

function resetResult() {
  summary.className = "summary pending";
  summary.textContent = "awaiting input";
  verdict.className = "verdict";
  verdict.innerHTML = '<div class="verdict-icon">◎</div><div class="verdict-text">Run the checker to see results.</div>';
  finalState.textContent = "—";
  stackOut.textContent = "—";
  tokensEl.innerHTML = '<em class="muted">no tokens yet</em>';
  tokenCount.textContent = "";
  setStatus("", "idle");
}

function classifyToken(tok) {
  if (tok.includes("INVALID")) return "error";
  if (tok.startsWith("</")) return "close";
  if (tok.startsWith("<") && tok !== "<!---->") return "open";
  return "";
}

function renderTokens(tokens, errorLine) {
  if (!tokens.length) {
    tokensEl.innerHTML = '<em class="muted">no tokens produced</em>';
    tokenCount.textContent = "";
    return;
  }
  tokenCount.textContent = `(${tokens.length})`;
  tokensEl.innerHTML = "";
  tokens.forEach(({ line, token }) => {
    const el = document.createElement("span");
    const cls = classifyToken(token);
    el.className = `token ${cls}`;
    if (errorLine && line === errorLine) el.classList.add("error");
    el.innerHTML = `<span class="line">L${line}</span>${escapeHtml(token)}`;
    tokensEl.appendChild(el);
  });
}

function escapeHtml(s) {
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

checkBtn.addEventListener("click", async () => {
  const html = editor.value;
  const pdaName = pdaPicker.value || "pda.txt";
  if (!html.trim()) {
    setStatus("bad", "no input");
    summary.className = "summary bad";
    summary.textContent = "empty input";
    return;
  }

  setStatus("run", "checking…");
  summary.className = "summary pending";
  summary.textContent = "running PDA…";

  try {
    const res = await fetch("/api/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ html, pda: pdaName }),
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error);

    renderTokens(data.tokens, data.error_line);
    finalState.textContent = data.final_state || "—";
    stackOut.textContent = data.stack && data.stack.length ? data.stack.join(" · ") : "∅ (empty)";

    if (data.valid) {
      setStatus("ok", "valid");
      summary.className = "summary ok";
      summary.textContent = "VALID";
      verdict.className = "verdict ok";
      verdict.innerHTML = '<div class="verdict-icon">✓</div><div class="verdict-text">HTML is accepted by the PDA.</div>';
    } else {
      setStatus("bad", "invalid");
      summary.className = "summary bad";
      summary.textContent = "INVALID";
      verdict.className = "verdict bad";
      verdict.innerHTML = `<div class="verdict-icon">✕</div><div class="verdict-text">HTML is invalid — error at line <b>${data.error_line}</b>.</div>`;
    }
  } catch (err) {
    setStatus("bad", "error");
    summary.className = "summary bad";
    summary.textContent = "error";
    verdict.className = "verdict bad";
    verdict.innerHTML = `<div class="verdict-icon">!</div><div class="verdict-text">${escapeHtml(err.message)}</div>`;
  }
});

(async function init() {
  updateGutter();
  await Promise.all([loadSamples(), loadPdas()]);
})();
