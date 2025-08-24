
##############################################################################################################
#
# This is a Python program that demonstrates string manipulation techniques.
#
###############################################################################################################


#Enter your name and print a welcome message
firstname = input ("Enter your first name: ")
secondname = input ("Enter your second name: ")
print (f"Hello, {firstname} {secondname}, " "Welcome to Python programming!")
print (f"Hello, {firstname} {secondname}")

# This is another way of using print function
# Notice the use of + operator to concatenate strings
print ("Hellooo, " +firstname + " " + secondname) 



"""Remove whitespace from the input strings using the strip() method"""
name_to_try = input("Enter your name with lots of spaces: ")
name_to_try = name_to_try.strip()  # Remove leading and trailing whitespace
print(f"Hello, {name_to_try}, see all the whitespaces are GONE!!")

"""We are going to Capitalize the string using the capitalize() method"""
name_to_try = name_to_try.capitalize()  # Capitalize the first letter of the string
print(f"Hello, {name_to_try}, see the first character is now capitalized!!")

"""We are going to Capitalize the name using the title() method"""
name_to_try = name_to_try.title()  # Capitalize the first letter of the string
print(f"Hello, {name_to_try}, see the NAME is now capitalized!!")

"""We are going to use the strip() method to remove whitespace and title() method to capitalize the name"""

name_with_lots_of_spaces = input("Enter another name with lots of spaces: ").strip().title()
#name_with_lots_of_spaces = name_with_lots_of_spaces.strip().title()
print(f"Welcome to the world of Python, {name_with_lots_of_spaces}")


"""We are going to use the split() method to split the string into a list of words"""

full_name = input("Enter your full name: ")
name_parts = full_name.split()  # Split the string into a list of words
print(f"Your first name is: {name_parts[0]}")
print(f"Your middle name is: {name_parts[1]}")  # Get the middle name from the list
print(f"Your last name is: {name_parts[-1]}")  # Get the last name from the list
print(f"Your full name is: {name_parts}")  # Convert the list to a string for display
print(f"Your full name is: {' '.join(name_parts)}")  # Join the list back into a string with spaces

#Another way to split the string into a list of words (Only if you know there are exactly two names)
two_name = input("Enter your full name (e.g., John Doe):")
first, last = two_name.split(" ")
print(f"Your first name is: {first}")
print(f"Your last name is: {last}")  



three_name = input("Enter your full name (e.g., Sachin Ramesh Tendulkar):")
first, second, last = three_name.split(" ")
print(f"Your first name is: {first}")
print(f"Your second name is: {second}")
print(f"Your last name is: {last}")  
