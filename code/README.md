# Markdown Parser/Generator

## Parser

---
test
---

---
@test
---

---
# test
---

Represents a subset of the Markdown syntax as an abstract syntax tree (AST).

Example:
```python
from pathlib import Path
from md.nodes import Document
from md.lexer import Lexer
from md.parser import Parser

file = Path('<the markdown file>.md')
tokens = Lexer(file).tokenize()
document : Document = Parser(file, tokens).parse()
document.print()  # Prints nodes of the AST with their respective tokens.
```

A node can be of the following types (which also represents the supported Markdown syntax):
`Node`, `Document`, `Text`, `Image`, `Reference`, `Code`, `Heading`, `List`, `Table`, `TableRow`, `TableCell`

## Generator

Generates a HTML representation from a collection of nodes.
Ideally, the collection of nodes is a folder of Markdown files.

Example:
```python
from md.nodes import Folder
from export.html import export_html

root: Folder = ...  # Result of the parser
clear: bool = True  # Overwrite existing results
export_html("assets/", "templates/", "destination/", clear, root=root)
```

The `"templates/"` folder needs to contain a `index.html.j2` and a `page.html.j2` jinja template file.
Markdown files will be rendered to the `page.html` file.
The `index.html` file can be used as entry point.

The `"assets/"` folder can be used for additional resources like fonts, images, style sheets, or scripts that will be shipped with the exported files.

`"destination/"` determines the output folder of all exported files.

### HTML Export

The HTML generator can be given additional arguments to launch an HTTP webserver to host the HTML files and a Websocket server to enable the search functionality.

Example (launched from the code/ folder):
```
python ./source/main.py -f ../docs/ HTML -c -d build -t ./resource/html/templates/ -a ./resource/html/assets/ -p 9000
```

This will open the default browser at localhost:9000/index.html which will look something like that:
![Page](https://github.com/SWBF2004/SWBFdocumentation/blob/master/code/resource/images/doc.png)

## Tests

```
python -m unittest discover -s test -t .
```
