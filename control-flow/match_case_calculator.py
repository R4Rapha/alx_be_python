# Ask user for the first number
num1 = float(input("Enter the first number: "))

# Ask user for the second number
num2 = float(input("Enter the second number: "))

# Ask user for the operation
operation = input("Enter the operation (+, -, *, /):")

# Perform the operation using match case
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        
        # Handle division by zero
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation selected.")
# This code implements a simple calculator using match case to handle different operations.