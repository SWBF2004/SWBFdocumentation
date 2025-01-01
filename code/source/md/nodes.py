import re
from pathlib import Path


class Node:
    def __init__(self, parent = None):
        self.parent: Node = parent
        self.children: list = []

    def type(self):
        return self.__class__.__name__
    
    def add(self, other):
        other.parent = self
        self.children.append(other)

    def print(self, level: int = 0):
        print(f'{" " * level}{self.__class__.__name__:20s}')
        for c in self.children:
            c.print(level + 1)
    
    def walk(self):
        yield self

        for child in self.children:
            yield from child.walk()


class Folder(Node):
    def __init__(self, path: Path, parent: Node = None):
        super().__init__(parent)

        self.path = path


class Document(Node):
    def __init__(self, path: Path, parent: Node = None):
        super().__init__(parent)

        self.path = path


class LexicalNode(Node):
    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(parent)

        self.tokens: list = tokens
    
    def raw(self) -> str:
        return ''.join(list(map(lambda x : x.text, self.tokens)))

    def print(self, level: int = 0):
        print(f'{" " * level}{self.__class__.__name__:20s}{bytearray(self.raw(), encoding="utf-8")}')
        for c in self.children:
            c.print(level + 1)


class Text(LexicalNode):
    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        self.text = self.raw().strip()


class Heading(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)

        self.level = 1


class Image(LexicalNode):
    RE = re.compile('\!\[(.*)\]\((.*)\)')

    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        match = re.search(Image.RE, self.raw())

        self.text = match.group(1)
        self.target = match.group(2)


class Reference(LexicalNode):
    RE = re.compile('\[(.*)\]\((.*)\)')

    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        match = re.search(Reference.RE, self.raw())

        self.text = match.group(1)
        self.target = match.group(2)


class Code(LexicalNode):
    RE = re.compile('`([^`]*)`')

    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        match = re.search(Code.RE, self.raw())

        self.text = match.group(1)


class List(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)


class ListItem(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)


class Table(Node):
    class Align:
        left = 'left'
        center = 'center'
        right = 'right'

    def __init__(self, parent: Node = None):
        super().__init__(parent)

        self.columns = 0
        self.cell_alignment = []


class TableRow(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)


class TableCell(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)
