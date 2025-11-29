# Now, let's read the content of names.py file and print it

print("\nReading content of names.py file:\n")
code = open("names.py","r")
file_content = code.read()
print(file_content)
code.close()