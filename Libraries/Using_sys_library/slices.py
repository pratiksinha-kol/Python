# Using sys library to handle command line arguments excluding the script name
# We will use slicing to skip the first argument which is the script name

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# In the following line, we slice sys.argv to start from index 1, but not index 0
# After the colon, we leave it empty to include all remaining elements
# This way, we avoid printing the script name and only print the actual arguments
for i in (sys.argv[1:]):
    print("My name is", i)