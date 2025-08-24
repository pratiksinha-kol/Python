#################################################################################################################
# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively. 
# Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.
#################################################################################################################


greeting = input("Greeting: ").strip().lower()

if greeting.startswith ("Hello") or greeting.startswith ("hello"):
    print("$0.00")
elif greeting.startswith("h") or greeting.startswith("H"):
    print("$20")
else:
    print("$100")