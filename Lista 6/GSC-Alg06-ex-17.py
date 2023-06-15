def is_operator(char):
    operators = ['+', '-', '*', '/']
    if char in operators:
        return True
    return False

def get_precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

def infix_to_prefix(expression):
    stack = []
    prefix = []
    for char in reversed(expression):
        if char.isdigit():
            prefix.append(char)
        elif is_operator(char):
            while stack and get_precedence(char) < get_precedence(stack[-1]):
                prefix.append(stack.pop())
            stack.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()  # Descarta o parêntese direito
    while stack:
        prefix.append(stack.pop())
    return ' '.join(reversed(prefix))

def evaluate_expression(expression):
    stack = []
    tokens = expression.split()
    for token in reversed(tokens):
        if token.isdigit():
            stack.append(int(token))
        elif is_operator(token):
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)
    return stack[0]

def main():
    infix_expression = input("Digite a expressão matemática em formato infixo: ")
    prefix_expression = infix_to_prefix(infix_expression)
    result = evaluate_expression(prefix_expression)
    print("Resultado:", result)

main()