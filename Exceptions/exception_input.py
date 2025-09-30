
def getint():
    while True:
        try:
            number = int(input("Enter a number: "))
            # print(f"Number: {number}")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")    
        else:   
            break
    print(f"Number is: {number}")

    