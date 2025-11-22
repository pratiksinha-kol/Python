# Use sys.exit() to exit from Python scripts when exceptions occur
# We will handle the case where too few or too many command line arguments are provided
# If the number of arguments is incorrect, we will exit the program with an error message

# Refer to arg_value_exception_handling.py and arg_value.py for context on handling command line arguments

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments on the command line")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments on the command line")

print ("Hello, my name is", sys.argv[1]) 