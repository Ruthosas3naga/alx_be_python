monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_Savings = int(total_monthly_expenses - monthly_income)
print("Your monthly savings are", "$",monthly_Savings,".")
projected_Savings = float(monthly_Savings * 12 * 0.05)
print("Projected savings after one year,", "with interest,", "is:", "$", projected_Savings, ".")

