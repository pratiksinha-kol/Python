##############################################################################
#
#                   FLOAT NUMBERS
#
##############################################################################


"""Show result in float format, use the code below:"""

# print(f"The sum of {num1} and {num2} as FLOAT is {float(num1) + float(num2)}") # Show result in float format

number1 = float(input("Enter first FLOAT number: "))
number2 = float(input("Enter second FLOAT number: "))
number3 = round(number1 + number2, 3)  # Round the result to 2 decimal places
print(f"The sum of {number1} and {number2} as FLOAT is {number1 + number2}")  # Show result in float format
print(number1 + number2)  # Show result in float format without any text
print(number3)
print(round(number3)) # Round the result to the nearest integer

print(f"Output of the number with commas as thousands separators {number3:,}") # Format the number with commas as thousands separators
print(f"Output of the number with commas and two decimal places: {number3:,.2f}")  # Format the number with commas and two decimal places
print(f"Output of the number with commas and three decimal places: {number3:,.3f}")  # Format the number with commas and three decimal places