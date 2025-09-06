# This program takes a string and an integer input from the user
# and prints the string the specified number of times using a for loop.

text = input("Enter some text: ")
times = int(input("Enter number of times to repeat: ")) 


# We are using "_" as throwaway variable and we are not going to use it and consider it as a placeholder 
for _ in range(times):
    print(text)