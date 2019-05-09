#!/usr/bin/python
import AST
from SymbolTable import SymbolTable

good_operations_and_types = {
    ("int", "int", "+") : "int",
    ("int", "int", "-") : "int",
    ("int", "int", "*") : "int",
    ("int", "int", "/") : "int",
    ("int", "float", "+") : "float",
    ("int", "float", "*") : "float",
    ("int", "float", "-") : "float",
    ("int", "float", "/") : "float",

    ("float", "int", "+") : "float",
    ("float", "int", "*") : "float",
    ("float", "int", "-") : "float",
    ("float", "int", "/") : "float",

    ("float", "float", "+") : "float",
    ("float", "float", "*") : "float",
    ("float", "float", "-") : "float",
    ("float", "float", "/") : "float",

    ("string", "string", "+") : "string",

    ("vector", "float", "+") : "vector",
    ("vector", "float", "-") : "vector",
    ("vector", "float", "*") : "vector",
    ("vector", "float", "/") : "vector",
    
    ("float", "vector", "+") : "vector",
    ("float", "vector", "*") : "vector",

    ("vector", "int", "+") : "vector",
    ("vector", "int", "-") : "vector",
    ("vector", "int", "*") : "vector",
    ("vector", "int", "/") : "vector",
    
    ("int", "vector", "+") : "vector",
    ("int", "vector", "*") : "vector",

    ("vector", "vector", ".+") : "vector",
    ("vector", "vector", ".-") : "vector",
    ("vector", "vector", ".*") : "vector",
    ("vector", "vector", "./") : "vector",

    ("int", "int", "CMP") : "int",
    ("float", "float", "CMP") : "int",
    ("int", "float", "CMP") : "int",
    ("float", "int", "CMP") : "int",

    ("vector", "vector", "==") : "int",
    ("string", "string", "==") : "int",
    ("vector", "vector", "!=") : "int",
    ("string", "string", "!=") : "int"
}


class ValueType():
    def __init__(self, node, value=None):
        #("vector", size)
        if(isinstance(node, AST.Int)):
            self.type = "int"
        elif(isinstance(node, AST.Float)):
            self.type = "float"
        elif(isinstance(node, AST.String)):
            self.type = "string"
        elif(isinstance(node, AST.Vector)): # vector
            self.type = "vector"
            if(isinstance(node.nodes[0], AST.Vector)): # [[1,2], [3+5,4]]
                self.shape = (len(node.nodes), len(node.nodes[0]))
            else:   # [1,2]
                self.shape = (1, len(node.nodes))
        elif(isinstance(node, str)):
            self.type = node
            if(node == "vector"):
                self.shape = value
        else:
            raise BaseException("ValueType Init error")


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method)
        return visitor(node)

    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)



