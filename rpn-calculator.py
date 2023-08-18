OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

def solve(eqn):
    stack = []
    for element in eqn:
        try:
            element = int(element)
        except: 
            operator = OPERATORS[element]
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = operator(operand1, operand2)
            stack.append(result)
            continue
        stack.append(element)
    return stack.pop()

if __name__ == "__main__":
    import sys
    eqn = sys.argv[1:]
    print(solve(eqn))