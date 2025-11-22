
# This script imports the custom library and calls the hello and goodbye function
# We have imported only the functions we need from the custom library
# Importing sys module to handle command-line arguments
# Using sys.argv to get names from command line arguments

import sys
# from creating_custom_library import hello 
from creating_custom_library import goodbye

if len(sys.argv) == 2:
    # hello(sys.argv[1])
    goodbye(sys.argv[1])
else:
    sys.exit("Please provide a name as a command-line argument.")