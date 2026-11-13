# set methods
#
# A set is an unordered collection of UNIQUE items.
#   - No duplicates: adding something that is already there does nothing.
#   - No indexes: you cannot do s[0] (order is not guaranteed).
#   - Items must be hashable (numbers, strings, tuples are ok; lists/dicts are not).
#   - Checking "x in s" is very fast (O(1) on average) - that is why sets are popular in DSA.
#   - Variant: frozenset = an immutable (cannot change) set.
#
# Theme: a tiny "fruit basket" we add to, remove from, and compare with another basket.

# ---------- create ----------
basket = {"apple", "banana", "cherry"}   # curly braces with items -> a set
empty = set()                            # empty set MUST be set(); {} would make a dict
print(len(basket))                       # len() returns number of items -> prints: 3
print(type(empty))                       # -> prints: <class 'set'>

dupes = set(["a", "b", "a", "b", "c"])   # set(iterable) removes duplicates, returns a new set
print(len(dupes))                        # -> prints: 3

# ---------- add / update ----------
basket.add("mango")                      # adds ONE item, mutates in place, returns None
basket.add("apple")                      # already there -> nothing happens, no error
print(len(basket))                       # -> prints: 4

basket.update(["kiwi", "grape"])         # adds MANY items from any iterable, returns None
print(len(basket))                       # -> prints: 6

# ---------- read / check ----------
print("apple" in basket)                 # membership test, returns bool -> prints: True
print("pear" in basket)                  # -> prints: False
print(sorted(basket))                    # sorted() returns a new LIST in order
                                         # -> prints: ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'mango']

# ---------- remove ----------
basket.remove("kiwi")                    # removes item; raises KeyError if missing; returns None
basket.discard("kiwi")                   # removes item; does NOTHING if missing (safe); returns None
popped = basket.pop()                    # removes and returns an ARBITRARY item (raises KeyError if empty)
print(len(basket))                       # 6 -> remove kiwi -> 5 -> pop one -> prints: 4
basket.add(popped)                       # put it back so the rest of the example is predictable
basket.add("kiwi")                       # put kiwi back too
print(len(basket))                       # -> prints: 6

# ---------- compare with another set ----------
other = {"banana", "cherry", "orange", "peach"}

print(sorted(basket.union(other)))       # (or basket | other) everything from both, new set
                                         # -> prints: ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'mango', 'orange', 'peach']
print(sorted(basket.intersection(other)))      # (or &) only items in BOTH, new set
                                         # -> prints: ['banana', 'cherry']
print(sorted(basket.difference(other)))        # (or -) in basket but NOT in other, new set
                                         # -> prints: ['apple', 'grape', 'kiwi', 'mango']
print(sorted(basket.symmetric_difference(other)))  # (or ^) in one but not both, new set
                                         # -> prints: ['apple', 'grape', 'kiwi', 'mango', 'orange', 'peach']

# ---------- yes/no questions (all return bool) ----------
small = {"apple", "banana"}
print(small.issubset(basket))            # every item of small is in basket? -> prints: True
print(basket.issuperset(small))          # basket contains all of small? -> prints: True
print(basket.isdisjoint({"pear"}))       # no items in common? -> prints: True

# ---------- in-place versions (change basket itself, return None) ----------
# update(), intersection_update(), difference_update(), symmetric_difference_update()
basket.difference_update(other)          # same as basket -= other
print(sorted(basket))                    # -> prints: ['apple', 'grape', 'kiwi', 'mango']

# ---------- copy / clear ----------
backup = basket.copy()                   # shallow copy, a separate new set
basket.clear()                           # removes everything, returns None
print(len(basket))                       # -> prints: 0
print(len(backup))                       # backup is unaffected -> prints: 4

# Typical use: remove duplicates fast, or check "have I seen this before?"
nums = [1, 2, 2, 3, 3, 3]
print(sorted(set(nums)))                 # -> prints: [1, 2, 3]
