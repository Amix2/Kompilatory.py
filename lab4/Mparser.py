#!/usr/bin/python

import scanner
import ply.yacc as yacc
import AST


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
             | INSTRUCTION """
    if(len(p) == 2):
        p[0]= AST.InstructionSet([])
        p[0].append(AST.Instruction(p[1]))
    else:
        p[0] = p[1]
        p[0].append(AST.Instruction(p[2]))

def p_instruction(p):
    """INSTRUCTION : '{' START '}'
                   | ASSIGN_EXP
                   | IF_INSTRUCTION
                   | WHILE_INSTRUCTION
                   | FOR_INSTRUCTION
                   | PRINT_FUN
                   | RETURN_FUN
                   | BREAK ';'
                   | CONTINUE ';' """
    if(p[1] == "BREAK"):
        p[0] = AST.Break()
    elif(p[1] == "CONTINUE"):
        p[0] = AST.Continue()
    elif(len(p) < 3):
        p[0] = AST.Instruction(p[1])
    else:
        p[0] = p[2]

def p_basic_vector(p):
    """VECTOR : '[' LIST_VALUE ']'"""
    p[0] = AST.Vector(p[2])

def p_basic_value(p):
    """VALUE : INTNUM
             | FLOATNUM
             | ID
             | STRING
             | EYE '(' ARITHMETIC_EXP ')'
             | ZEROS '(' ARITHMETIC_EXP ')'
             | ONES '(' ARITHMETIC_EXP ')'
             | VECTOR
             | ID VECTOR
             | VALUE "'" """
    if(len(p) == 2):
        p[0] = AST.Value(p[1])
    elif(len(p) == 3):
        p[0] = AST.Value(AST.Transpose(AST.Value(p[1])))
    else:
        if(p[1] == "EYE"):
            p[0] = AST.Value(AST.Eye(AST.Value(p[3])))
        elif(p[1] == "ZEROS"):
            p[0] = AST.Value(AST.Zeros(AST.Value(p[3])))
        else:
            p[0] = AST.Value(AST.Ones(AST.Value(p[3])))

def p_basic_list_values(p):
    """LIST_VALUE : VALUE
                  | VALUE ',' LIST_VALUE"""
    if(len(p) == 2):
        p[0] = []
        p[0].append(AST.Value(p[1]))
    else:
        p[0] = p[3]
        p[0].insert(0, p[1])

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
    p[0] = p[1]

def p_basic_relation_op(p):
    """RELATION_OP : GT
                   | LT
                   | LE
                   | GE
                   | NE
                   | EQ """
    p[0] = p[1]

def p_basic_arithmetic_op_unar(p):
    """ARITHMETIC_OP_UNARY : '+'
                           | '-' """
    p[0] = p[1]

def p_exp_arithmetic(p):
    """ARITHMETIC_EXP : ARITHMETIC_EXP ARITHMETIC_OP ARITHMETIC_EXP %prec expr
                     | '(' ARITHMETIC_EXP ')'
                     | ARITHMETIC_OP_UNARY ARITHMETIC_EXP %prec uminus
                     | VALUE"""
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = AST.UnarExpr(p[1], p[2])
    elif(p[1] == "("):
        p[0] = p[2] ## uwaga
    else:
        p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_exp_relation(p):
    """RELATION_EXP : ARITHMETIC_EXP RELATION_OP ARITHMETIC_EXP
                    | '(' RELATION_EXP ')'"""
    if(p[1] == "("):
        p[0] = p[2] ## uwaga
    else:
        p[0] = AST.RelExpr(p[2], p[1], p[3])

def p_exp_assign(p):
    """ASSIGN_EXP : ID ASSIGN_OP ARITHMETIC_EXP ';'
                    | ID '[' LIST_VALUE ']' ASSIGN_OP ARITHMETIC_EXP ';' """
    if(len(p) == 5):
        p[0] = AST.Assign(AST.Value(p[1]), p[2], p[3])
    else:
        p[0] = AST.Assign(AST.Ref(p[1], p[3]), p[5], p[6])
    
def p_instruction_if(p):
    """IF_INSTRUCTION : IF '(' RELATION_EXP  ')' INSTRUCTION %prec IF
                      | IF '(' RELATION_EXP  ')' INSTRUCTION  ELSE INSTRUCTION """
    p[0] = AST.IfExp(p[3], p[5], p[7]) #uwaga

def p_instruction_while(p):
    """WHILE_INSTRUCTION : WHILE '(' RELATION_EXP  ')' INSTRUCTION """
    p[0] = AST.IfExp(p[3], p[5])

def p_instruction_for(p):
    """FOR_INSTRUCTION : FOR ID '=' ARITHMETIC_EXP ':' ARITHMETIC_EXP INSTRUCTION """
    p[0] = AST.For(p[2], p[4], p[6], p[7])
    
def p_fun_print(p):
    """PRINT_FUN : PRINT LIST_VALUE ';'"""
    p[0] = AST.Print(p[2])
def p_fun_return(p):
    """RETURN_FUN : RETURN LIST_VALUE ';'"""
    p[0] = AST.Return(p[2])


parser = yacc.yacc()
