####################################
# A List in python is a collection which is ordered and changeable. Allows duplicate members.
# 
# List of students
# Iterate through the list of students and print a greeting for each student
####################################



students = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy"]

print(f"Number of new students as per given list: {len(students)}\n")

####################################
# Iterate through the list of students and print a greeting for each student without using for loop
# print(students[0])
####################################

for _ in students:
    print("Hello, " + _ + "!")
    # print("You are a student at Hogwarts School of Witchcraft and Wizardry.\n")


# Range function uses index to iterate through the list
# Since, list does not have index, we will use len() function to get the length of the list
# and use it in range() function to iterate through the list using index 
# In line 10, we are getting length of the list using len() function

for i in range(len(students)):
    # print(students[i]) # print name
    # print( i, students[i]) # print index and name
    print( i+1, students[i]) # print index+1 and name

# Redundant code below, not needed for the exercise
#
# length = len(students)
# print(length)
###############################