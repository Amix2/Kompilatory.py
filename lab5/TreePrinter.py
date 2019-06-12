from __future__ import print_function
import AST
import inspect    

def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("| "*indent + "\"" + str(self.value) + "\"")
    @addToClass(AST.Int)
    def printTree(self, indent=0):
        print("| "*indent +str(self.value))
    @addToClass(AST.Float)
    def printTree(self, indent=0):
        print("| "*indent + str(self.value))
    @addToClass(AST.Id)
    def printTree(self, indent=0):
        print("| "*indent + str(self.value))
    

    @addToClass(AST.Value)
    def printTree(self, indent=0):
        ## to do
        if(isinstance(self.value, AST.Node)):
            self.value.printTree(indent) ## indent ++
        else:
            print("| "*indent + str(self.value))

    @addToClass(AST.InstructionSet)
    def printTree(self, indent=0):
        for node in self.nodes:
            node.printTree(indent)

    @addToClass(AST.Instruction)
    def printTree(self, indent=0):
        self.node.printTree(indent)

    @addToClass(AST.Assign)
    def printTree(self, indent=0):
        print("| "*indent + str(self.op))
        self.target.printTree(indent+1)
        self.value.printTree(indent+1)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("| "*indent + str(self.op))
        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.Transpose)
    def printTree(self, indent=0):
        print("| "*indent + "Transpose")
        if(isinstance(self.value, AST.Node)):
            self.value.printTree(indent+1)
        #else:            print("| "*(indent+1) + str(self.value))

    @addToClass(AST.Eye)
    def printTree(self, indent=0):
        print("| "*indent + "Eye")
        self.value.printTree(indent+1)

    @addToClass(AST.Zeros)
    def printTree(self, indent=0):
        print("| "*indent + "Zeros")
        self.value.printTree(indent+1)

    @addToClass(AST.Ones)
    def printTree(self, indent=0):
        print("| "*indent + "Ones")
        self.value.printTree(indent+1)

    @addToClass(AST.UnarExpr)
    def printTree(self, indent=0):
        print("| "*indent + str(self.op))
        self.value.printTree(indent+1)

    @addToClass(AST.RelExpr)
    def printTree(self, indent=0):
        print("| "*indent + str(self.op))
        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.Ref)
    def printTree(self, indent=0):
        print(self.target.value)
        #print("| "*indent + self.target.value)
        self.target.printTree(indent)
        print("| "*indent + "Ref")
        for node in self.nodes:
            node.printTree(indent+1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("| "*indent + "Vector")
        for node in self.nodes:
            node.printTree(indent+1)

    @addToClass(AST.IfExp)
    def printTree(self, indent=0):
        print("| "*indent + "If")
        self.cond.printTree(indent+1)
        print("| "*indent + "Then")
        self.body.printTree(indent+1)
        if(self.orelse is not None):
            print("| "*indent + "Else")
            self.orelse.printTree(indent+1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print("| "*indent + "While")
        self.test.printTree(indent+1)
        print("| "*indent + "Do")
        self.body.printTree(indent+1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("| "*indent + "For")
        self.itera.printTree(indent+1)
        print("| "*(indent+1) + "Range")
        self.rangeStart.printTree(indent+2)
        self.rangeEnd.printTree(indent+2)
        print("| "*indent + "Do")
        self.body.printTree(indent+1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("| "*indent + "Print")
        for node in self.nodes:
            node.printTree(indent+1)

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print("| "*indent + "Return")
        for node in self.nodes:
            node.printTree(indent+1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print("| "*indent + "Break")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print("| "*indent + "Continue")
