#!/usr/bin/python

import ply.lex as lex;
import ply.yacc as yacc;

literals = [ '+','-','*','/','(',')' ]

tokens = ( "VAR", "NUMBER", "MUL", "DOTDIV");
t_DOTDIV = r"./"

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
#    line = t.value.lstrip()
#    i = line.find("\n")
#    line = line if i == -1 else line[:i]
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

def t_VAR(t):
    r"[a-zA-Z_]\w*"
    if(t.value == "MUL"): t.type = "MUL";
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

precedence = (
   ("left", '+', '-'),
   ("left", '*', '/'),
   ("nonassoc", "MUL"),
   ("nonassoc", "DOTDIV") )

def p_error(p):
    print("parsing error\n")

def p_start(p):
    """start : EXPRESSION"""
    print("p[1]=", p[1])

def p_expression_number(p):
    """EXPRESSION : NUMBER"""
    pass

def p_expression_var(p):
    """EXPRESSION : VAR"""
    pass


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION"""
    # 0                 1       2       3 
    pass


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION
                  | EXPRESSION MUL EXPRESSION"""
    pass
def p_expression_do(p):
    """EXPRESSION : EXPRESSION DOTDIV EXPRESSION"""
    pass

def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ']'"""
    pass

file = open("example.txt", "r");

lexer = lex.lex()
parser = yacc.yacc()
text = file.read()
parser.parse(text, lexer=lexer)



