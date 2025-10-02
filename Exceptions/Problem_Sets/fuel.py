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
    if numerator < 0 or denominator <= 0:
        raise ValueError
    percentage = (numerator / denominator)*100
    if percentage < 0 or percentage > 100:
        raise ValueError
    return percentage
    


def main():
    while True:
        try:
            x = input("Fraction: ")
            fractions = round(fraction(x))
            if fractions >= 99:
                print("F")
            elif fractions <= 1:
                print("E") 
            else:
                print(f"{fractions}%")
            break
        except (ValueError, TypeError, ZeroDivisionError):
            pass

main()