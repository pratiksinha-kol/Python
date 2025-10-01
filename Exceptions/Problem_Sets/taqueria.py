# Implement a program that repeatedly prompts the user for a menu item
# and keeps a running total of the cost of all items entered.
# Use a dictionary to store the menu items and their prices

# For each entered item, check if it exists in the menu dictionary
# If it does, show price formatted to two decimal places
# Continue until input is interrupted using Ctrl-D
# Print total price of the all the entered item

dict_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.0

try:
    while True:
        item = input("Item: ").title().strip()
        if item in dict_menu:
            total += dict_menu[item]
            print(f"${total:.2f}")
except EOFError:
    print()
