from .tok import Tok, TokenType, keyword_or_identifier

class Lexer:
    def __init__(self, source: str):
        self.input = source
        self.pos = 0
        self.read_pos = 0
        self.ch = ""
        self._read_char()

    def _read_char(self):
        self.ch = "" if self.read_pos >= len(self.input) else self.input[self.read_pos]
        self.pos = self.read_pos
        self.read_pos += 1

    def _peek_char(self):
        return "" if self.read_pos >= len(self.input) else self.input[self.read_pos]

    def _skip_ws(self):
        while self.ch in (" ", "\t", "\r", "\n"):
            self._read_char()

    def _read_identifier(self):
        start = self.pos
        while self.ch.isalpha() or self.ch.isdigit() or self.ch == "_":
            self._read_char()
        return self.input[start:self.pos]

    def _read_number(self):
        start = self.pos
        while self.ch.isdigit():
            self._read_char()
        return self.input[start:self.pos]

    def _read_string(self):
        self._read_char()  # skip opening "
        start = self.pos
        while self.ch != "" and self.ch != '"':
            if self.ch == "\\" and self._peek_char() == '"':
                self._read_char()
            self._read_char()
        lit = self.input[start:self.pos]
        if self.ch == '"':
            self._read_char()  # skip closing "
        return lit

    def next_token(self) -> Tok:
        self._skip_ws()

        if self.ch == "":
            return Tok(TokenType.EOF, "")

        if self.ch == '"':
            return Tok(TokenType.CONSTANT, self._read_string())

        if self.ch.isalpha() or self.ch == "_":
            ident = self._read_identifier()
            return Tok(keyword_or_identifier(ident), ident)

        if self.ch.isdigit():
            return Tok(TokenType.CONSTANT, self._read_number())

        if self.ch in ("=", "+", "-", "*", "/"):
            tok = Tok(TokenType.OPERATOR, self.ch)
            self._read_char()
            return tok

        if self.ch in (";", ",", "(", ")", "{", "}", "[", "]"):
            tok = Tok(TokenType.PUNCTUATION, self.ch)
            self._read_char()
            return tok

        tok = Tok(TokenType.INVALID, self.ch)
        self._read_char()
        return tok
