# Handling user input with exception handling
# This code prompts the user to enter a number and handles invalid input gracefully.
# else and break are used to exit the loop upon valid input.

while True:
    try:
        number = int(input("Enter a number: "))
        # print(f"Number: {number}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")    
    else:   
        break

print(f"Number: {number}")