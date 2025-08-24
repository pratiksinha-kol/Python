

def test_even(num):
    # return True if num % 2 == 0 else False
    return num % 2 == 0  # More concise way without ternary operator

def main():
    number = int(input("Enter a number to test if it's EVEN or ODD: "))
    if test_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
main()

# The above code is a more pythonic way of writing the even-odd program using a
# ternary operator. It makes the code more concise and readable.