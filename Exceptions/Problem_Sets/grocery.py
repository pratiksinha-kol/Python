# Implement a program where user inputs grocery items
# It count how many times the items has been entered and the item


count = 0
try:
    while True:
        item = input("Item: ").strip()
        for i in item:
            item = item.upper()
            count += item.count(item)
            print(f"{count} {item}")        
except EOFError:
            print()