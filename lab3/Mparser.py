#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
  ("left", "IF"),
  ("left", "ELSE"),
  ("nonassoc", "GT", "LT", "LE", "GE", "NE", "EQ"),
  ("nonassoc", "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
  ("left", "*", r"/", "DOTMUL", "DOTDIV"),
  ("left", "+", "-", "DOTADD", "DOTSUB"),
  ("left", "expr"),
  ("right", "uminus"),
  ("left", r"'")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def p_start(p):
    """START : START INSTRUCTION
             | INSTRUCTION"""
    pass
def p_instruction(p):
    """INSTRUCTION : '{' START '}'
                   | ASSIGN_EXP ';'
                   | IF_INSTRUCTION
                   | WHILE_INSTRUCTION
                   | FOR_INSTRUCTION
                   | PRINT_FUN
                   | RETURN_FUN
                   | BREAK ';'
                   | CONTINUE ';' """
    pass
def p_empty(p):
    """empty : """
    pass
def p_basic_vector_list(p):
    """VECTOR_LIST : VECTOR_LIST ',' '[' LIST_VALUE ']' %prec expr
                   | '[' LIST_VALUE ']' ',' '[' LIST_VALUE ']' """
    pass
def p_basic_matix(p):
    """MATRIX : '[' LIST_VALUE ']'
              | '[' VECTOR_LIST ']' """
    pass
def p_basic_value(p):
    """VALUE : INTNUM
             | FLOATNUM
             | ID "'"
             | ID
             | STRING
             | EYE '(' ARITHMETIC_EXP ')'
             | ZEROS '(' ARITHMETIC_EXP ')'
             | ONES '(' ARITHMETIC_EXP ')'
             | MATRIX
             | MATRIX "'" """
    print(p[0], p[1])
    if(len(p) == 2): p[0] = p[1]
def p_basic_list_values(p):
    """LIST_VALUE : VALUE
                  | VALUE ',' LIST_VALUE"""
    pass
def p_basic_arithmetic_op(p):
    """ARITHMETIC_OP : '+'
                     | '-'
                     | '*'
                     | '/'
                     | DOTADD
                     | DOTSUB
                     | DOTMUL
                     | DOTDIV """
    p[0] = p[1]
def p_basic_assign_op(p):
    """ASSIGN_OP : ADDASSIGN
                 | SUBASSIGN
                 | MULASSIGN
                 | DIVASSIGN
                 | '=' """
    pass
def p_basic_relation_op(p):
    """RELATION_OP : GT
                   | LT
                   | LE
                   | GE
                   | NE
                   | EQ """
    pass
def p_exp_arithmetic(p):
    """ARITHMETIC_EXP : ARITHMETIC_EXP ARITHMETIC_OP ARITHMETIC_EXP %prec expr
                     | '(' ARITHMETIC_EXP ')'
                     | ARITHMETIC_OP_UNARY ARITHMETIC_EXP %prec uminus
                     | VALUE"""
    pass
def p_basic_arithmetic_op_unar(p):
    """ARITHMETIC_OP_UNARY : '+'
                           | '-' """
    pass
def p_exp_relation(p):
    """RELATION_EXP : ARITHMETIC_EXP RELATION_OP ARITHMETIC_EXP
                    | '(' RELATION_EXP ')'"""
    pass
def p_exp_assign(p):
    """ASSIGN_EXP : ID ASSIGN_OP ARITHMETIC_EXP
                    | ID '[' LIST_VALUE ']' ASSIGN_OP ARITHMETIC_EXP"""
    pass
def p_instruction_if(p):
    """IF_INSTRUCTION : IF '(' RELATION_EXP  ')' INSTRUCTION %prec IF
                      | IF '(' RELATION_EXP  ')' INSTRUCTION  ELSE INSTRUCTION """
    if(len(p) == 6):
        print("short if")
    else:
        print("long if")
    pass

def p_instruction_while(p):
    """WHILE_INSTRUCTION : WHILE '(' RELATION_EXP  ')' INSTRUCTION """
    pass
def p_instruction_for(p):
    """FOR_INSTRUCTION : FOR ID '=' ARITHMETIC_EXP ':' ARITHMETIC_EXP INSTRUCTION """
    pass
def p_fun_print(p):
    """PRINT_FUN : PRINT LIST_VALUE ';'"""
    pass
def p_fun_return(p):
    """RETURN_FUN : RETURN LIST_VALUE ';'"""
    pass


parser = yacc.yacc()
