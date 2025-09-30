# Exception handling in python using pass


def getint():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass  # We are using pass here to ignore the exception and continue prompting the user.


def main():
    num = getint()
    print(f"Entered Number is: {num}")

main()