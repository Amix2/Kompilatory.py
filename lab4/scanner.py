import sys
import ply

reserved = {
    'for' : 'FOR',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT'
}

tokens = [
    "DOTADD", # .+
    "DOTSUB", # .-
    "DOTMUL", # .*
    "DOTDIV", # ./
    "ADDASSIGN", # +=
    "SUBASSIGN", # -=
    "MULASSIGN", # *=
    "DIVASSIGN", # /=
    "LT", # <
    "GT", # >
    "LE", # <=
    "GE", # >=
    "NE", # !=
    "EQ", # ==
    "ID", # [a-z|A-Z|_] [a-z|A-Z|0-9]*
    "INTNUM",
    "FLOATNUM",
    "STRING",
    ] + list(reserved.values())
literals = r"+-*/()[]{}:',;="

t_DOTADD = r"\.\+"
t_DOTSUB = r"\.-"
t_DOTMUL = r"\.\*"
t_DOTDIV = r"./"
t_ADDASSIGN = r"\+="
t_SUBASSIGN = r"-="
t_MULASSIGN = r"\*="
t_DIVASSIGN = r"/="
t_LT = r"<"
t_GT = r">"
t_LE = r"<="
t_GE = r">="
t_NE = r"!="
t_EQ = r"=="

t_FLOATNUM = r"((\d+\.\d+|\.\d+|\d+\.)([Ee][+–]?\d+)?)|\d+[Ee][+–]?\d+"
t_INTNUM = r"\d+"

t_ignore = ' \t'

def t_STRING(t):
    r"\".*?\""
    t.value = t.value[1:-1]
    return t

def t_ID(t):    
    r"[a-zA-Z_]\w*"    
    t.type = reserved.get(t.value,'ID')
    return t

def t_COMMENT(t):
    r"\#.*"
    #return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    print("line %d: illegal character '%s'" %(t.lineno, t.value[0]) )
    t.lexer.skip(1)

lexer = ply.lex.lex()