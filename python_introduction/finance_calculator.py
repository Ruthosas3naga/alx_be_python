monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_Savings = float(total_monthly_expenses - monthly_income)
print("Your monthly savings are", "$",monthly_Savings,".")
projected_Savings = (monthly_Savings * 12 * 0.05)
print("Projected savings after one year,", "with interest,", "is:", "$", projected_Savings, ".")

