"""
deque (double-ended queue) from the `collections` module.

A deque is like a list, but adding/removing at BOTH ends is fast (O(1)).
(A normal list is slow when you insert/remove at the front.)

Methods covered (and what they return):
    append(x)         -> add x to the RIGHT end             -> None
    appendleft(x)     -> add x to the LEFT end              -> None
    pop()             -> remove RIGHT-most item             -> the removed item
    popleft()         -> remove LEFT-most item              -> the removed item
    extend(iter)      -> add every item to the RIGHT end    -> None
    extendleft(iter)  -> add every item to the LEFT end     -> None (order ends up reversed)
    insert(i, x)      -> insert x at index i                -> None
    remove(x)         -> remove first occurrence of x       -> None (ValueError if missing)
    rotate(n)         -> shift items n steps right          -> None (negative n = left)
    reverse()         -> reverse in place                   -> None
    count(x)          -> how many times x appears           -> int
    index(x)          -> index of first x                   -> int (ValueError if missing)
    copy()            -> shallow copy                       -> new deque
    clear()           -> remove everything                  -> None
    maxlen            -> fixed-size deque; old items fall off the opposite end
"""

from collections import deque

# ==============================================================
# PART 1: Adding and removing at the ends
# ==============================================================

dq = deque([2, 3, 1])
print("Start:              ", dq)            # deque([2, 3, 1])

# append(x): add to the right end
dq.append(5)
print("After append(5):    ", dq)            # deque([2, 3, 1, 5])

# appendleft(x): add to the left end
dq.appendleft(7)
print("After appendleft(7):", dq)            # deque([7, 2, 3, 1, 5])

# pop(): remove from the right end and RETURN the removed item
removed = dq.pop()
print("pop() returned:     ", removed)       # 5  (the right-most item)
print("Deque now:          ", dq)            # deque([7, 2, 3, 1])

# popleft(): remove from the left end and RETURN the removed item
removed = dq.popleft()
print("popleft() returned: ", removed)       # 7  (the left-most item)
print("Deque now:          ", dq)            # deque([2, 3, 1])

# ==============================================================
# PART 2: Adding many items at once
# ==============================================================

dq = deque([1, 2, 3])

# extend(iterable): add each item to the right, in order
dq.extend([4, 5])
print("After extend([4,5]):    ", dq)        # deque([1, 2, 3, 4, 5])

# extendleft(iterable): add each item to the left ONE BY ONE,
# so the items end up in reversed order
dq.extendleft([8, 9])
print("After extendleft([8,9]):", dq)        # deque([9, 8, 1, 2, 3, 4, 5])

# ==============================================================
# PART 3: Insert, remove, search
# ==============================================================

dq = deque([10, 20, 30, 20])

# insert(i, x): put x at index i, shifting the rest to the right
dq.insert(1, 15)
print("After insert(1, 15):", dq)            # deque([10, 15, 20, 30, 20])

# remove(x): delete the FIRST x found (raises ValueError if not found)
dq.remove(20)
print("After remove(20):   ", dq)            # deque([10, 15, 30, 20])

# count(x): how many times x appears
print("count(20):          ", dq.count(20))  # 1

# index(x): position of the first x (raises ValueError if not found)
print("index(30):          ", dq.index(30))  # 2

# ==============================================================
# PART 4: Rotate and reverse
# ==============================================================

dq = deque([1, 2, 3, 4])

# rotate(n): positive n moves items to the right, wrapping around
dq.rotate(1)
print("After rotate(1): ", dq)               # deque([4, 1, 2, 3])

# rotate(-n): negative n moves items to the left, wrapping around
dq.rotate(-2)
print("After rotate(-2):", dq)               # deque([2, 3, 4, 1])

# reverse(): flip the order in place
dq.reverse()
print("After reverse(): ", dq)               # deque([1, 4, 3, 2])

# ==============================================================
# PART 5: Copy and clear
# ==============================================================

original = deque([1, 2, 3])

# copy(): returns a NEW deque; changing it doesn't affect the original
duplicate = original.copy()
duplicate.append(99)
print("original: ", original)                # deque([1, 2, 3])
print("duplicate:", duplicate)               # deque([1, 2, 3, 99])

# clear(): remove everything
duplicate.clear()
print("After clear():", duplicate)           # deque([])

# ==============================================================
# PART 6: maxlen (fixed-size deque)
# ==============================================================

# When full, adding to one end automatically drops an item from the other.
window = deque([1, 2, 3], maxlen=3)
print("Start:            ", window)          # deque([1, 2, 3], maxlen=3)

window.append(4)                             # 1 falls off the left
print("After append(4):  ", window)          # deque([2, 3, 4], maxlen=3)

window.appendleft(0)                         # 4 falls off the right
print("After appendleft(0):", window)        # deque([0, 2, 3], maxlen=3)

# ==============================================================
# BONUS: built-in functions and indexing also work on a deque
# ==============================================================

dq = deque([5, 6, 7])
print("len(dq):", len(dq))                   # 3
print("dq[0]:  ", dq[0])                     # 5  (fast at the ends)
print("dq[-1]: ", dq[-1])                    # 7
