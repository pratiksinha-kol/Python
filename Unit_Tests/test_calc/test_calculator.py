
# Using different methods to test the square function from calculator module
# Assertions provide a clear and concise way to validate expected outcomes.
# The keyword 'assert' checks if a condition is true, and raises an AssertionError if not.

from calculator import square

# Using if statements for testing (commented out)
# We end up writing more code and it's less clear than using assertions.
# def test_square():
#     if square(2) != 4:
#         print("Test failed: square(2) should be 4")
#     if square(-3) != None:
#         print("Test failed: square(-3) should be None")
#     if square(0) != 0:
#         print("Test failed: square(0) should be 0")
#     if square(1.5) != 2.25:
#         print("Test failed: square(1.5) should be 2.25")
#     if square(-1.5) != None:
#         print("Test failed: square(-1.5) should be None")

# Using assertions for testing
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-3) == 9
#     assert square(0) == 0
#     assert square(1.5) == 2.25
#     assert square(-1.5) == 2.25


# Using try-except to catch assertion errors
# This way we can report if any test fails without stopping the entire test suite.
# Also provides more specific feedback.
# This is lots of code for simple tests
def test_square():
    try:
        assert square(2) == 4
        assert square(3) == 9
        assert square(-3) == 9
        assert square(0) == 0
        assert square(1.5) == 2.25
        assert square(-1.5) == 2.25
        print("All tests passed!")
    except AssertionError:
        print("An assertion exception is raised")


def main():
    test_square()

if __name__ == "__main__":
    main()