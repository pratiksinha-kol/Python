##########################################
# Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, can hold multiple values.
# A Dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
##########################################

students = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Creating a dictionary using two lists
# Using dictionary comprehension
# 
student_dict = {students[i]: houses[i] for i in range(len(students))}
print(student_dict)


# Manually creating a dictionary
player_dict_manual = {
    "Wayne Rooney": "Manchester United",
    "Lionel Messi": "Barcelona",
    "Paolo Maldini": "AC Milan",
    "Diego Maradona": "Napoli"
}
print(f"The manual dictionary is as follows: {player_dict_manual}\n")
print(player_dict_manual["Paolo Maldini"]) # Accessing value using key

# Using loop to get values from dictionary
for player in player_dict_manual:
    # print(player) # This will print all the keys in the dictionary
    # print(player_dict_manual[player]) # This will print all the values in the dictionary
    print (player, player_dict_manual[player], sep=", ") # This will print both key and value



first_name = ["Pratik", "Atindra", "Rohit", "Sourav", "Virat"]
last_name = ["Sinha", "Sarkar", "Sharma", "Ganguly", "Kohli", "Dhoni"]

# Using zip function to combine two lists into a dictionary
# zip() function returns an iterator of tuples based on the iterable objects.
# We can convert the iterator of tuples into a dictionary using dict() function
# Here, first_name list will be the keys and last_name list will be the values
# If the lists are of unequal length, zip() will stop creating pairs when the shortest list is exhausted.
# In this case, last_name list has 6 elements while first_name list has 5 elements
fullname_dict_zip = dict(zip(first_name, last_name))
print(f"The dictionary created using zip function WITH UNEQUAL LENGTH: {fullname_dict_zip}")
