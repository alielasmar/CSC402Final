import operator
from lexer import Lexer
from my_ast import Number, BinOp


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ValueError('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == 'INTEGER':
            self.eat('INTEGER')
            return Number(token.value)
        else:
            self.error()

    def term(self):
        node = self.factor()

        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                node = BinOp(left=node, op=operator.mul, right=self.factor())
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
                node = BinOp(left=node, op=operator.truediv, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                node = BinOp(left=node, op=operator.add, right=self.term())
            elif token.type == 'MINUS':
                self.eat('MINUS')
                node = BinOp(left=node, op=operator.sub, right=self.term())

        return node

    def parse(self):
        return self.expr()