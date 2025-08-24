############################################################################
#                   Area Calculation Program
#                   This program calculates the area of a rectangle and a circle.
#                   It demonstrates the use of functions and basic arithmetic operations.
##############################################################################  


def rectangle_area(length, width):
    return length * width  # Calculate the area of a rectangle

def circle_area(radius):
    import math  # Import the math module to use pi
    return math.pi * (radius ** 2)  # Calculate the area of a circle

def main():
    # Input for rectangle area
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rect_area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {rect_area:.2f}")

    # Input for circle area
    radius = float(input("Enter the radius of the circle: "))
    circ_area = circle_area(radius)
    print(f"The area of the circle is: {circ_area:.2f}")

main()  # Call the main function to execute the program    

