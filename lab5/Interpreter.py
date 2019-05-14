
import AST

from SymbolTable import SymbolTable
from Exceptions import *
from visit import *
import numpy
import sys

sys.setrecursionlimit(10000)


def add_f(a, b):    return a+b;
def sub_f(a, b):    return a-b;
def mul_f(a, b):    return a*b;
def div_f(a, b):    return a/b;
def pass_f(a, b):   return a;

def dotAdd_f(a, b): return numpy.add(a,b).tolist()
def dotSub_f(a, b): return numpy.substract(a,b).tolist()
def dotMul_f(a,b):  return numpy.dot(a,b).tolist()
def dotDiv_f(a,b):  return numpy.divide(a,b).tolist()
functions_for_operations = {
    "+" : add_f,
    "-" : sub_f,
    "*" : mul_f,
    "/" : div_f,
    "=" : pass_f,
    ".+" : dotAdd_f,
    ".-" : dotSub_f,
    ".*" : dotMul_f,
    "./" : dotDiv_f,
};

def LOG(*args):
    print(*args)
    pass

class Interpreter(object):
    def __init__(self):
        self.symbolTable = SymbolTable()
        
    @on('node')
    def visit(self, node):
        print("pass")
        pass

    @when(AST.Vector)
    def visit(self, node):
        base_node_list = []
        for n in node.nodes:
            base_node_list.append(n.accept(self))
        LOG("Vector", str(base_node_list))
        return base_node_list

    @when(AST.Int)
    def visit(self, node):
        LOG("int", node.value)
        return node.value 
        
    @when(AST.String)
    def visit(self, node):
        LOG("string", node.value)
        return node.value 

    @when(AST.Float)
    def visit(self, node):
        LOG("float", node.value)
        return node.value 
    
    @when(AST.Id)
    def visit(self, node):
        LOG("id", node.value)
        return self.symbolTable.get(node.value) # value or error
    
    @when(AST.Transpose)
    def visit(self, node):
        vector = node.value.accept(self) # list / list of lists
        vector_trans = numpy.transpose(vector).tolist()
        LOG("Transpose", vector_trans)
        return vector_trans
    
    @when(AST.Eye)
    def visit(self, node):
        shape = node.value.accept(self)
        vector = numpy.eye(shape).tolist()
        LOG("eye", vector)
        return vector
    
    @when(AST.Zeros)
    def visit(self, node):
        shape = node.value.accept(self)
        vector = numpy.zeros((shape,shape)).tolist()
        LOG("Zeros", vector)
        return vector
    
    @when(AST.Ones)
    def visit(self, node):
        shape = node.value.accept(self)
        vector = numpy.ones((shape,shape)).tolist()
        LOG("Ones", vector)
        return vector

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self) # AST.Int / .Float / .String / .Vector
        oper_fun = functions_for_operations[node.op]
        return oper_fun(r1, r2)
    
    @when(AST.UnarExpr)
    def visit(self, node):
        if(node.op == "+"): return node.value
        else:   return -node.value
    
    @when(AST.RelExpr)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        op = node.op
        if(op == ">"): return left > right;
        if(op == "<"): return left < right;
        if(op == "=="): return left == right;
        if(op == "!="): return left != right;
        if(op == ">="): return left >= right;
        if(op == "<="): return left <= right;       
            
    @when(AST.Assign)
    def visit(self, node):          # TODO poprawić try excepty
        #   = / +=...
        #   ref / id
        rVal = node.value.accept(self);
        op = node.op

        try:
            target = node.target.value # string nazwa ID
        except Exception:
            target = node.target.target

        if(node.target.__class__.__name__ == "Ref"):
            #   ref 
            target = node.target.target.value
            ref_values = []
            for n in node.target.nodes:
                ref_values.append(n.accept(self))
            vector_value = self.symbolTable.get(target)
            oper_fun = functions_for_operations[op[0]]
            LOG("Assign ref", oper_fun, ref_values)
            if(len(ref_values) == 1):
                # 1 elem
                vector_value[int(ref_values[0])] = oper_fun(rVal, vector_value[int(ref_values[0])]);
            else:
                # 2 elem
                vector_value[int(ref_values[0])][int(ref_values[1])] = oper_fun(rVal, vector_value[int(ref_values[0])][int(ref_values[1])]);
            self.symbolTable.put(target, vector_value)
        else:
            #   normal
            target = node.target.value
            try:
                target_value = node.target.accept(self) # wartość pod ID jesli trzeba
            except BaseException:
                target_value = None
            oper_fun = functions_for_operations[op[0]]
            LOG("Assign id", oper_fun, target_value)
            new_value = oper_fun(rVal, target_value)
            self.symbolTable.put(target, new_value)
        LOG("Symbol table", self.symbolTable.vars_dict)           

        
    @when(AST.Ref)
    def visit(self, node):
        target = node.target.value # string z ID
        vector_value = self.symbolTable.get(target)
        ref_values = []
        for n in node.nodes:
                ref_values.append(n.accept(self))
        if(len(ref_values) == 1):
            # 1 elem
            A = vector_value[int(ref_values[0])];
        else:
            # 2 elem
            A = vector_value[int(ref_values[0])][int(ref_values[1])];
            
        LOG("Ref", A, target, ref_values)
        return A
        
    @when(AST.IfExp)
    def visit(self, node):
        self.symbolTable = self.symbolTable.create_new_scope()
        cond = node.cond.accept(self)
        LOG("IF", cond, node.body, node.orelse)
        if(cond):
            node.body.accept(self)
        else:
            if(node.orelse is not None):
                node.orelse.accept(self)
        self.symbolTable = self.symbolTable.leave_scope()
    
    @when(AST.While)
    def visit(self, node):
        self.symbolTable = self.symbolTable.create_new_scope()
        while(node.test.accept(self)):
            try:
                node.body.accept(self)
            except ContinueException:
                LOG("ContinueException")
                continue
            except BreakException:
                LOG("BreakException")
                break
        self.symbolTable = self.symbolTable.leave_scope()
    
    @when(AST.For)
    def visit(self, node):
        self.symbolTable = self.symbolTable.create_new_scope()
        iterator_name = node.itera.target
        rangeStart = node.rangeStart.accept(self)
        rangeEnd = node.rangeEnd.accept(self)
        self.symbolTable.put(iterator_name, rangeStart)
        while(self.symbolTable.get(iterator_name) < rangeEnd):
            try:
                node.body.accept(self)
            except ContinueException:
                LOG("ContinueException")
            except BreakException:
                LOG("BreakException")
                break

            self.symbolTable.put(iterator_name, self.symbolTable.get(iterator_name)+1)

        self.symbolTable = self.symbolTable.leave_scope()
    
    @when(AST.Print)
    def visit(self, node):
        print_list = [];
        for n in node.nodes:
            print_list.append(n.accept(self))
        print(print_list)
    
    @when(AST.Return)
    def visit(self, node):
        LOG("Return")
        ret_vals = []
        for n in node.nodes:
            ret_vals.append(n.accept(self))
        raise ReturnValueException(ret_vals)
    
    @when(AST.Break)
    def visit(self, node):
        LOG("break")
        raise BreakException()
    
    @when(AST.Instruction)
    def visit(self, node):
        LOG("Instruction", str(node.node))
        node.node.accept(self)
        
    
    @when(AST.InstructionSet)
    def visit(self, node):
        LOG("InstructionSet", node.nodes)
        for n in node.nodes:
            n.accept(self)
    
    @when(AST.Continue)
    def visit(self, node):
        LOG("Continue")
        raise ContinueException()
    
    @when(AST.Error)
    def visit(self, node):
        pass
    
   