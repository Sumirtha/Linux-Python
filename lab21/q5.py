def calculate(n1, n2, operation):
    try:
        if operation == 'add':
            result = n1 + n2
        elif operation == 'subtract':
            result = n1 - n2
        elif operation == 'multiplication':
            result = n1 * n2
        elif operation == 'division':
            result = n1 / n2
        else:
            raise ValueError("Invalid arithmetic operation")
        print("Result:", result)
    except ValueError as ve:
        print("ValueError:", ve)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Operation complete.")

calculate(10, 5, 'add')
calculate(10, 0, 'division')
calculate(10, 5, 'modulus')