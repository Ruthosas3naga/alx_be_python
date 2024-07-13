def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)       
        result = x / y
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    except ValueError:
        return f"Error: Please enter numeric values only."
    