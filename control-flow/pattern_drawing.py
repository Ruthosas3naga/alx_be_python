# Ask the user to input a positive integer for the size of the pattern
user_input = int(input("Enter the size of the pattern: "))

# Validate user input to ensure it's a positive integer
if user_input <= 0:
    print("Pattern size must be greater than zero.")
else:
    # Initialize variables
    rows = 0
    
    # Loop to print each row of the pattern
    while rows < user_input:
        # Inner loop to print asterisks in each row
        for i in range(user_input):
            print("*", end=" ")
        print()  # Move to the next line after printing each row
        rows += 1  # Increment row counter

