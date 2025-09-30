# Handling user input with exception handling
# We have used while True loop to repeatedly prompt the user until valid input is received.
# The first version of the code is commented out below. It uses break to exit the loop.
# The second version encapsulates the logic in a function getint() and uses return to exit the loop.
# Both versions handle invalid input gracefully by catching ValueError exceptions.


# def getint():
#     while True:
#         try:
#             number = int(input("Enter a number: "))
#         except ValueError:
#             print("Error: Invalid input. Please enter a valid integer.")    
#         else:  
#             return number 
#             # break # Instead of using "break", we can return the value directly


# We have refined the code by encapsulating the logic in a function getint().
# This function will keep prompting the user until a valid integer is entered,
# the return statement exits the loop and provides the valid integer.
def getint():
    while True:
        try:
            return int(input("Enter a number: "))
            # number = int(input("Enter a number: "))
            # return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def main():
    num = getint()
    print(f"Entered Number is: {num}")

main()