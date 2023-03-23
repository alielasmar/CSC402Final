from lexer import Lexer
from parser_1 import Parser
from interpreter import Interpreter

# Load the BASIC program from the file
with open("example_program.bas") as f:
    program = f.read()

# Create instances of the lexer, parser, and interpreter
lexer = Lexer(program)
parser = Parser(lexer)
interpreter = Interpreter(lexer,parser,program)

# Run the program
interpreter.run()