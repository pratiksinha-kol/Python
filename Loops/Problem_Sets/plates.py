# Plates validation
# A valid plate: String must begin with at least two letters
# A valid plate: String must contain a maximum of 6 characters (letters or numbers)
# A valid plate: Numbers, if any, must be at the end. The first number used cannot be '0'
# A valid plate: No periods, spaces, or punctuation marks are allowed
# A valid plate: Vanity plates cannot be all numbers

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            number_started = True
            if s[i] == '0' and (i == 2 or s[i-1].isalpha()):
                return False
        elif number_started and s[i].isalpha():
            return False
    return True


main()
