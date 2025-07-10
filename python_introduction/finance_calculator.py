# Ask the user for their monthly income
monthly_income = input("Enter your monthly income: ")

# Ask the user for their total monthly expenses
monthly_expenses = input("Enter your total monthly expenses: ")

# Convert inputs to integers
monthly_income = int(monthly_income)
monthly_expenses = int(monthly_expenses)

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the monthly and projected annual savings
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)
