## This is a simple while loop example that prints a message a specified number of times.
## It prompts the user for input and continues to loop until the condition is no longer met.
## The loop decrements the counter each iteration to eventually terminate.



text = input("Enter some text: ")
times = int(input("Enter number of times to repeat: "))


while times != 0:
    print(text)
    times = times - 1
    # times -= 1  # This is a shorthand for the above line

#########################################
# Another approach to the same problem using a for loop
#########################################   


# while times > 0:
#     print(text)
#     times = times - 1