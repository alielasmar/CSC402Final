from typing import List
from typing import Union

class Number:
    def __init__(self, value: float):
        self.value = value

class Variable:
    def __init__(self, name: str):
        self.name = name

class UnaryOperator:
    def __init__(self, op: str, right):
        self.op = op
        self.right = right

class BinaryOperator:
    def __init__(self, op: str, left, right):
        self.op = op
        self.left = left
        self.right = right

class IfStatement:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body

class ForLoop:
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

class PrintStatement:
    def __init__(self, values: List):
        self.values = values

class InputStatement:
    def __init__(self, prompt: str):
        self.prompt = prompt
        
class FunctionCall:
    def __init__(self, name: str, args: List[Union[Number, Variable]]):
        self.name = name
        self.args = args