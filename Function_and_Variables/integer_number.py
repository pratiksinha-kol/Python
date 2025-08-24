##############################################################################
#
#                   INTEGER NUMBERS
#
##############################################################################

"""Enter two numbers and print their sum"""
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

"""Show result in integer format, use the code below:"""

print(f"The sum of {num1} and {num2} as INTEGER is {int(num1) + int(num2)}")

int_num1 = int(input("Enter first INTEGER number: "))
int_num2 = int(input("Enter second INTEGER number: "))

print(f"The sum of {int_num1} and {int_num2} as INTEGER is {int_num1 + int_num2}")
print(int_num1 + int_num2)  # Show result in integer format without any text

print(f"Output of the number with commas as thousands separators {int_num1 + int_num2:,}")  # Format the number with commas as thousands separators