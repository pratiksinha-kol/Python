
# You need to create a folder named Unit_Tests in the root directory of your project.
# Inside the Unit_Tests folder, create another folder named Test.
# Inside the Test folder, create a file named test_hello.py and add the following code: 
# test_hello.py

# You need to mention the correct path to import the hello function from your hello_program.py file.
# Here Unit_Test_Hello is the name of the main project folder.
# hello_program.py is the file where the hello function is defined.

from Unit_Test_Hello.hello_program import hello

def test_hello():
    for name in ["Bob", "Charlie", "Pratik"]:
        assert hello(name) == f"Hello, {name}"
        # assert hello(name) == f"Hello, {name}", f"Test failed for input '{name}'"
    
    # if hello("Alice") != "Hello, Alice":
    #     raise AssertionError("Test failed for input 'Alice'")

def test_hello_default():
    assert hello() == "Hello, World"

# To work with pytest, you need another file IN THE SAME FOLDER to test this code.
# We will create a file named __init__.py in the same folder as this file.
# Run the following command in the terminal to create the file:
# touch Unit_Tests/Test/__init__.py
# This file can be empty, but it tells Python that this folder should be treated as a package.
# With this setup, you can run pytest from the command line in the parent directory of the Unit_Tests folder.    