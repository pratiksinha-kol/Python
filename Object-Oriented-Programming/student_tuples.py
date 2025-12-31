
def main():
    student = get_student()
    if student[0] == "ANS": 
            student[1] = "KNS"
    print(f"Hello, {student[0]} FROM {student[1]}!")
    # Alternatively, we can unpack the tuple directly into variables

    # name, house = get_student()
    # print(f"Hello, {name} of {house}!")


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    # The return statement below returns both name and house as a 'tuple'
    # FYI: Tuples are immutable lists in Python (cannot be changed after creation)
    # To be more explicit, we can also write: 'return (name, house)'
    # return name, house

    # To return a list instead of a tuple, we can do the following:
    # FYI: Lists are mutable (can be changed after creation)
    return [name, house]


if __name__ == "__main__":
    main()