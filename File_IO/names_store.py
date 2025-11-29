# We will take user's name and store that list in a file.

name = input("What is your name? ")

# Open a file in write mode to store the name
# "a" is for append, "w" is for write (overwrites existing content), "r" is for read
file =  open("list of names.txt", "a")
file.write(name + "\n")
file.close()
print(f"The name of '{name}' is written to file successfully")