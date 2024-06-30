num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation_type = input("Choose the operation (+, -, *, /): ")
match operation_type:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case"*":
        print(num1*num2)
    case "/":
        print(num2/num1)
    case ZeroDivisionError:
        print("cannot divide by zero")
 


