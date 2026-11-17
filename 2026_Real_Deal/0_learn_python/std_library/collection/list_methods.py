# list methods
#
# A list is an ordered, changeable (mutable) collection that can hold any
# values, including duplicates. Items are reached by position (index),
# starting at 0. Negative indexes count from the end (-1 = last item).
#
# Most list methods change the list IN PLACE and return None.
# So never write:  nums = nums.sort()   (that would make nums = None)
#
# Theme: a shopping basket that we add to, read, remove from, and reorder.

basket = ["apple", "banana"]          # make a list with 2 items
print(basket)                         # -> prints: ['apple', 'banana']

# ---------- ADD ----------
basket.append("cherry")               # adds ONE item at the end; returns None
print(basket)                         # -> prints: ['apple', 'banana', 'cherry']

basket.insert(1, "mango")             # insert(index, item): puts item at index, shifts the rest right; returns None
print(basket)                         # -> prints: ['apple', 'mango', 'banana', 'cherry']

basket.extend(["grape", "banana"])    # adds EVERY item of another iterable to the end; returns None
print(basket)                         # -> prints: ['apple', 'mango', 'banana', 'cherry', 'grape', 'banana']

# ---------- READ / SEARCH ----------
print(basket[0])                      # item at index 0 -> prints: apple
print(basket[-1])                     # last item -> prints: banana
print(basket[1:3])                    # slice [start:stop) makes a NEW list -> prints: ['mango', 'banana']
print(len(basket))                    # number of items (built-in function) -> prints: 6
print("cherry" in basket)             # membership test, returns True/False -> prints: True

print(basket.index("banana"))         # index of the FIRST match (error if missing) -> prints: 2
print(basket.count("banana"))         # how many times the item appears -> prints: 2

# ---------- CHANGE ----------
basket[0] = "avocado"                 # replace the item at index 0; no return value
print(basket)                         # -> prints: ['avocado', 'mango', 'banana', 'cherry', 'grape', 'banana']

# ---------- REMOVE ----------
basket.remove("banana")               # removes the FIRST match by value; returns None (error if missing)
print(basket)                         # -> prints: ['avocado', 'mango', 'cherry', 'grape', 'banana']

last = basket.pop()                   # removes AND RETURNS the last item
print(last)                           # -> prints: banana

second = basket.pop(1)                # pop(index): removes AND RETURNS the item at that index
print(second)                         # -> prints: mango
print(basket)                         # -> prints: ['avocado', 'cherry', 'grape']

del basket[0]                         # statement (not a method): deletes the item at index 0, returns nothing
print(basket)                         # -> prints: ['cherry', 'grape']

# ---------- REORDER ----------
nums = [5, 2, 9, 1]

nums.sort()                           # sorts IN PLACE, smallest first; returns None
print(nums)                           # -> prints: [1, 2, 5, 9]

nums.sort(reverse=True)               # biggest first
print(nums)                           # -> prints: [9, 5, 2, 1]

nums.reverse()                        # flips the order IN PLACE; returns None
print(nums)                           # -> prints: [1, 2, 5, 9]

print(sorted([3, 1, 2]))              # built-in sorted(): returns a NEW sorted list, original untouched -> prints: [1, 2, 3]

# ---------- COPY / CLEAR ----------
alias = nums                          # NOT a copy: both names point to the SAME list
copy = nums.copy()                    # a real (shallow) copy: a new list with the same items
nums.append(100)
print(alias)                          # sees the change -> prints: [1, 2, 5, 9, 100]
print(copy)                           # unaffected -> prints: [1, 2, 5, 9]

nums.clear()                          # removes ALL items, list stays but is empty; returns None
print(nums)                           # -> prints: []

# Typical use: use append() + pop() as a stack (last in, first out).
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())                    # -> prints: 2
