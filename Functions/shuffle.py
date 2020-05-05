# Python Program to Shuffle Deck of Cards

import random
import itertools

deck = list(itertools.product(range(1, 14), [
            'Spade', 'Heart', 'Diamond', 'Club']))

random.shuffle(deck)

for i in range(5):
    print(deck[i][0], 'of', deck[i][1])
