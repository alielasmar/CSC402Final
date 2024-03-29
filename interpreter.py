from lexer import Lexer
from parser_1 import Parser
import ast
import my_ast
from typing import Union
from typing import Dict
from typing import Any
from typing import Iterable

class FunctionNotFoundError(Exception):
    pass

class Error(Exception):
    def __init__(self, message):
        self.message = message

class LexerError(Exception):
    def __init__(self, message):
        self.message = message

class ParserError(Exception):
    def __init__(self, message):
        self.message = message
        
class InterpreterError (Exception):
    def __init__(self, message):
        self.message = message

class ReturnValue:
    def __init__(self, value):
        self.value = value

class Environment:
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}

    def get(self, var_name):
        if var_name in self.variables:
            return self.variables[var_name]
        elif self.parent:
            return self.parent.get(var_name)
        else:
            raise InterpreterError(f"Undefined variable '{var_name}'")

    def set(self, var_name, value):
        self.variables[var_name] = value

    def define(self, var_name, value):
        if var_name in self.variables:
            raise InterpreterError(f"Variable '{var_name}' is already defined")
        else:
            self.variables[var_name] = value

    def copy(self):
        return Environment(parent=self)

class Interpreter:
    def __init__(self, lexer, parser, program):
        self.program = program
        self.lexer = lexer
        self.parser = parser
        self.symbols = {}
        self.functions = {}
        self.current_token = None
        self.peek_token = None
        self.advance()  # set up the current_token and peek_token
    ''' not working yet:'''
    
    def advance(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.get_next_token()
        
    def error(self, message):
        raise Exception(f"Error: {message}")

    def eat(self, token_type):
        if self.current_token.kind == token_type:
            pass
            #self.advance()
        else:
            self.error(f"Expected {token_type}, but got {self.current_token.kind}")

    def execute(self, statement):
        if isinstance(statement, my_ast.PrintStatement):
            value = self.evaluate_ast(statement.expression)
            print(value)
        elif isinstance(statement, my_ast.Assignment):
            var_name = statement.token.value
            var_value = self.evaluate_ast(statement.right)
            self.environment[var_name] = var_value
        # add more elif clauses to handle other types of statements
        else:
            raise InterpreterError(f"Invalid statement: {statement}")
        
    def factor(self):
        ...
        
    def term(self):
        ...
        
    def arithmetic_expr(self):
        ...
        
    def comparison_expr(self):
        ...
        
    def boolean_expr(self):
        ...
        
    def expr(self):
        ...
        
    def assignment_statement(self):
        ...
        
    def input_statement(self):
        ...
        
    def print_statement(self):
        ...
        
    def statement(self):
        ...
        
    def block(self):
        ...
        
    def function_definition(self):
        ...
    
    def run_prompt(self):
        while True:
            try:
                text = input('basic> ')
            except EOFError:
                break
            if not text:
                continue
            try:
                tokens = self.lexer.tokenize(text)
                ast = self.parser.parse(tokens)
                self.run_ast(ast)
            except (LexerError, ParserError, InterpreterError) as e:
                print(e)
        
    def run_file(self, file_name):
        with open(file_name, 'r') as f:
            program_text = f.read()
            self.parse(program_text)
            self.run()

    def parse(self, program_text):
        # Create the lexer and parser
        lexer = Lexer(program_text)
        parser = Parser(lexer)

        # Parse the program and build the AST
        self.program = parser.parse_program()
        if len(parser.errors) > 0:
            print("Parsing failed:")
            for error in parser.errors:
                print(error)
            return

        # Bind function names to function objects
        for function in self.program.functions.values():
            function_body = function.body
            function_name = function.name.value
            self.symbol_table[function_name] = function_body

    def run(self):
        if not self.program:
            print("No program to run")
            return

        # Execute each statement in the program
        for statement in self.program:
            result = self.execute(statement)
            if isinstance(result, ReturnValue):
                return result.value
            elif isinstance(result, Error):
                return result.message
    '''
    def run_basic_program(self, input_string):
        # Create the lexer and parser
        lexer = Lexer(input_string)
        parser = Parser(lexer)

        # Parse the program
        program = parser.parse()

        # Evaluate the program
        global_vars = {}
        local_vars = {}
        program.eval(global_vars, local_vars)
        '''
    def run_basic_program(self, program: str) -> None:
        token_stream = self.lexer.lex(program)
        ast = self.parser.parse(token_stream)

        for statement in ast:
            self.evaluate_statement(statement)
        
        
    def print_token_stream(self):
        """
        Prints the list of tokens generated by the lexer.
        """
        for token in self.token_stream:
            print(token)
            
    def print_ast(self, ast_node, indent=0):
        """Prints the AST node in a human-readable format with indentation."""
        print(' ' * indent + str(ast_node))
        for child in ast_node.children:
            self.print_ast(child, indent + 2)
#Call with:
    #ast = self.build_ast()
    #self.print_ast(ast)

    def print_environment(self):
        for name, value in self.environment.items():
            print(name, "=", value)
    
    def evaluate_statement(self, statement):
        if isinstance(statement, my_ast.PrintStatement):
            for expr in statement.expressions:
                value = self.evaluate_expr(expr)
                print(value)
        elif isinstance(statement, my_ast.Assignment):
            variable = statement.variable.name
            value = self.evaluate_expr(statement.expression)
            self.environment[variable] = value
        elif isinstance(statement, my_ast.IfStatement):
            condition = self.evaluate_expr(statement.condition)
            if condition:
                for stmt in statement.body:
                    self.evaluate_statement(stmt)
            elif statement.else_body:
                for stmt in statement.else_body:
                    self.evaluate_statement(stmt)
        elif isinstance(statement, my_ast.WhileStatement):
            condition = self.evaluate_expr(statement.condition)
            while condition:
                for stmt in statement.body:
                    self.evaluate_statement(stmt)
                condition = self.evaluate_expr(statement.condition)
        else:
            raise InterpreterError(f"Invalid statement: {statement}")
    
    def evaluate_ast(self, node):
        if isinstance(node, ast.Number):
            return node.value
        elif isinstance(node, ast.String):
            return node.value
        elif isinstance(node, ast.Variable):
            return self.environment.get(node.name)
        elif isinstance(node, ast.Function):
            args = [self.evaluate_ast(arg) for arg in node.args]
            func = self.functions[node.name]
            return func(*args)
        elif isinstance(node, ast.BinaryOperator):
            left = self.evaluate_ast(node.left)
            right = self.evaluate_ast(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
            elif node.op == '^':
                return left ** right
            elif node.op == '<':
                return left < right
            elif node.op == '>':
                return left > right
            elif node.op == '<=':
                return left <= right
            elif node.op == '>=':
                return left >= right
            elif node.op == '==':
                return left == right
            elif node.op == '<>':
                return left != right
            else:
                raise Exception(f'Invalid operator: {node.op}')
        elif isinstance(node, ast.UnaryOperator):
            operand = self.evaluate_ast(node.operand)
            if node.op == '-':
                return -operand
            elif node.op == '+':
                return +operand
            else:
                raise Exception(f'Invalid operator: {node.op}')
        elif isinstance(node, ast.Assignment):
            value = self.evaluate_ast(node.value)
            self.environment[node.variable.name] = value
            return value
        else:
            raise Exception(f'Invalid AST node: {node}')
        
    def evaluate_unary_operator(self, op: str, right: Union[my_ast.Number, my_ast.Variable]) -> Union[int, float]:
        if op == "-":
            return -self.evaluate_ast(right)
        else:
            raise Exception(f"Invalid unary operator '{op}'")
        
    def evaluate_number(self, node, env):
        return ast.Number(node.value)
    
    def evaluate_string(self, string: str):
        lexer = Lexer(string)
        parser = Parser(lexer)
        program = parser.parse()
        return self.evaluate_ast(program)
    
    def evaluate_variable(self, node):
        variable_name = node.value
        if variable_name not in self.environment:
            raise InterpreterError(f"Undefined variable '{variable_name}'")
        return self.environment[variable_name]
    
    def evaluate_assignment(self, node):
        var_name = node.token.value
        var_value = self.evaluate_ast(node.right)
        self.environment[var_name] = var_value
        return ReturnValue(None)
    
    def evaluate_function(self, node: my_ast.FunctionCall, env: Dict[str, Any]) -> Any:
        function_name = node.name
        arguments = [self.evaluate(expr, env) for expr in node.arguments]

        if function_name in self.functions:
            return self.functions[function_name](*arguments)
        else:
            raise FunctionNotFoundError(f"Function '{function_name}' not found")
        
    def evaluate_if_statement(self, node: my_ast.IfStatement) -> Union[int, float, bool, str, None]:
        condition_value = self.evaluate(node.condition)
        if condition_value:
            return self.evaluate(node.if_branch)
        elif node.else_branch is not None:
            return self.evaluate(node.else_branch)
        else:
            return None
    
    def evaluate_for_loop(self, node: my_ast.ForLoop) -> Union[None, ReturnValue]:
        iterable = self.evaluate(node.iterable)
        if not isinstance(iterable, Iterable):
            raise InterpreterError(f"'{node.iterable}' is not iterable")
        
        # Create a new scope for the loop
        self.environment.push_scope()
        
        try:
            for item in iterable:
                # Set the loop variable in the loop scope
                self.environment.add_variable(node.loop_var, item)
                
                # Evaluate the body of the loop
                result = self.evaluate(node.body)
                
                # Check for return statements in the loop body
                if isinstance(result, ReturnValue):
                    return result
        finally:
            # Pop the loop scope from the environment stack
            self.environment.pop_scope()
    
    def evaluate_print_statement(self, node: my_ast.PrintStatement, env: Dict[str, Any]) -> None:
        """Evaluate a print statement node."""
        value = self.evaluate_ast(node.expression, env)
        print(value)
        
    def evaluate_input_statement(self, node: my_ast.InputStatement) -> ReturnValue:
        user_input = input(node.message)
        if node.var_name is not None:
            self.environment[node.var_name] = float(user_input)
        return ReturnValue(None)