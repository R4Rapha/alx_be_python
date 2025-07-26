# File: arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Performs a basic arithmetic operation based on the input.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float: Result of the operation
    - str: Error message in case of invalid operation or division by zero
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
