# The following loop converts camelCase to snake_case by iterating through each character in the input string.
# When an uppercase letter is found, it adds an underscore before it 
# (except if it's the first character) and converts it to lowercase.
# Here the for loop uses 'i' to track the index of the character in the string.
# The 'char' variable holds the current character being processed.

camelCase = input("camelCase: ")
snake_case = ""

for i, char in enumerate(camelCase):
    if char.isupper():
        if i != 0:
            snake_case += "_"
        snake_case += char.lower()
    else:
        snake_case += char

print("snake_case:", snake_case)