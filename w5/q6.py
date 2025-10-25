class FormulaError(Exception):
    pass

def parse_and_calculate(input_str):
    parts = input_str.split()
    if len(parts) != 3:
        raise FormulaError("Input must consist of exactly 3 elements")
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        raise FormulaError("First and third inputs must be numbers")
    if operator not in ('+', '-'):
        raise FormulaError("Operator must be '+' or '-'")
    if operator == '+':
        return num1 + num2
    return num1 - num2

while True:
    user_input = input("Enter formula (e.g., '1 + 1') or 'quit': ").strip()
    if user_input.lower() == 'quit':
        break
    try:
        result = parse_and_calculate(user_input)
        print(result)
    except FormulaError as e:
        print(f"Error: {e}")