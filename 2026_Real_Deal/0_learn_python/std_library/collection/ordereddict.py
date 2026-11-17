# ---------------------------------------------------------------
# OrderedDict (from the "collections" module)
# ---------------------------------------------------------------
# What it is : a dictionary that REMEMBERS the order in which keys were added.
# Vs plain dict: a normal dict (Python 3.7+) also keeps insertion order, but
#                OrderedDict adds extras:
#                  - move_to_end(key, last=True)  -> move a key to the end / front
#                  - popitem(last=True)           -> remove from the end / front
#                  - two OrderedDicts are equal only if the ORDER is the same too
# Common use : LRU cache (move_to_end + popitem(last=False)).
# Example idea: a "recently watched" list of 3 tasks.
# ---------------------------------------------------------------

from collections import OrderedDict  # import the class; prints nothing

# OrderedDict([...]) builds a new OrderedDict from (key, value) pairs.
od = OrderedDict([("dsa", 1), ("python", 2), ("sql", 3)])
print(od)  # -> prints: OrderedDict({'dsa': 1, 'python': 2, 'sql': 3})

# ---------- add / change ----------
od["java"] = 4  # new key is added at the END. Returns nothing.
print(od)  # -> prints: OrderedDict({'dsa': 1, 'python': 2, 'sql': 3, 'java': 4})

od["dsa"] = 10  # existing key: value changes, its POSITION stays the same.
print(od)  # -> prints: OrderedDict({'dsa': 10, 'python': 2, 'sql': 3, 'java': 4})

# update(other) adds many keys at once (or changes existing ones). Returns None.
od.update({"go": 5, "sql": 30})  # "go" is new -> goes to end, "sql" is just changed
print(od)  # -> prints: OrderedDict({'dsa': 10, 'python': 2, 'sql': 30, 'java': 4, 'go': 5})

# setdefault(key, default): returns the value if key exists,
# otherwise ADDS key=default and returns default.
print(od.setdefault("python", 99))  # -> prints: 2 (already there, unchanged)
print(od.setdefault("rust", 6))  # -> prints: 6 (was missing, now added at the end)

# ---------- read ----------
print(od["dsa"])  # -> prints: 10 (raises KeyError if key is missing)
print(od.get("php", "none"))  # -> prints: none (get never errors, returns default)
print("java" in od)  # -> prints: True (True/False check for a key)
print(list(od.keys()))  # -> prints: ['dsa', 'python', 'sql', 'java', 'go', 'rust']
print(list(od.values()))  # -> prints: [10, 2, 30, 4, 5, 6]
print(list(od.items()))  # -> prints: [('dsa', 10), ('python', 2), ('sql', 30), ('java', 4), ('go', 5), ('rust', 6)]
print(len(od))  # -> prints: 6 (number of keys)

# ---------- reorder (the OrderedDict superpower) ----------
od.move_to_end("dsa")  # moves "dsa" to the END. Returns None.
print(list(od.keys()))  # -> prints: ['python', 'sql', 'java', 'go', 'rust', 'dsa']

od.move_to_end("rust", last=False)  # last=False -> moves "rust" to the FRONT.
print(list(od.keys()))  # -> prints: ['rust', 'python', 'sql', 'java', 'go', 'dsa']

# ---------- remove ----------
print(od.popitem())  # removes + returns the LAST pair (like a stack)
# -> prints: ('dsa', 10)

print(od.popitem(last=False))  # removes + returns the FIRST pair (like a queue)
# -> prints: ('rust', 6)

print(od.pop("sql"))  # removes the key, returns its value (KeyError if missing)
# -> prints: 30

print(od.pop("php", "not found"))  # with a default it never errors
# -> prints: not found

del od["java"]  # deletes the key. Returns nothing (KeyError if missing).
print(od)  # -> prints: OrderedDict({'python': 2, 'go': 5})

# ---------- order matters when comparing ----------
a = OrderedDict([("x", 1), ("y", 2)])
b = OrderedDict([("y", 2), ("x", 1)])
print(a == b)  # -> prints: False (same items, different order)
print(dict(a) == dict(b))  # -> prints: True (a plain dict ignores order)

# ---------- copy and clear ----------
c = a.copy()  # returns a new OrderedDict with the same items (shallow copy)
c.clear()  # removes everything, returns None
print(c, a)  # -> prints: OrderedDict() OrderedDict({'x': 1, 'y': 2})

# Typical use tip: LRU cache = on every use call move_to_end(key);
# when it gets too big call popitem(last=False) to drop the oldest one.
