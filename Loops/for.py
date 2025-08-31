## Using for loop to iterate over a list

list_of_names = ["Alice", "Bob", "Charlie"]

for name in list_of_names:
    # print("Hello, " + name + "!\n")
    print(f"Hello, {name}!")



## Using hardcoded list to demonstrate for loop
for i in [1, 2, 3]:
    print(i)



## Using range() function to generate a sequence of numbers

for i in range(5):
    print("Iteration:", i)


## Using user input to determine loop iterations

text = input("Enter some text you want to repeat: ")
times = int(input("Enter number of times to repeat: ")) 

for i in range(times):
    print(text)


## Using underscore (_) as a throwaway variable in for loop
## Pythonically, underscore is used when the loop variable is not needed
## Above code does the same thing as below, we have just replaced 'i' with '_':

# for _ in range(times):
#     print(text)    

