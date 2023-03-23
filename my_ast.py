class Program:
    def __init__(self, statements):
        self.statements = statements

class Number:
    def __init__(self, value):
        self.value = value

class Variable:
    def __init__(self, name):
        self.name = name

class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class UnaryOp:
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

class Assignment:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

class PrintStatement:
    def __init__(self, values):
        self.values = values

class InputStatement:
    def __init__(self, variable):
        self.variable = variable