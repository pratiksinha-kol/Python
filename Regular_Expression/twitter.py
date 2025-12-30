# We wil extract username from Twitter/X profile URLs


import re

URL = input("Enter Twitter/X profile URL: ").strip()

# replace() method will be used to remove the fixed parts of the URL
# replace(), takes two arguments, first is the substring to be replaced, second is the substring to replace with.

# username = URL.replace("https://x.com/", "")
# print("Username:", username)

# removeprefix() method will be used to remove the fixed parts of the URL
# removeprefix(), takes one argument, the substring to be removed from the start of the string.

# username = URL.removeprefix("https://x.com/")
# print("Username:", username)

# Using regular expression to extract username from the URL
# Using re.sub() method to remove the fixed parts of the URL
# re.sub(), takes three arguments, first is the pattern to be replaced, 
# second is the replacement string, third is the string to be processed.
# fourth optional argument is count, which specifies the maximum number of replacements to be made.
#fifth optional argument is flags, which specifies the regex flags to be used.
# re.sub(pattern, replacement, string, count=0, flags=0)

username = re.sub(r"^(https?://)?(www\.)?x\.com/", "", URL)
print("Username:", username)

