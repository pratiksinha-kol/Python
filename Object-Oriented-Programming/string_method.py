
# Object-Oriented Programming: String Representation of Objects

# We define a new function __str__ in our class 'Student' to provide a user-friendly string representation of the object.

class Student:

    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Hyderabad", "Kolkata", "Patna", "Varanasi", "Shaktinagar"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    # Only takes one argument: self
    # This method is called when you use the print function on an object
    # Refer to line 33 in main() when we have called 'print(student)'
    def __str__(self):

        # You can customize the string representation as needed
        # return "A student object"

        # This return is more specific
        return f"{self.name} from the city of {self.house}"

def main():
    student = get_student()
    
    # This will give you the object location
    # print(student) prints something like <__main__.Student object at 0x7f9b8c2d1d30>
    # The hexadecimal number represents the memory address where the object is stored.
    print(student)

    # To get a more readable representation, we need to define a __str__ method in the class
    # After defining __str__, printing the object will give a user-friendly string
    # For example: print(student) might output "Harry from Hyderabad"
    # Make sure to implement the __str__ method in the Student class for this to work.    


def get_student():
    
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()