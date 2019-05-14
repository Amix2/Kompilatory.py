

class Node(object):
    def accept(self, visitor):
        return visitor.visit(self)
    pass


class String(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value  # Token


class Int(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value  # Token


class Float(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value  # Token


class Id(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value  # token


class Value(Node):
    def __init__(self, value, poz):
        print("QQQ VVALUEEEEEEEEEEEEEEE")
        self.poz = poz
        self.value = value  # node or not


class Transpose(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value  # node or not


class Eye(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value


class Zeros(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value


class Ones(Node):
    def __init__(self, value, poz):
        self.poz = poz
        self.value = value


class BinExpr(Node):
    def __init__(self, op, left, right, poz):
        self.poz = poz
        self.op = op  # token
        self.left = left  # node
        self.right = right  # node


class UnarExpr(Node):
    def __init__(self, op, value, poz):
        self.poz = poz
        self.op = op  # token
        self.value = value  # node


class RelExpr(Node):
    def __init__(self, op, left, right, poz):
        self.poz = poz
        self.left = left  # node
        self.op = op  # token
        self.right = right  # node


class Assign(Node):
    def __init__(self, target, op, value, poz):
        self.poz = poz
        self.target = target  # node
        self.op = op  # token
        self.value = value  # node


class Ref(Node):
    def __init__(self, target, nodes, poz):
        self.poz = poz
        self.target = target  # token
        self.nodes = nodes  # node list


class Vector(Node):
    def __init__(self, nodes, poz):
        self.poz = poz
        self.nodes = nodes  # node list


class IfExp(Node):
    def __init__(self, cond, body, orelse, poz):
        self.poz = poz
        self.cond = cond  # node
        self.body = body  # node
        self.orelse = orelse  # node or none


class While(Node):
    def __init__(self, test, body, poz):
        self.poz = poz
        self.test = test  # node
        self.body = body  # node


class For(Node):
    def __init__(self, itera, rangeStart, rangeEnd, body, poz):
        self.poz = poz
        self.itera = itera  # node ID_GR
        self.rangeStart = rangeStart  # node VAL
        self.rangeEnd = rangeEnd  # node VAL(int?)
        self.body = body  # node


class Print(Node):
    def __init__(self, nodes, poz):
        self.poz = poz
        self.nodes = nodes  # node list


class Return(Node):
    def __init__(self, nodes, poz):
        self.poz = poz
        self.nodes = nodes  # node list


class Break(Node):
    def __init__(self, poz):
        pass


class Instruction(Node):
    def __init__(self, node, poz):
        self.poz = poz
        self.node = node


class InstructionSet(Node):
    # list of nodes
    def __init__(self, nodes, poz):
        self.poz = poz
        self.nodes = nodes

    def append(self, new):
        if(self.nodes is None):
            self.nodes = []
        self.nodes.append(new)


class Continue(Node):
    def __init__(self, poz):
        pass


class Error(Node):
    def __init__(self, poz):
        pass
