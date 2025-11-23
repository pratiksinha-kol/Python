
from hello_program import hello

def test_hello():
    for name in ["Bob", "Charlie", "Pratik"]:
        assert hello(name) == f"Hello, {name}"
        # assert hello(name) == f"Hello, {name}", f"Test failed for input '{name}'"
    
    # if hello("Alice") != "Hello, Alice":
    #     raise AssertionError("Test failed for input 'Alice'")

def test_hello_default():
    assert hello() == "Hello, World"