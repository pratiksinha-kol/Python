

# We will use the pytest framework for unit testing
# We are a refining the version of the refined_test_calculator.py file

# Using this method, the test will run regardless if any of the tests fail
# To test it out, we have made a change in calculator.py to make the square function incorrect
# After running the tests, we will see which tests passed and which failed in the output

# We will import pytest to raise 
import pytest

from calculator import square

def test_positive_numbers():
    assert square(2) == 4
    assert square(3) == 9
    assert square(1.5) == 2.25

def test_negative_numbers():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-1.5) == 2.25

def test_zero():
    assert square(0) == 0

def test_large_numbers():
    assert square(1000) == 1000000
    assert square(-1000) == 1000000    

def test_string_input():
    with pytest.raises(TypeError):
        square("a string")