###############################################################################
#
#                DIVISION
#
###############################################################################


div_num1 = float(input("Enter first number for division: "))
div_num2 = float(input("Enter second number for division: "))
div_num3 = round(div_num1 / div_num2,2)  # Division result

print(f"The result of dividing {div_num1} by {div_num2} is {div_num1 / div_num2}")  # Division
print(round(div_num3,2)) # Show result with rounding to two decimal places
print(f"Output of division with two decimal places {div_num3:.2f}")  # Format the number with commas and two decimal places
print(f"The result of division with three decimal places is {div_num3:,.3f}")  # Show result in float format with three decimal places
