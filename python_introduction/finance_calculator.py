monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_Savings = total_monthly_expenses - monthly_income

projected_Savings = monthly_Savings * 12 * 0.05
print(f"Your monthly savings are ${monthly_Savings}.")
print(f"Projected savings after one year, with interest is: ${projected_Savings}.")

