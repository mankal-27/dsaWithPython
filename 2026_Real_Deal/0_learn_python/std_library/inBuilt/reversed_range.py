"""
Built-ins covered here: reversed() and range()

Key idea: both return LAZY objects (they don't build a list right away).
Wrap them in list() when you want to see or store the actual values.
"""

# ---------------------------------------------------------------------------
# 1. reversed(sequence)
#    Returns an ITERATOR that walks the sequence from the last item to the first.
#    It does NOT modify the original and does NOT return a list.
# ---------------------------------------------------------------------------
numbers = [1, 3, 4, 5, 6]

backwards = reversed(numbers)
print(backwards)
# Output: <list_reverseiterator object at 0x...>
# Printing it shows the iterator object, not the values.

print(list(reversed(numbers)))
# Output: [6, 5, 4, 3, 1]   <- convert to a list to see the values

print(numbers)
# Output: [1, 3, 4, 5, 6]   <- original list is unchanged

# Typical use: loop over items from the end
for n in reversed(numbers):
    print(n, end=" ")
print()
# Output: 6 5 4 3 1

# Note: an iterator can only be used ONCE. After it is consumed, it is empty.
backwards = reversed(numbers)
print(list(backwards))  # Output: [6, 5, 4, 3, 1]
print(list(backwards))  # Output: []  (already used up)

# ---------------------------------------------------------------------------
# 2. range(stop)
#    Numbers from 0 up to, but NOT including, stop.
# ---------------------------------------------------------------------------
print(list(range(5)))
# Output: [0, 1, 2, 3, 4]

# ---------------------------------------------------------------------------
# 3. range(start, stop)
#    Numbers from start up to, but NOT including, stop.
# ---------------------------------------------------------------------------
print(list(range(2, 5)))
# Output: [2, 3, 4]

# ---------------------------------------------------------------------------
# 4. range(start, stop, step)
#    Same as above, but jump by `step` each time.
# ---------------------------------------------------------------------------
print(list(range(1, 15, 2)))
# Output: [1, 3, 5, 7, 9, 11, 13]   (odd numbers below 15)

# A negative step counts downwards (start must be bigger than stop)
print(list(range(10, 0, -3)))
# Output: [10, 7, 4, 1]

# ---------------------------------------------------------------------------
# 5. Combining them: reverse a range
# ---------------------------------------------------------------------------
print(list(reversed(range(5))))
# Output: [4, 3, 2, 1, 0]

# Equivalent, using a negative step:
print(list(range(4, -1, -1)))
# Output: [4, 3, 2, 1, 0]

# ---------------------------------------------------------------------------
# Quick reference
# ---------------------------------------------------------------------------
# reversed(seq)            -> iterator over seq, last to first
# range(stop)              -> 0 .. stop-1
# range(start, stop)       -> start .. stop-1
# range(start, stop, step) -> start, start+step, ... (stop excluded)
