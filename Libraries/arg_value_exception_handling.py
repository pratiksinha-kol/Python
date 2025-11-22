
# Example of handling command line argument exceptions in Python
# We will handle the case where no command line argument is provided

import sys

# Handling IndexError using try-except block
# try:
#     print ("Hello, my name is", sys.argv[1])
# except IndexError:
#     print ("Enter arguments on the command line")    

# Another way to handle the exception using len() function and if-else statement
if len(sys.argv) < 2:
    print ("Too few arguments on the command line")
elif len(sys.argv) > 2:
    print ("Too many arguments on the command line")
else:
    print ("Hello, my name is", sys.argv[1])  

# If a user wishes to enter his full name with spaces, they can enclose the name in quotes
# For example: python arg_value_exception_handling.py "John Doe"    