class TypeChecker(NodeVisitor):
    """
    czyli do każdego noda sprawdzamy wszystkie potrzebne nody dzieci i potem sprawdzamy czy da sie wykonać operacje na nich
    
    """
    def __init__(self):
        self.symbols = SymbolTable()
    def visit_String(self, node):
        return ValueType(node)

    def visit_Int(self, node):
        return ValueType(node)

    def visit_Float(self, node):
        return ValueType(node)

    def visit_Vector(self, node): # [[1,2], [3+5,4], 34]
        # różne długości wektorów
        # różne typy
        val_inside_type = self.visit(node.nodes[0])
        if(val_inside_type.type == "vector"):
            # matrix
            good_shape = self.visit(node.nodes[0]).shape

            for vector in node.nodes:
                vector_type = self.visit(vector)
                if(vector_type.type != "vector"):
                    raise BaseException("Wrong matrix types")
                if(vector_type.shape[0] != 1
                    or (good_shape != vector_type.shape)):
                    raise BaseException("Wrong dimentions")
            return ValueType("vector", (len(node.nodes), good_shape[1]))

        else:
            # vector
            for val in node.nodes:  # all elements are int of float
                val_type = self.visit(val)
                if(val_type.type not in ("int", "float")):
                    raise BaseException("wrong value type")
            return ValueType(node) # vector (1,x)
            

    def visit_Id(self, node):
        value = ValueType(self.symbols.get(node.value).type)
        if(value.type == "vector"):
            value.shape = self.symbols.get(node.value).shape
        value.target = node.value
        return value

    def visit_Value(self, node):
        return self.visit(node.value) 

    def visit_Transpose(self, node):
        valueType = self.visit(node.value)
        if(valueType.type != "vector"):
            raise BaseException("Transpose not a vector")
        valueType.shape = valueType.shape[::-1]
        return valueType

    def visit_Eye(self, node):
        valueType = self.visit(node.value)
        if(valueType.type != "int"):
            raise BaseException("Eye with not int")
        return ValueType("vector", (node.value.value.value, node.value.value.value))

    def visit_Zeros(self, node):
        valueType = self.visit(node.value)
        if(valueType.type != "int"):
            raise BaseException("Zeros with not int")
        return ValueType("vector", (node.value.value.value, node.value.value.value))

    def visit_Ones(self, node):
        valueType = self.visit(node.value)
        if(valueType.type != "int"):
            raise BaseException("Ones with not int")
        return ValueType("vector", (node.value.value.value, node.value.value.value))

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        if(type1.type == "vector" and type2.type == "vector"):
            if(type1.shape != type2.shape):
                raise BaseException("Wrong dimentions in expresion")
        if( not (type1.type, type2.type, op) in good_operations_and_types):
            raise BaseException("Wrong operators")
        return ValueType(good_operations_and_types[(type1.type, type2.type, op)])

    def visit_UnarExpr(self, node):
        return self.visit(node.left) 

    def visit_RelExpr(self, node): 
        type1 = self.visit(node.left)   
        type2 = self.visit(node.right)
        op    = node.op
        if( not (type1.type, type2.type, op) in good_operations_and_types 
            and not (type1.type, type2.type, "CMP") in good_operations_and_types):
            raise BaseException("Wrong compare operators")
        return ValueType("int")

    def visit_Assign(self, node):   ##      wsadzanie do tablicy ID
        type_value = self.visit(node.value)
        op    = node.op
        if(op == "="): 
            if(not isinstance(node.target, AST.Ref)):
                self.symbols.put(node.target.value, type_value)
            return type_value
        type_target = self.visit(node.target) 
        op = op[:-1]
        if( not (type_target.type, type_value.type, op) in good_operations_and_types):
            if(not (type_target.type, type_value.type, "."+op) in good_operations_and_types):
                raise BaseException("Wrong assign operator")
            else:
                op = "." + op
        out_valueType = ValueType(good_operations_and_types[(type_target.type, type_value.type, op)]) 
        if(not isinstance(node.target, AST.Ref)):
            self.symbols.put(type_target.target, out_valueType)
        return out_valueType

    def visit_Ref(self, node): # A[1,2] = 1
        type_target = self.visit(node.target)  
        if(type_target.type != "vector"):
            raise BaseException("Reference to not vector")
        if(len(node.nodes) > 2):
            raise BaseException("Reference with too long vector")
        for node in node.nodes:
            type_node = self.visit(node)   
            if(type_node.type != "int"):
                raise BaseException("Wrong access operator value")
        return ValueType("float")
        

    def visit_IfExp(self, node):
        self.symbols = self.symbols.create_new_scope(True)  
        self.visit(node.cond)  
        self.visit(node.body)  
        if(node.orelse): self.visit(node.orelse) 
        self.symbols = self.symbols.leave_scope() 

    def visit_While(self, node):
        self.symbols = self.symbols.create_new_scope(True)  
        self.visit(node.test)  
        self.visit(node.body)
        self.symbols = self.symbols.leave_scope()

    def visit_For(self, node):  # dodaje do przestrzeni nazw
        self.symbols = self.symbols.create_new_scope(True)  
        iter_type = node.itera.value # self.visit(node.itera)
        self.symbols.put(iter_type, ValueType("int"))
        rangeStart = self.visit(node.rangeStart)
        if(rangeStart.type != "int"):   raise BaseException("rangeStart not int")
        rangeEnd = self.visit(node.rangeEnd)
        if(rangeEnd.type != "int"):   raise BaseException("rangeEnd not int")
        self.visit(node.body)
        self.symbols = self.symbols.leave_scope()

    def visit_Print(self, node):
        for val in node.nodes:
            self.visit(val)

    def visit_Return(self, node):
        for val in node.nodes:
            self.visit(val)

    def visit_Break(self, node):
        if(not self.symbols.isInLoopScope()):
            raise BaseException("Break not in scope")

    def visit_Continue(self, node):     # sprawdzanie scopa
        if(not self.symbols.isInLoopScope()):
            raise BaseException("Continue not in scope")

    def visit_InstructionSet(self, node):
        for val in node.nodes:
            self.visit(val)
    
    def visit_Instruction(self, node):
        try:
            if(isinstance(node.node, AST.InstructionSet)):
                self.symbols = self.symbols.create_new_scope(False)
                self.visit(node.node)
                self.symbols = self.symbols.leave_scope()
            else:
                self.visit(node.node)
        except BaseException as e:
            print("ERROR: [" + str(node.poz) + "] " + str(e))
