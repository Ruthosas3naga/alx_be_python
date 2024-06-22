


# Prompt the user to enter their monthly income and total monthly expenses
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - total_monthly_expenses

# Print the monthly savings
print("Your monthly savings are $", monthly_savings, ".", sep="")

# Calculate the projected savings after one year with interest
projected_savings = monthly_savings * 12 * 1.05  # Equivalent to (Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05))

# Print the projected savings after one year with interest
print("Projected savings after one year, with interest, is: $", projected_savings, ".", sep="")
