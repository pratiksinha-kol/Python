################################################
# Interpreter
# Write a program that prompts the user for a simple mathematical expression like 3 + 4 or 12 / 7 and prints the result.
# Assume that the user will input two numbers separated by an operator, with spaces between each number and the operator.
# Support the operators +, -, *, /, and %.
# Format the result to one decimal place.
################################################


expression = input("Expression: ")

first_number, operator, second_number = expression.split(" ")

if operator == "+":
    print(f"{float(first_number) + float(second_number):,.1f}")
elif operator == "-":
    print(f"{float(first_number) - float(second_number):,.1f}")
elif operator == "*":
    print(f"{float(first_number) * float(second_number):,.1f}")
elif operator == "/":
    print(f"{float(first_number) / float(second_number):,.1f}")
elif operator == "%":
    print(f"{float(first_number) % float(second_number):,.1f}")    
else:
    print("Invalid operator")