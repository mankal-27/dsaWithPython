import bisect

# bisect works on a SORTED list. It uses binary search (O(log n)) to find positions.
arr = [4, 5, 5, 6, 7, 7, 8, 10, 12, 12, 13]

# bisect_left(a, x) -> returns the index where x should be inserted
# to keep the list sorted, BEFORE any existing equal values.
# Does NOT modify the list.
print(bisect.bisect_left(arr, 5))    # 1  (first 5 is at index 1)

# bisect_right(a, x) (alias: bisect) -> returns the insertion index
# AFTER any existing equal values. Does NOT modify the list.
print(bisect.bisect_right(arr, 5))   # 3  (after the last 5)
print(bisect.bisect(arr, 5))         # 3  (same as bisect_right)

# insort(a, x) (alias of insort_right) -> inserts x into the list,
# AFTER any existing equal values. Modifies the list in place, returns None.
bisect.insort(arr, 5)
print(arr)   # [4, 5, 5, 5, 6, 7, 7, 8, 10, 12, 12, 13]

# insort_left(a, x) -> inserts x BEFORE any existing equal values.
# Modifies in place, returns None.
bisect.insort_left(arr, 9)
print(arr)   # [4, 5, 5, 5, 6, 7, 7, 8, 9, 10, 12, 12, 13]

# insort_right(a, x) -> inserts x AFTER any existing equal values.
# Modifies in place, returns None.
bisect.insort_right(arr, 11)
print(arr)   # [4, 5, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12, 12, 13]

# Optional lo/hi args limit the search range: bisect_left(a, x, lo, hi)
print(bisect.bisect_left(arr, 7, 0, 4))   # 4 (only searches arr[0:4])

# Optional key arg (Python 3.10+): compare using a function on elements.
words = ["a", "bb", "ccc", "dddd"]
print(bisect.bisect_left(words, 3, key=len))   # 2 (first word with len >= 3)

# Common use: count occurrences of x in a sorted list
print(bisect.bisect_right(arr, 5) - bisect.bisect_left(arr, 5))   # 3
