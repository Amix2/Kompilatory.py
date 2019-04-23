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
        #raise Exception("printTree not defined in class " + self.__class__.__name__)
        for _, value in self.__dict__.items():
            if(isinstance(value, AST.Node)):
                value.printTree(indent+1)
            elif(isinstance(value, list)):
                for item in value:
                    item.printTree(indent+1)
            else:
                 print("| "*indent + str(value))
           

    