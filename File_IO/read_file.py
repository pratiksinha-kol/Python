# Now, let's read the content of names.py file and print it

# This is a conventional way of reading a file, but it requires us to manually close the file. 
# print("\nReading content of names.py file:\n")
# code = open("stored_names.txt","r")
# file_content = code.read()
# print(file_content)
# code.close()

# We can improve the above code using 'with' statement
# The 'with' statement automatically handles closing the file after its suite finishes, even if an exception is raised.

# print("\nReading content of 'stored_names.txt' file using 'with' statement:\n")
# with open("stored_names.txt","r") as file:
#     # read() reads the entire file content
#     # file_content = file.read()
#     # readlines() reads all the lines and returns them as a list
#     lines = file.readlines()
#     print(lines)


# We will be using loops to read file line by line

# print("\nReading content of 'stored_names.txt' using loop:\n")
# for line in lines:
#     # print("Hello, " + line)
#     print(line.strip())  # strip() removes leading/trailing whitespace including newlines


# Improved version of the above code by iterating directly over the file object

print("\nImproved reading content of 'stored_names.txt' without using loop:\n")

with open("stored_names.txt","r") as file:
    for text in file:
        print(text.strip())
        print(text.rstrip())

# The rstrip() method is used to remove any trailing whitespace characters, including newlines, from the end of each line before printing.
# strip() removes both leading and trailing whitespace characters.        