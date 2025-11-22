# Use multiple arguement values from command line

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for i in (sys.argv):
    print("My name is", i)

# The output of this program will be:
# My name is multiple_enteries.py (We want to avoid this line as it is the script name)
# My name is arg1
# My name is arg2
# My name is arg3
# We will rectify this using program "slices.py"...    