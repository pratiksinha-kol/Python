
# This is a custom library with functions that can be imported into other Python scripts.
# It also contains a main section that runs when the file is executed directly.

def main():
    hello("Alice")
    goodbye("Bob")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")


# The main always runs when this file is executed directly
# Applicable even when imported as a module
# To avoid this, use the following construct:
if __name__ == "__main__":
    main()

# When this file is imported as a module, the main() function
# will not run automatically. Only the functions will be available
# for use in the importing script.
# This allows for modular code reuse without executing unwanted code.

# FYI: there is two underscores before and after "name" and "main"    