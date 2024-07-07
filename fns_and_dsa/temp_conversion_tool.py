FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
     ans = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32) 
     return ans

def convert_to_fahrenheit(celsius):
     answer = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
     return answer

def main():
    x = float(input("Enter the temperature to convert: "))
    y = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if y == "C":
        result = convert_to_fahrenheit(x)
        print(f"{x}°C is {result:.2f}°F")
    elif y == "F":
        result = convert_to_celsius(x)
        print(f"{x}°F is {result:.2f}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()