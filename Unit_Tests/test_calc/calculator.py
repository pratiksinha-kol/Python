# A simple calculator module to compute the square of a number
# We will use this to test Unit Tests
# Unit tests in Python test the functionality of this module or function
# The function in question is 'square' which computes the square of a number

def main():
    # We have used float type for more generality
    # You can change it to int if you want to restrict to integers only
    x = float(input("Enter a number (x): "))
    print(f"{x} squared is:", square(x))

# To fail the test, use 'n * n + 1' or any incorrect formula instead of 'n * n'
# Refer to refined_test_calculator.py for the improved version of unit tests
def square(n):
    if n < 0 or n > 0:
        # return n * n +1
        return n * n
    elif n == 0:
        return 0
    

if __name__ == "__main__":
    main()