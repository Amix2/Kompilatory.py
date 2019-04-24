#!/usr/bin/python

class SymbolTable(object):
    """ Zwraca wartość zmmiennej oraz informacje o przestreni nazw (czy w if, while, for)
    get(var_name) -> zwraca wartość z tego poziomu lub najbliższego poniżej
    put(var_name, var_value) -> dodaje zmienną do tej przestrzeni nazw
    leave_scope() -> zwraca przestrzeń nazw 1 poziom poniżej, tracą dane w tej prestrzeni 
    create_new_empty() -> """
    def __init__(self, parent=None): # parent scope and symbol table name
        self.vars_dict = {}
        self.parent = parent
        self.inLoopScope = False

    def put(self, name, value): # value is node
        self.vars_dict[name] = value
        #print(self.vars_dict)

    def get(self, name): # get variable symbol or fundef from <name> entry
        if(name in self.vars_dict): return self.vars_dict[name]
        if(self.parent is None):    raise BaseException("Value not found " + str(name))
        else:   return self.parent.get(name)

    def isInLoopScope(self):
        return self.inLoopScope

    def create_new_scope(self, isInLoop=False):
        newScope = SymbolTable(self)
        newScope.inLoopScope = isInLoop
        return newScope

    def leave_scope(self):
        return self.parent