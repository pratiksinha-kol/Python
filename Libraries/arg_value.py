# Import sys module for system-specific parameters and functions
# Specifically, we wil use argv to handle command-line arguments

import sys

# Print a greeting message using the first command-line argument as the name
# If no argument is provided, it will raise an IndexError
# For example, if the script is run as `python script.py Alice`,
# then sys.argv[1] will be "Alice".
# To execute the script with an argument, use:
# 'python arg_value.py YourName'
print ("Hello, my name is", sys.argv[1])

# The reason we use sys.argv[1] is that sys.argv[0] is the name of the script itself,
# and sys.argv[1] is the first argument passed to the script when it is executed.
# Execute the script without any arguments to see the default behavior
# 'python arg_value.py'
print("Default file name is:", sys.argv[0])