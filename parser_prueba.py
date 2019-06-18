import lexer_rules
import parser_rules
import lex
import yacc

lexer = lex.lex(module=lexer_rules)
parser = yacc.yacc(module=parser_rules)
text = open("texto.txt").readlines()
for i in text:
    ast = parser.parse(i, lexer)
    print (ast)
