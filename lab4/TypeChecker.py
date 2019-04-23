#!/usr/bin/python
import AST

good_operations_and_types = {
    ("int", "int", "+") : "int",
    ("int", "int", "-") : "int",
    ("int", "int", "*") : "int",
    ("int", "int", "/") : "int",
    ("int", "float", "+") : "float",
    ("int", "float", "*") : "float",
    ("int", "float", "-") : "float",
    ("int", "float", "/") : "float",
    ("float", "float", "+") : "float",
    ("float", "float", "*") : "float",
    ("float", "float", "-") : "float",
    ("float", "float", "/") : "float",
    ("string", "string", "+") : "int",
    ("vector", "vector", ".+") : "vector",
    ("vector", "vector", ".-") : "vector",
    ("vector", "vector", ".*") : "vector",
    ("vector", "vector", "./") : "vector"
}

class ValueType():
    def __init__(self, node):
        if(isinstance(node, AST.Int)):
            self.type = "int"
        elif(isinstance(node, AST.Float)):
            self.type = "float"
        elif(isinstance(node, AST.String)):
            self.type = "string"
        elif(isinstance(node, AST.Vector)):
            self.type = "vector"
            if(isinstance(node.nodes[0], list)):
                self.shape = (len(node.nodes), len(node.nodes[0]))
            else:
                self.shape = (1, len(node.nodes))
                

def is_good_operation(operation, node1, node2=None): # binExpr, Transpose, RelExpr, UnarExpr, Eye itp
    if(operation[0] == "."):    oper_type = "matrix"
    else:   oper_type = "simple"
    

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
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
    # zwracamy AST.Int itp... + AST.Vector
    """
    czyli do każdego noda sprawdzamy wszystkie potrzebne nody dzieci i potem sprawdzamy czy da sie wykonać operacje na nich
    
    """
    def visit_String(self, node):
        return ValueType(node)

    def visit_Int(self, node):
        return ValueType(node)

    def visit_Float(self, node):
        return ValueType(node)

    def visit_Vector(self, node):
        return ValueType(node)

    def visit_Id(self, node): ##        TO DO
        pass

    def visit_Value(self, node):
        return self.visit(node.value) 

    def visit_Transpose(self, node):
        valueType = self.visit(node.value)
        if(valueType.type != "vector"):
            

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    def visit_(self, node):
        pass

    

    def visitor_Assign(self, node):
            pass
    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        
        # ... 
        #
 

    def visit_Variable(self, node):
        pass
        

