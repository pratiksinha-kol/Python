# This script reads names from a file, sorts them, and greets each name.


# You can remove 'r' as it is the default mode for opening a file
# with open("stored_names.txt","r") as file:


# name = []

# with open("stored_names.txt") as file:
#     for line in file:
#         name.append(line.strip())

# for n in sorted(name):
#     print(f"Hi, {n}" )        
    
#--- We will further improve the above code ---#
#--- by combining reading, sorting, and greeting in fewer lines ---#    

#--- Sorting in ascending order ---#
with open("stored_names.txt") as file:
    for n in sorted(file):
        print(f"Hi, {n.strip()}" )

#--- Now, let's sort in reverse order ---#
with open("stored_names.txt") as file:
    for n in sorted(file, reverse=True):
        print(f"Hola, {n.strip()}" )