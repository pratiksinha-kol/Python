
import re

name = input("Enter your name: ".strip())

# We stored the result of re.search in a variable 'match' to avoid calling it multiple times
# The regex pattern '^(.+), (.+)$' captures two groups: the last name before the comma and the first name after the comma
# If a match is found, we use match.groups() to extract the captured groups

# match = re.search(r"^(.+), (.+)$", name)
# if match:
#     last, first = match.groups()
#     name = f"{first} {last}"


# Trying to be more specific with group indices
# Is the same as above code

# match = re.search(r"^(.+), (.+)$", name)

# Using '? ' after the space to make it optional (to handle cases where there might not be a space after the comma)
# Using '*' to allow for zero or more spaces after the comma
match = re.search(r"^(.+), ?(.+)$", name)
if match:
    last = match.groups(1)
    first = match.groups(2)
    name = f"{first} {last}"

    # Alternatively, we can use match.group(1) and match.group(2) to get the same result
    name = f"{match.group(2)} {match.group(1)}"

print("Formatted Name:", name)