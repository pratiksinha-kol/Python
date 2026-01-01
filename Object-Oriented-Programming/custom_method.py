


class Student:

    def __init__(self, name, house, nickname):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Hyderabad", "Kolkata", "Patna", "Varanasi", "Shaktinagar"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.nickname = nickname

    def __str__(self):
        return f"{self.name} from the city of {self.house}"


    def spell_nickname(self):
        match self.nickname:
            case "Jagan":
                return "🦁"
            case "Miku":
                return "🐍"
            case "Chiku":
                return "🐼"
            case _:
                return "🏳️"


def main():
    student = get_student()
    print("YOUR NICKNAME SPELLS IS.....")

    # We are calling the method spell_nickname() on the student object
    print(student.spell_nickname())


def get_student():
    
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    nickname = input("Enter your nickname: ")
    return Student(name, house, nickname)
    

if __name__ == "__main__":
    main()