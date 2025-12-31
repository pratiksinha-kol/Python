
# Create a Student class
# Class is a blueprint for creating objects
# Objects are instances of classes
# Attributes are characteristics of an object
# Methods are functions that belong to a class


class Student:
    # __init_ is a special method that is called when an object is created
    # It is used to initialize the attributes of the object
    # self is a reference to the current instance of the class
    # self is used to access variables that belong to the class
    # FYI: def __init__(self, name, house=None): can also be used to set a default value for house
    # If no value is provided, house will be set to None
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Hyderabad", "Kolkata", "Patna", "Varanasi", "Shaktinagar"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"Hello, {student.name} from {student.house}!")


def get_student():
    # # Create a new Student object
    # # Add attributes to the object using dot notation
    # student = Student()
    # student.name = input("Enter your name: ")
    # student.house = input("Enter your house: ")
    # return student

    # We can also do it this way (same as above but more concise):
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    # Here we are calling the function Student to create a new object
    # We get this function for free even though we didn't define it
    # It is called the constructor
    # We are also passing parameters to the constructor to set attributes
    
    # We can also handle exceptions if name is missing
    # This will prevent the program from crashing
    # Refer to line 15 for the exception raised
    try:
        return Student(name, house)
    except ValueError as e:
        print(e)
    


if __name__ == "__main__":
    main()