import random

cards = ['Diamond', 'Spade', 'Heart', 'Club']

# It returns None as shuffle method doesn't return any value
# random_card = random.shuffle(cards)
# print(random_card)

# It shuffles the original list and returns List in random order
random.shuffle(cards)
print(cards) # It prints the shuffled list

for card in cards:
    print(card)


# Alternate Approach
# Using "from" that helps in importing functions from a module. 
# This will directly import the shuffle function from the random module.
# In this case, we don't need to prefix shuffle with random.
from random import shuffle  

more_cards = ['Ace', 'King', 'Queen', 'Jack']
shuffle(more_cards)
print(more_cards)