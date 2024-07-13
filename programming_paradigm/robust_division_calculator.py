def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)       
        result = x / y
    except ZeroDivisionError:
        print ("Error: Cannot divide by zero.")
    except ValueError:
        print ("Please enter numeric values only.")
    else:
        print (f"The result of the division is {result}")