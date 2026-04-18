import os
from pathlib import Path

from flask import Flask, jsonify, render_template, request

import htmlParser
import pda

ROOT = Path(__file__).resolve().parent.parent
TEST_DIR = ROOT / "test"
PDA_DIR = ROOT / "pda"

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/samples")
def list_samples():
    files = sorted(p.name for p in TEST_DIR.glob("*.html"))
    return jsonify(files)


@app.route("/api/pdas")
def list_pdas():
    files = sorted(p.name for p in PDA_DIR.glob("*.txt"))
    return jsonify(files)


@app.route("/api/sample/<name>")
def get_sample(name):
    path = (TEST_DIR / name).resolve()
    if not path.is_file() or TEST_DIR not in path.parents:
        return jsonify({"error": "not found"}), 404
    return jsonify({"name": name, "content": path.read_text()})


def _load_pda(pda_name):
    path = (PDA_DIR / pda_name).resolve()
    if not path.is_file() or PDA_DIR not in path.parents:
        raise FileNotFoundError(pda_name)
    with open(path) as f:
        lines = [line.split() for line in f.readlines()]
    return (
        lines[0],
        lines[1],
        lines[2],
        lines[3][0],
        lines[4],
        lines[5],
        lines[6][0],
        lines[7:],
    )


@app.route("/api/check", methods=["POST"])
def check():
    data = request.get_json(force=True)
    html_content = data.get("html", "")
    pda_name = data.get("pda", "pda.txt")

    try:
        pda_args = _load_pda(pda_name)
    except FileNotFoundError:
        return jsonify({"error": f"PDA file '{pda_name}' not found"}), 400

    tokens = htmlParser.parseHTMLContent(html_content)
    checker = pda.HTMLCheckerPDA()
    checker.setPDA(*pda_args)
    result = checker.check_correctness(tokens)

    return jsonify({
        "valid": result == -1,
        "error_line": None if result == -1 else result,
        "tokens": [{"line": line, "token": tok} for line, tok in tokens],
        "final_state": checker.current_state,
        "stack": checker.stack,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5050)
