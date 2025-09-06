###############################
# Validating Input
# Use a for loop to print "Valid input" n times, where n is a positive integer provided by the user.
# If the user enters a non-positive integer, prompt them to enter a valid positive integer until they do so.
###############################


def get_number():
    while True:
        n = int(input("Enter a number greater than 0: "))
        if n>0:
            return n
            # You can also use return n here and remove the break statement below
            # break 
        else:   
            print("Invalid input, try again")
    # return n



def call(n):

    for _ in range(n):
        print("Valid input", _+1) # _+1 to start count from 1 instead of 0
        print("Input value is:", _) # print the input value from 0 to n-1


def main():
    number = get_number()
    call(number)


main()