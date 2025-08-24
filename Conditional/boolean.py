##################################################################################
#                   EVEN ODD PROGRAM
#                   USE OF BOOLEAN  
################################################################################

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False 



def main():
    number = int(input("Enter a number to test if its EVEN or ODD: "))
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

main()