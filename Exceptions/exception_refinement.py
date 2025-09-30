# Exception handling in python using pass
# Using parameterized prompt messages
# This code refines the previous example (exception_using_pass.py) by allowing a custom prompt message to be passed to the getint function.

def getint(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def main():
    num = getint("Enter a valid int number: ")
    print(f"Entered Number is: {num}")

main()