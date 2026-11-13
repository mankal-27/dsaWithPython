# ============================================================
# enumerate()
# ============================================================
# What it does:
#   Walks through any iterable (list, tuple, string, ...) and hands you
#   BOTH the position (index) and the value of each item.
#
# Signature:
#   enumerate(iterable, start=0)
#
# What it returns:
#   An "enumerate object" (a lazy iterator), NOT a list.
#   Each step of the iterator gives a tuple: (index, value).
#   Wrap it in list() if you want to see all the pairs at once.
# ============================================================

arr = [5, 6, 1, 3]

# ------------------------------------------------------------
# 1. What enumerate returns
# ------------------------------------------------------------
result = enumerate(arr)
print(result)
# Output: <enumerate object at 0x...>   <- a lazy iterator, not the pairs yet

# list() consumes the iterator and shows every (index, value) pair.
print(list(enumerate(arr)))
# Output: [(0, 5), (1, 6), (2, 1), (3, 3)]
#          ^ index 0 holds 5, index 1 holds 6, and so on

# ------------------------------------------------------------
# 2. Using it in a for loop (the most common use)
# ------------------------------------------------------------
# Each tuple is unpacked into two variables: `index` and `value`.
for index, value in enumerate(arr):
    print(index, value)
# Output:
# 0 5
# 1 6
# 2 1
# 3 3

# Without enumerate you would need to manage the counter yourself:
#   for i in range(len(arr)):
#       print(i, arr[i])
# enumerate is shorter and less error-prone.

# ------------------------------------------------------------
# 3. Changing the starting index with `start`
# ------------------------------------------------------------
# Handy when you want counting to begin at 1 (e.g. numbered lists).
for position, value in enumerate(arr, start=1):
    print(position, value)
# Output:
# 1 5
# 2 6
# 3 1
# 4 3

# ------------------------------------------------------------
# 4. Works on any iterable, e.g. strings
# ------------------------------------------------------------
print(list(enumerate("abc")))
# Output: [(0, 'a'), (1, 'b'), (2, 'c')]

# ------------------------------------------------------------
# 5. Note: it is a one-time iterator
# ------------------------------------------------------------
pairs = enumerate(arr)
print(list(pairs))  # [(0, 5), (1, 6), (2, 1), (3, 3)]
print(list(pairs))  # []  <- already used up, so it is now empty
