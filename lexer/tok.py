class Tok:
    def __init__(self, tokenType: str, literal: str):
        self.tokenType = tokenType
        self.literal = literal
    def __str__(self):
        return f"{self.tokenType}: {self.literal}"

class TokenType:
    KEYWORD = "KEYWORD"
    PUNCTUATION = "PUNCTUATION"
    IDENTIFIER = "IDENTIFIER"
    OPERATOR = "OPERATOR"
    CONSTANT = "CONSTANT"
    EOF = "EOF"
    INVALID = "INVALID"

KEYWORDS = {"print", "int", "var"}

def keyword_or_identifier(identifier: str) -> str:
    return TokenType.KEYWORD if identifier in KEYWORDS else TokenType.IDENTIFIER
