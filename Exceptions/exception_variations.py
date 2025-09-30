# Variation of Exception Handling in Python
# It uses ValueError and ZeroDivisionError as examples.

#Variation 1: Handling ValueError when converting input to integer
try:
    number = int(input("Enter a number: "))
    print(f"Number: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

#Variation 2: Handling ZeroDivisionError when performing division
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


