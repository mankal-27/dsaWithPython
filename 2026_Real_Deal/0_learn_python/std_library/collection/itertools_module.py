"""
itertools = built-in module of fast "iterator builders".
- Every function returns a lazy ITERATOR (not a list). It makes values one at a time.
- Wrap in list(...) to see all values. An iterator can be used only ONCE.
- Common groups:
    * Combinatorics : combinations, combinations_with_replacement, permutations, product
    * Infinite      : count, cycle, repeat   (always limit them! list(cycle(x)) never ends)
    * Joining/slice : chain, islice, zip_longest
    * Running/group : accumulate, groupby, pairwise
"""
import itertools

arr = [1, 5, 6, 7]

# ---------- COMBINATORICS ----------
# combinations(iterable, r): all groups of r items, order does NOT matter, no repeats.
print(list(itertools.combinations(arr, 3)))
# -> prints: [(1, 5, 6), (1, 5, 7), (1, 6, 7), (5, 6, 7)]

# combinations_with_replacement(iterable, r): like combinations, but an item can be reused.
print(list(itertools.combinations_with_replacement([1, 2], 3)))
# -> prints: [(1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]

# permutations(iterable, r): all arrangements of r items, order DOES matter.
print(list(itertools.permutations([1, 2, 3], 2)))
# -> prints: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# product(*iterables): every pick of one item from each list (nested for-loops).
print(list(itertools.product([1, 2], [3, 4], [5, 6])))
# -> prints: [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

# product(x, repeat=n): same list used n times (all binary strings of length 2 here).
print(list(itertools.product([0, 1], repeat=2)))
# -> prints: [(0, 0), (0, 1), (1, 0), (1, 1)]

# ---------- INFINITE ITERATORS (always limit them) ----------
# cycle(iterable): repeats the items forever. islice(it, n) takes only the first n.
print(list(itertools.islice(itertools.cycle([1, 2, 4]), 7)))
# -> prints: [1, 2, 4, 1, 2, 4, 1]

# repeat(value, times): gives the same value `times` times (forever if times is left out).
print(list(itertools.repeat(5, 6)))
# -> prints: [5, 5, 5, 5, 5, 5]

# count(start, step): 10, 12, 14, ... forever.
print(list(itertools.islice(itertools.count(10, 2), 4)))
# -> prints: [10, 12, 14, 16]

# ---------- JOINING / SLICING ----------
# chain(*iterables): glues several lists into one stream.
print(list(itertools.chain([1, 2], [5, 6], [7, 8])))
# -> prints: [1, 2, 5, 6, 7, 8]

# chain.from_iterable(list_of_lists): same, but flattens one list-of-lists.
print(list(itertools.chain.from_iterable([[1, 2], [3], [4, 5]])))
# -> prints: [1, 2, 3, 4, 5]

# islice(iterable, start, stop, step): slicing for any iterator (no negative numbers).
print(list(itertools.islice([10, 20, 30, 40, 50], 1, 4)))
# -> prints: [20, 30, 40]

# zip_longest(a, b, fillvalue=...): like zip, but doesn't stop at the shorter list.
print(list(itertools.zip_longest([1, 2, 3], ["a"], fillvalue="-")))
# -> prints: [(1, 'a'), (2, '-'), (3, '-')]

# ---------- RUNNING TOTALS / GROUPING ----------
# accumulate(iterable, func=add): running total (prefix sums).
print(list(itertools.accumulate([1, 2, 6, 10])))
# -> prints: [1, 3, 9, 19]

# accumulate with a custom function, here max -> running maximum.
print(list(itertools.accumulate([3, 1, 5, 2], max)))
# -> prints: [3, 3, 5, 5]

# groupby(iterable, key): groups NEXT-TO-EACH-OTHER equal items (sort first to group all).
print([(k, len(list(g))) for k, g in itertools.groupby("aabbbc")])
# -> prints: [('a', 2), ('b', 3), ('c', 1)]

# pairwise(iterable): overlapping neighbours (Python 3.10+).
print(list(itertools.pairwise([1, 2, 3, 4])))
# -> prints: [(1, 2), (2, 3), (3, 4)]

# ---------- ITERATOR GOTCHA ----------
it = itertools.chain([1], [2])
print(list(it))  # -> prints: [1, 2]
print(list(it))  # -> prints: []   (already used up!)

# Typical use: combinations/permutations for brute-force DSA (subsets, orderings),
# accumulate for prefix sums, groupby for run-length encoding, product for grid/state loops.
