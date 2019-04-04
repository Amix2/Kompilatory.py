

class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class RelExpr(Node):
    def __init__(self, left, ops, comparators):
        self.left = left
        self.ops = ops
        self.comparators = comparators

class Assign(Node):
    def __init__(self, target, op, value):
        self.op = op
        self.target = target
        self.value = value

class IfExp(Node):
    def __init__(self, test, body, orelse):
        self.test = test
        self.body = body
        self.orelse = orelse

class While(Node):
    def __init__(self, test, body, orelse):
        self.test = test
        self.body = body
        self.orelse = orelse

class For(Node):
    def __init__(self, target, itera, body, orelse):
        self.target = target
        self.itera = itera
        self.body = body
        self.orelse = orelse

class Break(Node):
    def __init__(self):
        pass

class Return(Node):
    def __init__(value):
        self.value = value

class Continue(Node):
    def __init__(self):
        pass

class PrintFun(Node):
    def __init__(self, values):
        self.values = values

class Error(Node):
    def __init__(self):
        pass
      