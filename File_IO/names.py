
names_list = []

for _ in range(3):
    # Uncomment the lines below to take input from the user and add to the list. This avoid usage of variables.
    # name = input("Enter a name: ")
    # names_list.append(name)

    # Improved version using inline input and append
    names_list.append(input("Enter a name to be added: "))
    
# We will sort the names before printing
# sorted() function returns a new sorted list from the elements of any iterable.
for name in sorted(names_list):
    names_list.sort()
    print(f"{name} is added to the list")

print("List of users in the File I/O example list.", names_list)