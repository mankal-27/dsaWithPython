"""
Built-in helpers for working with collections:
min, max, len, count, sum, math.prod, any, all

Each section shows: what the function does, an example, and what it returns.
"""

import math

numbers = [1, 2, 3, 4]
print("numbers =", numbers)
print()

# ---------------------------------------------------------------- min()
# min(iterable) -> the smallest item
print("min(numbers)            ->", min(numbers))   # 1

# ---------------------------------------------------------------- max()
# max(iterable) -> the largest item
print("max(numbers)            ->", max(numbers))   # 4

# ---------------------------------------------------------------- len()
# len(container) -> how many items it holds
print("len(numbers)            ->", len(numbers))   # 4

# ---------------------------------------------------------------- list.count()
# list.count(x) -> how many times x appears in the list
# (this is a list method, not a standalone built-in)
print("numbers.count(1)        ->", numbers.count(1))   # 1  (1 appears once)
print("[1, 1, 2].count(1)      ->", [1, 1, 2].count(1))  # 2

# ---------------------------------------------------------------- sum()
# sum(iterable)        -> adds all items together (starts from 0)
# sum(iterable, start) -> adds all items, but starts from `start`
print("sum(numbers)            ->", sum(numbers))       # 1+2+3+4      = 10
print("sum(numbers, 10)        ->", sum(numbers, 10))   # 10+1+2+3+4   = 20

# ---------------------------------------------------------------- math.prod()
# math.prod(iterable)          -> multiplies all items (starts from 1)
# math.prod(iterable, start=n) -> multiplies all items, starting from n
# NOTE: `start` must be passed by name here, unlike sum().
# The old line `math.prod(arr1, 10)` raised a TypeError for this reason.
print("math.prod(numbers)      ->", math.prod(numbers))           # 1*2*3*4      = 24
print("math.prod(numbers, start=10) ->", math.prod(numbers, start=10))  # 10*1*2*3*4 = 240

print()

# ---------------------------------------------------------------- any() / all()
flags = [True, False, True, True, False]
print("flags =", flags)

# any(iterable) -> True if AT LEAST ONE item is truthy, else False
print("any(flags)              ->", any(flags))   # True  (some are True)

# all(iterable) -> True only if EVERY item is truthy, else False
print("all(flags)              ->", all(flags))   # False (some are False)

# Edge cases on empty input:
print("any([])                 ->", any([]))      # False (nothing is True)
print("all([])                 ->", all([]))      # True  (nothing is False)
