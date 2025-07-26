def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation based on the input.

    Parameters:
    - num1: The first number (float expected)
    - num2: The second number (float expected)
    - operation: One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - Result of the operation or an error message as a string
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Unsupported operation"
