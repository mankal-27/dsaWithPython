"""
random module  (built in, no install needed)
--------------------------------------------
What it is : a toolbox for making pseudo-random numbers and picking random items.
Pseudo     : the numbers LOOK random but come from a formula. Same seed -> same numbers.
Not for    : passwords / secrets. Use the `secrets` module for that.
Variants   : random.Random() -> your own separate generator
             random.SystemRandom() -> uses the OS's real randomness (cannot be seeded)

Theme below: a tiny card game (a deck of 5 cards, roll a die, etc.).
"""
import random  # loads the module; nothing is returned/printed

# seed(n): fixes the starting point of the generator. Returns None.
# With the same seed, every run prints the same numbers (great for testing/debugging).
random.seed(42)

# random(): returns a float x where 0.0 <= x < 1.0
print(random.random())          # -> prints: 0.6394267984578837

# randint(a, b): returns a random INT from a to b, BOTH ends included (like a die roll)
print(random.randint(1, 6))     # -> prints: 1

# randrange(start, stop, step): random int from range(start, stop, step); stop is NOT included
# here: one of 0, 2, 4, 6, 8
print(random.randrange(0, 10, 2))   # -> prints: 4

# uniform(a, b): returns a random FLOAT between a and b
print(random.uniform(1, 5))     # -> prints: 1.979567415213905

cards = ["A", "K", "Q", "J", "10"]

# choice(seq): returns ONE random item from a non-empty list/tuple/string. List is unchanged.
print(random.choice(cards))     # -> prints: K

# choices(seq, k=n): returns a NEW list of n items picked WITH replacement
# (same item can appear twice). Can take weights=[...] to make some items likelier.
print(random.choices(cards, k=3))   # -> prints: ['J', 'J', '10']

# sample(seq, k): returns a NEW list of k UNIQUE items (no repeats, like dealing cards).
# Original list is unchanged.
print(random.sample(cards, 2))  # -> prints: ['A', 'J']

# shuffle(list): reorders the list IN PLACE and returns None
# (so never write `cards = random.shuffle(cards)` -> that gives None!)
random.shuffle(cards)
print(cards)                    # -> prints: ['K', 'Q', 'J', '10', 'A']

# getrandbits(k): returns a random int made of k random bits (0 to 2**k - 1)
print(random.getrandbits(4))    # -> prints: 3   (always between 0 and 15)

# getstate() / setstate(): save the generator's position, then go back to it later
state = random.getstate()       # returns a snapshot (a tuple)
a = random.random()             # draw a number
random.setstate(state)          # rewind to the snapshot; returns None
b = random.random()             # draws the SAME number again
print(a == b)                   # -> prints: True

# Typical use: random.shuffle(list) to shuffle, random.randint(a, b) for dice/indexes,
# random.sample(list, k) to pick k unique items, random.seed(n) to make tests repeatable.
