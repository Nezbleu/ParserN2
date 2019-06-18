import lexer_rules
import lex
text = "(14 - 6) * 2"
lexer = lex.lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
while token is not None:
    print token.type, token.value
    token = lexer.token()
