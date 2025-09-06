#################################
# Using for loop with user input
# Take input from user and print it multiple times using for loop
#################################

name = input("Enter text you want to print multiple times: ")
times = int(input("Enter number of times you want to print: "))

# print (name * times)
# print (f"{name}\n" * times)
# # print (f"{name}\n" * times, end = "")

for _ in range(times):
    print (f"{name}\n", end = "")
    # print (f"{name}\n" * times)
    # print (f"{name}\n" * times, end = "")