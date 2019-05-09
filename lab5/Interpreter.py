
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

def LOG(*args):
    print(*args)

class Interpreter(object):

    @on('node')
    def visit(self, node):
        print("pass")
        pass
    

    @when(AST.Vector)
    def visit(self, node):
        base_node_list = []
        for n in node.nodes:
            base_node_list.append(n.accept())
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
      return symbolTable.get(node.value) # value or error
    
    @when(AST.Transpose)
    def visit(self, node):
        pass
    
    @when(AST.Eye)
    def visit(self, node):
        pass
    
    @when(AST.Zeros)
    def visit(self, node):
        pass
    
    @when(AST.Ones)
    def visit(self, node):
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self) # AST.Int / .Float / .String / .Vector
        oper_fun = functions_for_operations[node.op]
        print(oper_fun(r1, r2))
        return oper_fun(r1, r2)
    
    @when(AST.UnarExpr)
    def visit(self, node):
        pass
    
    @when(AST.RelExpr)
    def visit(self, node):
        pass
    
    @when(AST.Assign)
    def visit(self, node):          # TODO poprawić try excepty
        rVal = node.value.accept();
        op = node.op
        try:
            target = node.target.value # string nazwa ID
        except Exception:
            target = node.target.target
        targetVal = None    # wartość, lista z ref, None
        try:
            targetVal = node.target.accept()
        except BaseException:
            pass

        if(op=="="):
            if(not isinstance(targetVal, list)): 
                targetVal = symbolTable.get(target)
                if ref.len() == 2:
                    target2[ref[0], ref[1]] == value
                #else
                    #target[]
            symbolTable.put(target, rVal, ref = targetVal)
            

        
    @when(AST.Ref)
    def visit(self, node):
        valList = []
        for n in node.nodes:
            valList.append(n.accept())
        LOG(valList)
        return valList
    
    @when(AST.Vector)
    def visit(self, node):
        pass
    
    @when(AST.IfExp)
    def visit(self, node):
        pass
    
    @when(AST.While)
    def visit(self, node):
        pass
    
    @when(AST.For)
    def visit(self, node):
        pass
    
    @when(AST.Print)
    def visit(self, node):
        pass
    
    @when(AST.Return)
    def visit(self, node):
        pass
    
    @when(AST.Break)
    def visit(self, node):
        pass
    
    @when(AST.Instruction)
    def visit(self, node):
        pass
    
    @when(AST.InstructionSet)
    def visit(self, node):
        pass
    
    @when(AST.Continue)
    def visit(self, node):
        pass
    
    @when(AST.Error)
    def visit(self, node):
        pass
    
   