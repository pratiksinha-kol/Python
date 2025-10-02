# Implement a program where user inputs grocery items
# It count how many times the items has been entered and the item


grocery_list = {}

try:
    while True:
        item = input("Item: ").strip().upper()
        if item:
            # If item is already in the dictionary, increment its count
            # Otherwise, add it to the dictionary with a count of 1
            # Using get method to simplify the code
            grocery_list[item] = grocery_list.get(item, 0) + 1
except EOFError:
    print()
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")