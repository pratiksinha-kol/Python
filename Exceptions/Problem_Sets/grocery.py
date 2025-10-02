grocery_list = {}

while True:
    try:
        item = input()
        grocery_list[item] = grocery_list.get(item, 0) + 1

    except EOFError:
        break

# Sort the dictionary by keys (item names)
# Create a new dictionary with sorted keys
# This ensures the original dictionary remains unchanged
# Here 'k' is the key (item name) and 'grocery_list[k]' is the value (count)
sorted_dict = {k: grocery_list[k] for k in sorted(grocery_list)}

for item, count in sorted_dict.items():
    print(f"{count} {item.upper()}")

