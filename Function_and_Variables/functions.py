##############################################################################
#
#                   Functions in Python
#
##############################################################################

def main():
    name = input("Enter your name: ")
    hello(name)


def hello(to="unknown user"):
    # print(f"Welcome to the world of Python! {name}")
    print(f"Greetings from Function, {to}!")
    print("Function testing name:", to)


main()

# hello()  # Call the function with default argument, this will print "unknown user"
# hello("Atindra Narayan Sinha")  # Call the function with a specific name

