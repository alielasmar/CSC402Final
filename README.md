# CSC402Proj

Functions needed for interpreter.py:

run_file(file_path, env): Takes the path to a BASIC file and an environment object, reads the file, and executes the contents of the file in the environment.

run_prompt(env): Starts an interactive prompt that allows the user to enter BASIC commands one line at a time. The prompt will continue to run until the user enters the QUIT command.

run_basic_program(program_text, env): Compiles and executes the BASIC program given as a string using the provided environment.

print_token_stream(tokens): Helper function that prints the token stream for a given input.

print_ast(node, level=0): Helper function that prints the abstract syntax tree for a given input.

print_environment(env): Helper function that prints the variables and their values in the given environment.

evaluate_ast(node, env): Takes an abstract syntax tree node and an environment, evaluates the node, and returns the result.

evaluate_binary_operator(operator_node, env): Takes a binary operator node and an environment, evaluates the left and right operands, and applies the operator.


evaluate_unary_operator(operator_node, env): Takes a unary operator node and an environment, evaluates the operand, and applies the operator.

evaluate_number(node): Takes a number node, converts it to a Python float, and returns the result.

evaluate_string(node): Takes a string node, strips the quotes, and returns the result.

THESE TO GO:

evaluate_variable(node, env): Takes a variable node and an environment, looks up the value of the variable in the environment, and returns the result.

evaluate_assignment(node, env): Takes an assignment node and an environment, evaluates the expression on the right-hand side of the assignment, and assigns the value to the variable on the left-hand side.

evaluate_function(node, env): Takes a function call node and an environment, evaluates the arguments to the function call, looks up the function in the environment, and applies the function to the arguments.

evaluate_if_statement(node, env): Takes an if statement node and an environment, evaluates the condition, and executes the appropriate branch based on the result.

evaluate_for_loop(node, env): Takes a for loop node and an environment, evaluates the initial value, final value, and step value, and executes the loop body.

evaluate_print_statement(node, env): Takes a print statement node and an environment, evaluates the arguments to the print statement, and prints the results.

evaluate_input_statement(node, env): Takes an input statement node and an environment, prompts the user for input, evaluates the expression, and assigns the input value to the variable on the left-hand side of the assignment.