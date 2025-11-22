# Python Packages
# Visit pypi.org to find more packages

# In this program, we will learn how to use packages in Python
# The first example would be 'cowsay' package which is used to print text in a cow speech bubble (https://pypi.org/project/cowsay/)

#First, we need to install the package using pip
# pip is a package manager for Python packages and comes pre-installed with Python

# To install cowsay package, run the following command in your terminal or command prompt:
# pip install cowsay
# You may need to restart VS Code or your IDE after installing the package

import cowsay
import sys
# cowsay.cow("Hello, this is a cow speaking!")

# To execute this program from command line with an argument, use the following command:
# python Libraries/packages.py YourName
if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])


# To execute this program from command line with multiple arguments, use the following command:
# python Libraries/packages.py Name1 Name2 Name3
for i in sys.argv[1:]:
    cowsay.cow("Welcome, " + i)