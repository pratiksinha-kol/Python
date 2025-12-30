# Regular Expression - Format Name
# Using the walrus operator to combine assignment and condition check
# walrus operator (:=) allows assignment within an expression
# Walrus operator captures the result of re.search directly in the if statement


import re

name = input("Enter your name: ".strip())

if match := re.search(r"^(.+), ?(.+)$", name):
    
    name = f"{match.group(2)} {match.group(1)}"

print("Formatted Name:", name)