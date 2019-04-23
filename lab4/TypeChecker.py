#!/usr/bin/python
import AST

good_operations_and_types = {
    (AST.Int.__name__, AST.Int.__name__, "+") : AST.Int,
    (AST.Int.__name__, AST.Int.__name__, "*") : AST.Int,
    (AST.Int.__name__, AST.Int.__name__, "-") : AST.Int,
    (AST.Int.__name__, AST.Int.__name__, "/") : AST.Int,
    (AST.Float.__name__, AST.Int.__name__, "+") : AST.Float,
    (AST.Float.__name__, AST.Int.__name__, "*") : AST.Float,
    (AST.Float.__name__, AST.Int.__name__, "-") : AST.Float,
    (AST.Float.__name__, AST.Int.__name__, "/") : AST.Float,
    (AST.Float.__name__, AST.Float.__name__, "+") : AST.Float,
    (AST.Float.__name__, AST.Float.__name__, "*") : AST.Float,
    (AST.Float.__name__, AST.Float.__name__, "-") : AST.Float,
    (AST.Float.__name__, AST.Float.__name__, "/") : AST.Float,
    (AST.String.__name__, AST.String.__name__, "+") : AST.String,
    (AST.Vector.__name__, AST.Vector.__name__, "+") : AST.Vector,
    (AST.Vector.__name__, AST.Vector.__name__, "-") : AST.Vector,
    (AST.Vector.__name__, AST.Vector.__name__, "*") : AST.Vector,
    (AST.Vector.__name__, AST.Vector.__name__, "/") : AST.Vector
}

class ValueType():
    def __init__(self, node):
        if(isinstance(node, AST.Int)):
            self.type = "int"
        elif(isinstalce(node, AST.Float)):
            self.type = "float"
        elif(isinstance(node, AST.String)):
            self.type = "string"
        elif(isinstance(node, AST.Vector)):
            self.type = "vector"

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
        

