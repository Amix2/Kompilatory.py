
import AST
import SymbolTable
#from Memory import *
from SymbolTable import SymbolTable
from Exceptions import *
from visit import *
import sys

sys.setrecursionlimit(10000)

symbolTable = SymbolTable();

def add_f(a, b):    return a+b;
def sub_f(a, b):    return a-b;
def mul_f(a, b):    return a*b;
def div_f(a, b):    return a/b;
functions_for_operations = {
    "+" : add_f,
    "-" : sub_f,
    "*" : mul_f,
    "/" : div_f
    #".+" : dotAdd_f,
    #".-" : dotSub_f,
    #".*" : dotMul_f,
   # "./" : dotDiv_f,
};



class Interpreter(object):

    @on('node')
    def visit(self, node):
        pass
    
    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self) # AST.Int / .Float / .String / .Vector
        oper_fun = functions_for_operations[node.op]
        return oper_fun(r1, r2)

    @when(AST.Vector)
    def visit(self, node):
        base_node_list = []
        for n in node.nodes:
            base_node_list.append(n.accept());
        return base_node_list

    @when(AST.Int)
    def visit(self, node):
        return node.value 
        
    @when(AST.String)
    def visit(self, node):
        return node.value 

    @when(AST.Float)
    def visit(self, node):
        return node.value 
    
    @when(AST.Id)
    def visit(self, node):
        return symbolTable.get(node.value)


