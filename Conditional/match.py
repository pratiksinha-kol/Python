


name = (input("Enter a name: "))

# if name == "Harry":
#     print("You belong to the house of Gryffindor")
# elif name == "Draco":
#     print("You belong to the house of Slytherin")
# elif name == "Luna":
#     print("You belong to the house of Ravenclaw")
# elif name == "Hermine":
#     print("You belong to the house of Hufflepuff")
# else:
#     print("You are not a student of Hogwarts")    

# Match case is a new feature in Python 3.10 and aboves
# It is similar to switch case in other languages
# It is used to match a variable against a set of values
# It is more readable and concise than if-elif-else ladder

# match name:
#     case "Harry":
#         print("You belong to the house of Gryffindor")
#     case "Ron":
#         print("You belong to the house of Gryffindor")
#     case "Neville":
#         print("You belong to the house of Gryffindor")        
#     case "Draco":
#         print("You belong to the house of Slytherin")
#     case "Luna":
#         print("You belong to the house of Ravenclaw")
#     case "Hermine":
#         print("You belong to the house of Hufflepuff")
#     case _:
#         print("You are not a student of Hogwarts")

# The underscore (_) is a wildcard that matches anything (line 35)
# It is used to handle the default case when none of the above cases match

# We will further improve above code using pipelines, refer to the code below

match name:
    case "Harry" | "Ron" | "Neville":
        print("You belong to the house of Gryffindor")
    case "Draco":
        print("You belong to the house of Slytherin")
    case "Luna":
        print("You belong to the house of Ravenclaw")
    case "Hermine":
        print("You belong to the house of Hufflepuff")
    case _:
        print("You are not a student of Hogwarts")