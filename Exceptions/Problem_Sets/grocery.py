grocery_list = {}

while True:
    try:
        item = input()
        grocery_list[item] = grocery_list.get(item, 0) + 1

    except EOFError:
        break

sorted_dict = {k: grocery_list[k] for k in sorted(grocery_list)}

for item, count in sorted_dict.items():
    print(f"{count} {item.upper()}")

