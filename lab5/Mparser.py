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
    line_start = input.rfind('\n', 0, token.lineno) + 1
    return (token.lineno - line_start) + 1

def p_start(p):
    """START : START INSTRUCTION
             | INSTRUCTION """
    if(len(p) == 2):
        p[0]= AST.InstructionSet([],  p.lineno(1))
        p[0].append(AST.Instruction(p[1],  p.lineno(1)))
    else:
        p[0] = p[1]
        p[0].append(AST.Instruction(p[2],  p.lineno(2)))

def p_instruction(p):
    """INSTRUCTION : '{' START '}'
                   | ASSIGN_EXP
                   | IF_INSTRUCTION
                   | WHILE_INSTRUCTION
                   | FOR_INSTRUCTION
                   | PRINT_FUN
                   | RETURN_FUN
                   | BREAK_GR
                   | CONTINUE_GR """
    if(len(p) < 3):
        p[0] = AST.Instruction(p[1], p.lineno(1))
    else:
        p[0] = p[2]


def p_basic_vector(p):
    """VECTOR : '[' LIST_VALUE ']'"""
    p[0] = AST.Vector(p[2], p.lineno(2))

def p_basic_string(p):
    """STRING_GR : STRING"""
    p[0] = AST.String(p[1], p.lineno(1))
def p_basic_int(p):
    """INT_GR : INTNUM"""
    p[0] = AST.Int(p[1], p.lineno(1))
def p_basic_float(p):
    """FLOAT_GR : FLOATNUM"""
    p[0] = AST.Float(p[1], p.lineno(1))
def p_basic_id(p):
    """ID_GR : ID"""
    p[0] = AST.Id(p[1], p.lineno(1))

def p_basic_value(p):
    """VALUE : INT_GR
             | FLOAT_GR
             | ID_GR
             | STRING_GR
             | EYE '(' ARITHMETIC_EXP ')'
             | ZEROS '(' ARITHMETIC_EXP ')'
             | ONES '(' ARITHMETIC_EXP ')'
             | VECTOR
             | ID_GR '[' LIST_VALUE ']'
             | VALUE "'" """
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = AST.Transpose(p[1], p.lineno(1))
    else:
        if(p[2] == "[") :
            p[0] = AST.Ref(p[1], p[3], p.lineno(1))
        elif(p[1].upper() == "EYE"):
            p[0] = AST.Eye(p[3], p.lineno(3))
        elif(p[1].upper() == "ZEROS"):
            p[0] = AST.Zeros(p[3], p.lineno(3))
        elif(p[1].upper() == "ONES"):
            p[0] = AST.Ones(p[3], p.lineno(3))
    

def p_basic_list_values(p):
    """LIST_VALUE : ARITHMETIC_EXP
                  | ARITHMETIC_EXP ',' LIST_VALUE"""
    if(len(p) == 2):
        p[0] = []
        p[0].append(p[1])
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
        p[0] = AST.UnarExpr(p[1], p[2], p.lineno(1))
    elif(p[1] == "("):
        p[0] = p[2] ## uwaga
    else:
        p[0] = AST.BinExpr(p[2], p[1], p[3], p.lineno(1))

def p_exp_relation(p):
    """RELATION_EXP : ARITHMETIC_EXP RELATION_OP ARITHMETIC_EXP
                    | '(' RELATION_EXP ')'"""
    if(p[1] == "("):
        p[0] = p[2] ## uwaga
    else:
        p[0] = AST.RelExpr(p[2], p[1], p[3], p.lineno(1))

def p_exp_assign(p):
    """ASSIGN_EXP : ID_GR ASSIGN_OP ARITHMETIC_EXP ';'
                    | ID_GR '[' LIST_VALUE ']' ASSIGN_OP ARITHMETIC_EXP ';' """
    if(len(p) == 5):
        p[0] = AST.Assign(p[1], p[2], p[3], p.lineno(1))
    else:
        p[0] = AST.Assign(AST.Ref(p[1], p[3], p.lineno(1)), p[5], p[6], p.lineno(1))
    
def p_instruction_if(p):
    """IF_INSTRUCTION : IF '(' RELATION_EXP  ')' INSTRUCTION %prec IF
                      | IF '(' RELATION_EXP  ')' INSTRUCTION  ELSE INSTRUCTION """
    if(len(p) == 8): 
        p[0] = AST.IfExp(p[3], p[5], p[7], p.lineno(3)) #uwaga
    else:
        p[0] = AST.IfExp(p[3], p[5], orelse=None, poz = p.lineno(3)) #uwaga

def p_instruction_while(p):
    """WHILE_INSTRUCTION : WHILE '(' RELATION_EXP  ')' INSTRUCTION """
    p[0] = AST.While(p[3], p[5], p.lineno(3))

def p_instruction_for(p):
    """FOR_INSTRUCTION : FOR ID_GR '=' ARITHMETIC_EXP ':' ARITHMETIC_EXP INSTRUCTION """
    p[0] = AST.For(p[2], p[4], p[6], p[7], p.lineno(2))
    
def p_fun_print(p):
    """PRINT_FUN : PRINT LIST_VALUE ';'"""
    p[0] = AST.Print(p[2], p.lineno(2))
def p_fun_return(p):
    """RETURN_FUN : RETURN LIST_VALUE ';'"""
    p[0] = AST.Return(p[2], p.lineno(2))
def p_break(p):
    """BREAK_GR : BREAK ';' """
    p[0] = AST.Break(p.lineno(1))

def p_continue(p):
    """CONTINUE_GR : CONTINUE ';' """
    p[0] = AST.Continue(p.lineno(1))


parser = yacc.yacc()
