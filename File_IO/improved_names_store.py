# We will showcase file operations using 'with' statements in Python.

name = input("Enter your name: ")

# Using 'with' to handle file operations ensures proper resource management.
# 'as file' assigns the opened file object to the variable 'file'.
# Here we didn't need to explicitly close the file.
# "a" is for append, "w" is for write (overwrites existing content), "r" is for read

with open("stored_names.txt", "a") as file:
    file.write(f"{name}\n")

# Line 11 will automatically close the file after the block is executed.    