



def main():
    length = int(input("Enter the height of the tower: "))
    width = int(input("Enter the width of the tower: "))

    print_column(length)
    print_row(width)

def print_column(height):
    for _ in range(height):     # Using loop here
        print("#")  

def print_row(width):
        print("?" * width)     # Not using loop here       

main()        