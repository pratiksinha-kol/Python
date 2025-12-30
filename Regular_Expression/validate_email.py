# Validate email using regular expressions
# re module is used for regex operations
# re.search(pattern, string, flags=0) scans through string looking for the first location where the regular expression pattern produces a match
# 'flags' can modify the behavior of the pattern matching (e.g., re.IGNORECASE for case-insensitive matching)

import re

email = input("Please enter your email address: ").strip()

# if re.search("@", email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")    

# 'r' before the string indicates a raw string, which treats backslashes as literal characters
# if re.search(r"^[^@]+@[^@]+\.com$", email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# Improved regex to allow only alphanumeric characters and underscores before and after '@'
# '+@' ensures at least one character on both sides of '@'
# You can replace [a-zA-Z0-9_] with '\w' for the same effect
# if re.search(r"^\w+@[a-zA-Z0-9_]+\.com$", email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")    


# Using re.IGNORECASE flag to make the domain case-insensitive
# So, if a user enters '.COM' or '.Com', it will still be considered valid
# We also allow an optional subdomain before the main domain. See the '(\w+\.)?' part. The '?' makes the preceding group optional.
# 'if re.search(r"^^[a-z0-9_\.]+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):' This code is same as below....
# if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")        


# Final version: Validates email addresses with alphanumeric characters and underscores before and after '@', allows optional subdomain, and is case-insensitive for the domain part.
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid email address.")
else:
    print("Invalid email address.")    