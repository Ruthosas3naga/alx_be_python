monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
Monthly_Savings = total_monthly_expenses - monthly_income
print("Your monthly savings are", "$",Monthly_Savings,".")
Projected_Savings = (Monthly_Savings * 12 * 0.05)
print("Projected savings after one year,", "with interest,", "is:", "$", Projected_Savings, ".")

