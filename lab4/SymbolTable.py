#!/usr/bin/python


class VariableSymbol(Symbol):

    def __init__(self, name, type):
        pass
    #


class SymbolTable(object):
    """ Zwraca wartość zmmiennej oraz informacje o przestreni nazw (czy w if, while, for)
    get(var_name) -> zwraca wartość z tego poziomu lub najbliższego poniżej
    put(var_name, var_value) -> dodaje zmienną do tej przestrzeni nazw
    leave_scope() -> zwraca przestrzeń nazw 1 poziom poniżej, tracą dane w tej prestrzeni """
    def __init__(self, parent, name): # parent scope and symbol table name
        pass
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        pass
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        pass
    #

    def getParentScope(self):
        pass
    #

    def pushScope(self, name):
        pass
    #

    def popScope(self):
        pass
    #

#   x = 10
#   if(1==1) {
#       x = 5
#       y = x + x
#   }
#   print(y)
