

def main():
    len = int(input("Enter the length of the square: "))
    print_square(len)

# This code uses a nested loop to print a square
# def print_square(size):
#     for i in range(size):          # Outer loop for rows
#         for j in range(size):      # Inner loop for columns
#             print("\U0001F9F1", end="")       # Print "#" or ASCII BRICK "\U0001F9F1" without newline
#         print()                      # Move to the next line after each row

# This code achives the same result without using a nested loop
# def print_square(size):
#     for i in range(size):          # Outer loop for rows
#         print("\U0001F9F1" * size)       # Print the entire row at once


# This code achives the same result without using a nested loop or string multiplication
def print_square(size):
    for i in range(size):          # Outer loop for rows
        print_row(size)            # Call a function to print each row  


# Abstracted function to print a row, we have called this function from the outer loop
def print_row(row_size):
    print("\U0001F9F1" * row_size)       # Print "#" or ASCII BRICK "\U0001F9F1" without newline
    

main()