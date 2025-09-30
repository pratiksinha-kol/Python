# Calculating fuel percentage with exception handling
# This code prompts the user to enter a fraction (e.g., "3/4")
# and calculates the percentage. It handles various exceptions that may arise from invalid input.   
# It uses a while True loop to repeatedly prompt the user until valid input is received.
# The function fraction() splits the input string, converts the parts to integers,
# and calculates the percentage. The main() function handles user input and exceptions. 
# If an exception occurs, it simply passes and prompts the user again.

def fraction(prompt):
    numerator, denominator = prompt.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    return (numerator / denominator)*100


def main():
    while True:
        try:
            x = input("Fraction: ")
            fractions = round(fraction(x))
            print(f"{fractions}%")
            break
        except (ValueError, TypeError, ZeroDivisionError):
            pass

main()