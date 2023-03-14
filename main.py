from lexer import Lexer
from parser_1 import Parser

# Write a vintage BASIC program
input_string = """
10 PRINT "Hello, world!"
20 END
"""

# Create a lexer and a parser
lexer = Lexer(input_string)
parser = Parser(lexer)

# Parse the program
parsed_program = parser.parse()

# Output the parsed program
print(parsed_program)