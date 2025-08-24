###############################################################################
#                   MODULAR OPERATOR
###############################################################################

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# Improving the above code by creating functions:
# This way, we can reuse the code and make it more modular.

def is_even(num):
    return num % 2 == 0 

def is_odd(num):
    return num % 2 != 0 

def main():
    num1 = int(input("Enter a number to test if its EVEN or ODD: "))
    if is_even(num1):
        print(f"{num1} is even")
    else:
        print(f"{num1} is odd")

main()