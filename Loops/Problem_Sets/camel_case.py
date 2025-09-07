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