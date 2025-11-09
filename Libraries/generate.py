import random

coin = random.choice(["heads", "tails"])
print(coin)


# Alternate Approach
# Using "from" that helps in importing functions from a module. 

# This will directly import the choice function from the random module.
# In this case, we don't need to prefix choice with random.
from random import choice

statement = choice(["truth", "lie"])
print(statement)