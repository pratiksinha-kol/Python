# Validate email using regular expressions
# re module is used for regex operations
# re.search(pattern, string, flags=0) scans through string looking for the first location where the regular expression pattern produces a match

###############################################################################
# Regex Symbols Cheat Sheet:
###############################################################################
# . = any character except a newline
# * = 0 or more occurrences (repeatation) of the preceding element
# + = 1 or more occurrences (repeatation) of the preceding element
# ? = 0 or 1 occurrence (optional) of the preceding element
# ^ = beginning of a string
# $ = end of a string
# [] = a set of characters
# {} = exact number of occurrences of the preceding element
# {m} = exactly m occurrences of the preceding element
# {m,n} = from m to n occurrences of the preceding element
# | = either or
# () = grouping
# \ = escape special characters
# \d = any digit (0-9)
# \D = any non-digit character
# \w = any alphanumeric character (a-z, A-Z, 0-9, _)
# \W = any non-alphanumeric character
# \s = any whitespace character (space, tab, newline)
# \S = any non-whitespace character
###############################################################################


import re

email = input("Please enter your email address: ").strip()

# if re.search("@", email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")    

# 'r' before the string indicates a raw string, which treats backslashes as literal characters
if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid email address.")
else:
    print("Invalid email address.")