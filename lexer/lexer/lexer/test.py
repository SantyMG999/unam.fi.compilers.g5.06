import argparse
from .lexer import Lexer
from .tok import TokenType

def run(src: str):
    lex = Lexer(src)
    cats = []
    while True:
        tk = lex.next_token()
        if tk.tokenType == TokenType.EOF:
            break
        cats.append(tk.tokenType.lower())
    print(" ".join(cats))
    print(f"Total of tokens: {len(cats)}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--str", dest="s", help="string a escanear")
    p.add_argument("--file", dest="f", help="ruta del archivo a escanear")
    a = p.parse_args()

    if a.s:
        src = a.s
    elif a.f:
        with open(a.f, "r", encoding="utf-8") as fh:
            src = fh.read()
    else:
        src = 'print("This is an example..."); int x = 10;'
    run(src)
