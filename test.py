import sys
import ply.lex as lex
import ply.yacc as yacc
literals = [ '+','-','*','/','(',')', "<", "=" ]

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'ID',
    'FOR',
)
#t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ID = r'[a-z|A-Z|_] [a-z|A-Z|0-9]*'
t_ignore = ' \t'

def t_FOR(t):
    r'for | FOR'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    print("line %d: illegal character '%s'" %(t.lineno, t.value[0]) )
    t.lexer.skip(1)



lexer = lex.lex()
fh = None
try:

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        fh = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)
    inp = fh.read()
    lexer.input( inp )
    for token in lexer:
        print("line %d: %s(%s)" %(find_column(inp,token), token.type, token.value))
except:
    print("open error\n")