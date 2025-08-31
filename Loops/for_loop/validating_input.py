##############################
# Validating Input
# Use a for loop to print "Valid input" n times, where n is a positive integer provided by the user.
# If the user enters a non-positive integer, prompt them to enter a valid positive integer until they do so.
##############################



while True:
    n = int(input("Enter a number: "))
    if n>0:
        break
    else:
        print("Invalid input, try again")

for _ in range(n):
    print("Valid input")