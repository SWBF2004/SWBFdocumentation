from pathlib import Path
from util.token import Token


class Node:
    def __init__(self, parent = None, **kwargs):
        super().__init__(**kwargs)

        self.parent: Node = parent
        self.children: list[Node] = []

    def type(self) -> str:
        return self.__class__.__name__
    
    def add(self, other) -> None:
        other.parent = self
        self.children.append(other)

    def print(self, level: int = 0) -> None:
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

        self.path : Path = path


class Document(Node):
    def __init__(self, filepath: Path, parent: Node = None, **kwargs):
        super().__init__(parent, **kwargs)

        self.filepath : Path = filepath


class LexicalNode(Node):
    def __init__(self, tokens: list[Token], parent: Node = None):
        super().__init__(parent)

        self.tokens: list[Token] = tokens
    
    def raw(self) -> str:
        return ''.join(list(map(lambda x : x.text, self.tokens)))

    def print(self, level: int = 0) -> None:
        print(f'{" " * level}{self.__class__.__name__:20s}{bytearray(self.raw(), encoding="utf-8")}')
        for c in self.children:
            c.print(level + 1)
