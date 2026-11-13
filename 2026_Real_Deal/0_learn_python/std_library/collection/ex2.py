"""
collections.Counter - a dict subclass that counts how many times each item appears.
Keys are the items, values are their counts.
"""
from collections import Counter

# ---------------------------------------------------------------
# 1. Creating a Counter
# ---------------------------------------------------------------
nums = Counter([1, 2, 2, 3, 2, 3, 3, 4])
print("Counter:", nums)
# -> Counter({2: 3, 3: 3, 1: 1, 4: 1})
#    1 appears once, 2 appears 3 times, 3 appears 3 times, 4 appears once
#    (ordered by count, highest first; ties keep first-seen order)

# ---------------------------------------------------------------
# 2. Looking up a count: counter[item]
#    Returns how many times the item appears.
#    Missing items return 0 (no KeyError, unlike a normal dict).
# ---------------------------------------------------------------
print("count of 1  :", nums[1])    # -> 1
print("count of 2  :", nums[2])    # -> 3
print("count of 3  :", nums[3])    # -> 3
print("count of 4  :", nums[4])    # -> 1
print("count of 10 :", nums[10])   # -> 0  (10 is not in the Counter)

# ---------------------------------------------------------------
# 3. most_common(n)
#    Returns a list of (item, count) tuples, highest count first.
#    - no argument -> all items
#    - n           -> only the top n items
#    - n bigger than the number of items -> just returns everything
# ---------------------------------------------------------------
print("most_common()   :", nums.most_common())     # [(2, 3), (3, 3), (1, 1), (4, 1)]
print("most_common(1)  :", nums.most_common(1))    # [(2, 3)]
print("most_common(2)  :", nums.most_common(2))    # [(2, 3), (3, 3)]
print("most_common(5)  :", nums.most_common(5))    # [(2, 3), (3, 3), (1, 1), (4, 1)]
print("most_common(10) :", nums.most_common(10))   # same as above, only 4 items exist

# ---------------------------------------------------------------
# 4. elements()
#    Returns an ITERATOR that repeats each item as many times as its count.
#    Printing it directly only shows the iterator object, so wrap it in list().
# ---------------------------------------------------------------
print("elements() raw  :", nums.elements())
# -> <itertools.chain object at 0x...>   (not useful to read)
print("elements() list :", list(nums.elements()))
# -> [1, 2, 2, 2, 3, 3, 3, 4]   (the original data, grouped by item)

# ---------------------------------------------------------------
# 5. update(iterable)
#    ADDS to the existing counts (a normal dict's update would overwrite).
# ---------------------------------------------------------------
nums.update([7])
print("after update([7])        :", list(nums.elements()))
# -> 7 is new, so it is added with count 1
# -> [1, 2, 2, 2, 3, 3, 3, 4, 7]

nums.update([7, 7, 3, 4])
print("after update([7,7,3,4])  :", list(nums.elements()))
# -> 7: 1+2 = 3,  3: 3+1 = 4,  4: 1+1 = 2
# -> [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 7, 7, 7]

# ---------------------------------------------------------------
# 6. subtract(iterable)
#    REMOVES from the existing counts. Counts may go to 0 or negative;
#    elements() ignores items whose count is 0 or less.
# ---------------------------------------------------------------
nums.subtract([3])
print("after subtract([3])      :", list(nums.elements()))
# -> 3: 4-1 = 3
# -> [1, 2, 2, 2, 3, 3, 3, 4, 4, 7, 7, 7]

# ---------------------------------------------------------------
# 7. Math between Counters
#    Two fresh Counters used for all the operators below:
#      a = {2: 3, 3: 3, 1: 1, 4: 1}
#      b = {3: 2, 1: 1, 4: 1, 5: 1}
# ---------------------------------------------------------------
a = Counter([1, 2, 2, 3, 2, 3, 3, 4])
b = Counter([3, 3, 1, 4, 5])

# a - b  : subtract counts, KEEP ONLY results greater than 0
diff = a - b
print("a - b :", dict(diff))
# -> 2: 3-0 = 3,  3: 3-2 = 1,  1: 1-1 = 0 (dropped),  4: 1-1 = 0 (dropped)
# -> {2: 3, 3: 1}

# b - a  : the other direction gives a different answer
print("b - a :", dict(b - a))
# -> 3: 2-3 = -1 (dropped), 5: 1-0 = 1
# -> {5: 1}

# a + b  : add counts together
total = a + b
print("a + b :", dict(total))
# -> 1: 2,  2: 3,  3: 5,  4: 2,  5: 1
# -> {1: 2, 2: 3, 3: 5, 4: 2, 5: 1}

# x & y  : INTERSECTION -> the MINIMUM count of each item present in both
both = diff & total
print("(a - b) & (a + b) :", dict(both))
# -> diff = {2: 3, 3: 1},  total = {1: 2, 2: 3, 3: 5, 4: 2, 5: 1}
# -> 2: min(3,3) = 3,  3: min(1,5) = 1
# -> {2: 3, 3: 1}

# x | y  : UNION -> the MAXIMUM count of each item present in either
either = diff | total
print("(a - b) | (a + b) :", dict(either))
# -> 1: 2,  2: max(3,3) = 3,  3: max(1,5) = 5,  4: 2,  5: 1
# -> {1: 2, 2: 3, 3: 5, 4: 2, 5: 1}
