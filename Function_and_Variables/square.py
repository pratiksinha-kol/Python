##################################################################################
#                   Square a Number
#                   This program takes a number as input and returns its square.
#                   RETURN value
##################################################################################


def main():
    x = int(input("Enter a number to square it: "))
    y = int(input("Enter another number to square it: "))
    
    print(f"The squared value of {x} is:", square(x))
    print(f"The squared value of {y} is:", power(y))

def square(x):
    """Function to calculate the square of a number."""
    return x*x    

def power(n):
    """Function to calculate the square of a number."""
    """ x*x is equivalent to pow(x, 2) or x ** 2 """

    # You can use the pow function
    # return pow(n, 2)  # This is equivalent to n * n
    # return pow(n, 2)
    
    # Alternative way to calculate square using exponentiation
    # return n ** 2  # This is equivalent to n * n
    
    return n ** 2

main()