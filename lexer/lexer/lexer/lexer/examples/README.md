# Lexer - Compiladores
Python 3.10+.

## Ejecutar con cadena
python -m lexer.test --str 'print("This is an example..."); int x = 10;'

## Ejecutar con archivo
python -m lexer.test --file examples/input1.txt

## Salida esperada
keyword identifier operator constant punctuation
Total of tokens: 5
