

def main():
    student = get_student()
    if student["name"] == "ANS":
        student["house"] = "Gryffindor"
    print(f"Hello, {student["name"]} from {student["house"]}!")


def get_student():
    # # Create an empty dictionary to hold student information
    # student = {}
    # # Set keys
    # student["name"] = input("Enter your name: ")
    # student["house"] = input("Enter your house: ")
    # # Return values as a list
    # return student

    # Another approach to make it more concise:
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()