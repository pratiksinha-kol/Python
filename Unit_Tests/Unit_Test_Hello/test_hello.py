
from hello_program import hello

def test_hello():
    if hello("Alice") != "Hello, Alice":
        raise AssertionError("Test failed for input 'Alice'")

def test_hello_default():
    if hello() != "Hello, World":
        raise AssertionError("Test failed for default input")