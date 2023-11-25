# HTML-Checker-Using-PDA

HTML Checker Using Pushdown Automata (PDA)

Notes:

1. Here is one of the example of the tokenization process for our HTML tags:

   from:

```
<h1 class="footer for main" > Main Content </h1>
```

to:

```
['<h1', 'class=""', '>', '</h1>']
```

2. If within the PDA, there exist the a transition function which is in the same state, has the same input symbol, and has different pop stack requirement, put the transition function with epsilon (no requirement) as the requirement at the bottom most of the .txt file, so that it will check all other possible requirement first. Example:

```
B1 <input epsilon B4 epsilon            // This is wrong
B1 <input input B4 epsilon              // This is wrong

B1 <input input B4 epsilon              // This is correct
B1 <input epsilon B4 epsilon            // This is correct
```
