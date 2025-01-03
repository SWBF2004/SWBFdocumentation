"""
class Temp:
    Null = 0

    Whitespace = 0x10
    Whitespaces = \
        [LineFeed, CarriageReturn, Space, HorizontalTabulator, VerticalTabulator] = \
        ['\n', '\r', ' ', '\t', '\v']

    Separator = 0x20
    Separators = [
        ExclamationMark, QutationMark, NumberSign, DollarSign, PercentSign, Ampersand, Apostrophe,
        ParanthesisOpen, ParanthesisClose, Asterisk, PlusSign, Comma, MinusSign, Period,
        Slash, Colon, Semicolon, LessThanSign, EqualSign, GreaterThanSign, QuestionMark,
        AtSign, Backtick, VerticalBar, SquareBracketOpen, SquareBracketClose
    ] = [
        '!', '"', '#', '$', '%', '&', '\'',
        '(', ')', '*', '+', ',', '-', '.',
        '/', ':', ';', '<', '=', '>', '?',
        '@', '`', '|', '[', ']'
    ]
"""

class TK:
    def __class_getitem__(klass, sym: str) -> int:
        for k, v in TK.__dict__.items():
            if v == sym:
                return TK.__dict__[k]
        return TK.Null

    Null = 0

    Whitespaces = \
        [LineFeed, CarriageReturn, Space, HorizontalTabulator, VerticalTabulator] = \
        ['\n', '\r', ' ', '\t', '\v']

    Separators = [
        ExclamationMark, NumberSign, ParanthesisOpen, ParanthesisClose,
        Asterisk, Period, Minus,
        Slash, Backtick, VerticalBar, SquareBracketOpen, SquareBracketClose
    ] = [
        '!', '#', '(', ')',
        '*', '.', '-',
        '/', '`', '|', '[', ']'
    ]

    Symbol = 0x30
    Number = 0x31
    Word = 0x32
    TargetName = [Number, Word, Period, Slash, Minus]
    Text = [Space, HorizontalTabulator, Symbol, Number, Word, ParanthesisOpen, ParanthesisClose, Period, Slash, Minus]
    ReferenceText = [Number, Word] + Whitespaces


class Token:
    def __init__(self, beg: int = 0, end: int = 0, row: int = 0, col: int = 0, type: TK = TK.Null, text: str = ''):
        self.beg = beg
        self.end = end
        self.row = row
        self.col = col
        self.type = type
        self.text = text

    def __repr__(self):
        return f'{bytes(self.text, encoding="utf-8")}'
