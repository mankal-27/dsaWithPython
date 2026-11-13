"""
Sorting in Python
=================
Quick guide to the built-ins used for sorting. Run the file to see the output.

    Built-in            What it does                          What it returns
    ------------------  ------------------------------------  -------------------
    sorted(x)           sorts any iterable (list, tuple,      a NEW sorted list
                        string, dict keys, ...)               (original untouched)
    list.sort()         sorts a list in place                 None (changes the list)
    abs(n)              absolute value (distance from 0)      a non-negative number
    len(x)              number of items / characters          an int

Options accepted by both sorted() and list.sort():
    reverse=True   -> largest to smallest instead of smallest to largest
    key=function   -> function is called on every item; items are ordered by
                      the value the function returns (items themselves unchanged)
"""

# ---------------------------------------------------------------------------
# 1. sorted()  ->  returns a NEW list, original stays the same
# ---------------------------------------------------------------------------
numbers = [1, 5, 4, 7, 6]
print("1) Original list:           ", numbers)

new_list = sorted(numbers)  # returns [1, 4, 5, 6, 7]
print("   sorted(numbers) returns: ", new_list)
print("   original is unchanged:   ", numbers)  # still [1, 5, 4, 7, 6]

# ---------------------------------------------------------------------------
# 2. list.sort()  ->  changes the list itself, returns None
# ---------------------------------------------------------------------------
result = numbers.sort()  # sorts `numbers` in place
print("\n2) numbers.sort() returns:  ", result)   # None  (nothing to use)
print("   but the list is now:     ", numbers)    # [1, 4, 5, 6, 7]

# Common mistake: `numbers = numbers.sort()` would set numbers to None!
# Just call numbers.sort() on its own line, then use numbers.

# ---------------------------------------------------------------------------
# 3. reverse=True  ->  descending order (largest first)
# ---------------------------------------------------------------------------
numbers.sort(reverse=True)  # in place again, still returns None
print("\n3) After sort(reverse=True):", numbers)  # [7, 6, 5, 4, 1]
print("   sorted(..., reverse=True):", sorted(numbers, reverse=True))

# ---------------------------------------------------------------------------
# 4. key=abs  ->  order by absolute value
#    abs(-5) returns 5, abs(3) returns 3, so we compare 5 vs 3, not -5 vs 3.
#    The original values (with their minus signs) are what get returned.
# ---------------------------------------------------------------------------
mixed = [-1, 3, 7, -5, 19, -12, -4]
print("\n4) Original list:           ", mixed)
print("   Normal sorted():         ", sorted(mixed))
# [-12, -5, -4, -1, 3, 7, 19]  -> by actual value
print("   sorted(key=abs):         ", sorted(mixed, key=abs))
# [-1, 3, -4, -5, 7, -12, 19]  -> by distance from zero (1, 3, 4, 5, 7, 12, 19)

# ---------------------------------------------------------------------------
# 5. key=len  ->  order by length
#    len("pie") returns 3, len("apple") returns 5, len("banana") returns 6.
# ---------------------------------------------------------------------------
words = ["apple", "pie", "banana"]
print("\n5) Original list:           ", words)
print("   sorted(key=len):         ", sorted(words, key=len))
# ['pie', 'apple', 'banana']  -> shortest first
print("   key=len, reverse=True:   ", sorted(words, key=len, reverse=True))
# ['banana', 'apple', 'pie']  -> longest first

# Note: sorting is "stable" -- if two items have the same key (e.g. two words
# of the same length), they stay in the same order they originally had.

# ---------------------------------------------------------------------------
# Cheat sheet
# ---------------------------------------------------------------------------
# * Need to keep the original list?       -> use sorted(x)
# * Fine to modify the list directly?     -> use x.sort()
# * Sort by something other than value?   -> add key=some_function
# * Biggest first?                        -> add reverse=True
# * Both sorted() and .sort() take O(n log n) time.
