#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
  ("left", "+", "-", "DOTADD", "DOTSUB"),
  ("left", "*", r"/", "DOTMUL", "DOTDIV"),
  ("nonassoc", "LT", "GT", "LE", "GE", "NE", "EQ"),
  ("nonassoc", "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
  ("left", r"'"),
  ("nonassoc", ":", ","),
  ("left", "(", ")", "[", "]"),
  ("left", "{", "}"),
  ("right", ";"),
  ("left", "IF", "ELSE", "FOR", "WHILE")
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
    """START : '{' START '}' 
             | START START  
             | ASSIGN_EXP ';' 
             | IF_INSTR 
             | WHILE_INSTR 
             | FOR_INSTR 
             | PRINT_FUN 
             | RETURN_FUN ';'
             | BREAK ';' 
             | CONTINUE ';'"""
    pass

def p_empty(p):
    """empty :"""
    pass

def p_basic_value_single(p):
    """VALUE_SINGLE : INTNUM 
                    | FLOATNUM 
                    | ID "'"
                    | ID 
                    | STRING"""
    pass
def p_basic_list_values_single(p):
    """LIST_VALUE_SINGLE : VALUE_SINGLE 
                         | VALUE_SINGLE ',' LIST_VALUE_SINGLE"""
    pass
def p_basic_matrix_row_list(p):
    """MATRIX_ROW_LIST : '[' LIST_VALUE_SINGLE ']' ',' MATRIX_ROW_LIST 
                        | '[' LIST_VALUE_SINGLE ']' ',' '[' LIST_VALUE_SINGLE ']'"""
    pass
def p_basic_matix(p):
    """MATRIX : '[' MATRIX_ROW_LIST ']' 
              | '[' LIST_VALUE_SINGLE ']'
              | MATRIX "'" """
    pass
def p_basic_value(p):
    """VALUE : VALUE_SINGLE 
             | MATRIX  """
    pass
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
                     | DOTDIV"""
    pass
def p_basic_assign_op(p):
    """ASSIGN_OP : ADDASSIGN 
                 | SUBASSIGN 
                 | MULASSIGN 
                 | DIVASSIGN
                 | '=' """
    pass
def p_basic_relation_op(p):
    """RELATION_OP : LT 
                   | GT 
                   | LE 
                   | GE 
                   | NE 
                   | EQ"""
    pass
def p_exp_arithmetic(p):
    """ARTHMETIC_EXP : VALUE 
                     | ARITHMETIC_OP_UNAR ARTHMETIC_EXP 
                     | ARTHMETIC_EXP ARITHMETIC_OP ARTHMETIC_EXP 
                     | '(' ARTHMETIC_EXP ')' 
                     | EYE '(' ARTHMETIC_EXP ')' 
                     | ZEROS '(' ARTHMETIC_EXP ')' 
                     | ONES '(' ARTHMETIC_EXP ')'"""
    pass
def p_basic_arithmetic_op_unar(p):
    """ARITHMETIC_OP_UNAR : '+' 
                          | '-' 
                          | ARITHMETIC_OP_UNAR ARITHMETIC_OP_UNAR"""
    pass
def p_exp_relation(p):
    """RELATION_EXP : ARTHMETIC_EXP RELATION_OP ARTHMETIC_EXP 
                    | '(' RELATION_EXP ')'"""
    pass
def p_exp_assign(p):
    """ASSIGN_EXP : ID ASSIGN_OP ARTHMETIC_EXP 
                    | ID '[' LIST_VALUE ']' ASSIGN_OP ARTHMETIC_EXP"""
    pass
def p_instr_if(p):
    """IF_INSTR : IF '(' RELATION_EXP  ')' START 
                | IF '(' RELATION_EXP  ')' START ELSE START"""
    pass
def p_instr_while(p):
    """WHILE_INSTR : WHILE '(' RELATION_EXP  ')' START"""
    pass
def p_instr_for(p):
    """FOR_INSTR : FOR ID '=' ARTHMETIC_EXP ':' ARTHMETIC_EXP START"""
    pass
def p_fun_print(p):
    """PRINT_FUN : PRINT LIST_VALUE ';'"""
    pass
def p_fun_return(p):
    """RETURN_FUN : RETURN LIST_VALUE ';'"""
    pass


parser = yacc.yacc()
