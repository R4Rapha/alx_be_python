# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table using a for loop
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
