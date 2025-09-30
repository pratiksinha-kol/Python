# Variation of Exception Handling in Python
# It uses else clause in exception handling.
# NameError will occur if ValueError is raised.


try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")    

# This line will lead to NameError if ValueError occurs
# If user enters "cat" instead of a number, then the following line will throw NameError.
# print(f"Number: {number}") // Remove '#' to see the error
# Using 'else' to avoid that

else:   
    print(f"Number: {number}")    