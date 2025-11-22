# Using sys library to handle command line arguments excluding the script name
# We will use slicing to skip the first argument which is the script name

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# In the following line, we slice sys.argv to start from index 1, but not index 0
# After the colon (argv[1:]), we leave it empty to include all remaining elements
# This way, we avoid printing the script name and only print the actual arguments
for i in (sys.argv[1:]):
    print("My name is", i)

# Using the '-1' index to exclude the last argument as well
# In the following line, we slice sys.argv to start from index 1 and go up to but not including the last element
# This way, we avoid printing both the script name and the last argument
for i in (sys.argv[1:-1]):
    print("My modified name is", i)    