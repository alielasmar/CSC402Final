import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.pos = 0
        self.current_char = self.source_code[self.pos]
    
    def advance(self):
        self.pos += 1
        if self.pos > len(self.source_code) - 1:
            self.current_char = None
        else:
            self.current_char = self.source_code[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        
        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            
            return {'type': 'FLOAT', 'value': float(result)}
        else:
            return {'type': 'INTEGER', 'value': int(result)}
    
    def get_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        return {'type': 'IDENTIFIER', 'value': result}
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return self.get_number()
            
            if self.current_char.isalpha() or self.current_char == '_':
                return self.get_identifier()
            
            if self.current_char == '+':
                self.advance()
                return {'type': 'PLUS', 'value': '+'}
            
            if self.current_char == '-':
                self.advance()
                return {'type': 'MINUS', 'value': '-'}
            
            if self.current_char == '*':
                self.advance()
                return {'type': 'MULTIPLY', 'value': '*'}
            
            if self.current_char == '/':
                self.advance()
                return {'type': 'DIVIDE', 'value': '/'}
            
            if self.current_char == '(':
                self.advance()
                return {'type': 'LPAREN', 'value': '('}
            
            if self.current_char == ')':
                self.advance()
                return {'type': 'RPAREN', 'value': ')'}
            
            if self.current_char == '=':
                self.advance()
                return {'type': 'EQUALS', 'value': '='}
            
            if self.current_char == ',':
                self.advance()
                return {'type': 'COMMA', 'value': ','}
            
            raise Exception(f"Invalid character: {self.current_char}")
        
        return {'type': 'EOF', 'value': None}