def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)       
        result = x / y
    except ZeroDivisionError:
        print ("Error: Cannot divide by zero.")
        if y == str:
            raise ValueError("Please enter numeric values only.")
    else:
        print (f"The result of the division is {result}")