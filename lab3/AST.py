

class Node(object):
    pass


class Value(Node):
    def __init__(self, value):
        self.value = value #node or not

class Transpose(Node):
    def __init__(self, value):
        self.value = value #node or not

class Eye(Node):
    def __init__(self, value):
        self.value = value
class Zeros(Node):
    def __init__(self, value):
        self.value = value
class Ones(Node):
    def __init__(self, value):
        self.value = value

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op #token
        self.left = left #node
        self.right = right #node

class UnarExpr(Node):
    def __init__(self, op, value):
        self.op = op #token
        self.value = value #node

class RelExpr(Node):
    def __init__(self, op, left, right):
        self.left = left #node
        self.op = op #token
        self.right = right #node

class Assign(Node):
    def __init__(self, target, op, value):
        self.target = target #node
        self.op = op # token
        self.value = value #node

class Ref(Node):
    def __init__(self, target, nodes):
        self.target = target #token
        self.nodes = nodes #node list

class Vector(Node):
    def __init__(self, nodes):
        self.nodes = nodes #node list

class IfExp(Node):
    def __init__(self, cond, body, orelse=None):
        self.cond = cond #node
        self.body = body #node
        self.orelse = orelse #node or none

class While(Node):
    def __init__(self, test, body):
        self.test = test #node
        self.body = body #node

class For(Node):
    def __init__(self, itera, rangeStart, rangeEnd, body):
        self.itera = itera #token
        self.rangeStart = rangeStart #node
        self.rangeEnd = rangeEnd #node
        self.body = body #node


class Print(Node):
    def __init__(self, nodes):
        self.nodes = nodes #node list

class Return(Node):
    def __init__(self, value):
        self.nodes = nodes #node list

class Break(Node):
    def __init__(self):
        pass

class Instruction(Node):
    def __init__(self, node):
        self.node = node

class InstructionSet(Node):
    # list of nodes
    def __init__(self, nodes):
        self.nodes = nodes

    def append(self, new):
        if(self.nodes is None): self.nodes = []
        self.nodes.append(new)

class Continue(Node):
    def __init__(self):
        pass

class Error(Node):
    def __init__(self):
        pass
      