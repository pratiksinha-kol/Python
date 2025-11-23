
# We are testing this program using unit tests
# Refer to test_hello.py for the tests

def main():
    name = input("Whats your name? ")
    # input() returns a string, so no need to convert
    # To include default behavior when no name is given, we check for empty input
    # If the input is empty or only whitespace, we call hello() with default value
    
    if name.strip() == "":
        print(hello())
    else:
        print(hello(name))

# By default hello() function doesn't return any value, just prints to console
# We modify it to return the greeting string for testing purposes
# This way, we can verify the output in our unit tests
def hello(n="World"):
    # print("Hello,", n)
    return f"Hello, {n}"

if __name__ == "__main__":
    main()