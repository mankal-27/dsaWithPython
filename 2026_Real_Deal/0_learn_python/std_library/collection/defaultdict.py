from collections import defaultdict

# ---------------------------------------------------------------
# defaultdict(factory)
#   A normal dict, except: if you read a key that does not exist,
#   it CREATES that key automatically using factory() as the value,
#   instead of raising KeyError.
#   (A normal dict would crash on dd["zyc"] with KeyError.)
#
#   factory = int   -> missing key gets 0
#   factory = list  -> missing key gets []
#   factory = str   -> missing key gets ""
#   factory = set   -> missing key gets set()
#
#   Extra things only defaultdict has:
#     dd.default_factory  -> the factory you passed (int, list, ... or None)
#     dd.__missing__(key) -> called automatically when a key is missing;
#                            runs factory(), stores it, returns it
#                            (you rarely call it yourself)
# ---------------------------------------------------------------

# --- Example 1: defaultdict(int) -------------------------------
dd = defaultdict(int)       # default value for missing keys = int() = 0

# Assigning always works like a normal dict (any key type, any value type).
dd[1] = 'Manju'             # int key    -> str value
dd["kal"] = "manju"         # str key    -> str value
dd["u"] = 99                # str key    -> int value
dd["list"] = [1, 2, 4]      # str key    -> list value

# print(dd) -> shows the whole dict with its class name:
# defaultdict(<class 'int'>, {1: 'Manju', 'kal': 'manju', 'u': 99, 'list': [1, 2, 4]})
print(dd)

# "zyc" was never added. A normal dict would raise KeyError here.
# defaultdict creates dd["zyc"] = 0 and RETURNS 0.   -> prints: 0
# Side effect: "zyc" is now a real key inside dd.
print(dd["zyc"])

# --- Example 2: defaultdict(list) ------------------------------
ddList = defaultdict(list)  # default value for missing keys = list() = []

ddList["listing"] = [1, 2, 3, 4]   # set the key to a list
ddList["listing"].append(5)        # list.append(x): adds x at the end, returns None
                                   # (it changes the list in place)

# Reading the key returns the list itself.   -> prints: [1, 2, 3, 4, 5]
print(ddList["listing"])

# Typical use: group items without checking "does key exist?" first.
#   ddList["new_key"].append(1)    # works even if "new_key" is new,
#                                  # because it starts as [] automatically

# ---------------------------------------------------------------
# Other methods (all inherited from dict, so they work the same way)
# ---------------------------------------------------------------
demo = defaultdict(int)
demo["a"] = 1
demo["b"] = 2

# default_factory: the factory this defaultdict was created with.
print(demo.default_factory)        # -> <class 'int'>

# --- Reading WITHOUT creating the key (safe checks) ---
print("zzz" in demo)               # `in` returns True/False, does NOT create key -> False
print(demo.get("zzz"))             # .get(key) returns the value, or None if missing,
                                   # does NOT create key                          -> None
print(demo.get("zzz", -1))         # .get(key, default) returns default if missing -> -1
# Compare: demo["zzz"] WOULD create "zzz" with value 0.

# --- Looking at contents (each returns a "view" that stays in sync with the dict) ---
print(list(demo.keys()))           # .keys()   -> all keys              -> ['a', 'b']
print(list(demo.values()))         # .values() -> all values            -> [1, 2]
print(list(demo.items()))          # .items()  -> (key, value) pairs    -> [('a', 1), ('b', 2)]
print(len(demo))                   # len()     -> number of keys        -> 2

# --- Changing contents ---
print(demo.pop("a"))               # .pop(key) removes key, RETURNS its value     -> 1
                                   # (KeyError if missing and no default given)
print(demo.pop("nope", "none"))    # .pop(key, default) returns default if missing -> none
print(demo.setdefault("c", 10))    # .setdefault(key, val): if key exists returns its value,
                                   # else inserts val and returns it              -> 10
demo.update({"b": 20, "d": 4})     # .update(other) merges other in, overwrites existing keys,
                                   # returns None
print(dict(demo))                  # -> {'b': 20, 'c': 10, 'd': 4}

print(demo.popitem())              # .popitem() removes and RETURNS the LAST (key, value) pair
                                   #                                               -> ('d', 4)
del demo["c"]                      # del dd[key] removes the key, returns nothing
                                   # (KeyError if the key is missing)

copied = demo.copy()               # .copy() returns a shallow copy (still a defaultdict)
print(copied)                      # -> defaultdict(<class 'int'>, {'b': 20})

demo.clear()                       # .clear() removes everything, returns None
print(demo)                        # -> defaultdict(<class 'int'>, {})

# --- Common patterns ---
counts = defaultdict(int)          # COUNT items: missing key starts at 0
for ch in "banana":
    counts[ch] += 1
print(dict(counts))                # -> {'b': 1, 'a': 3, 'n': 2}

groups = defaultdict(list)         # GROUP items: missing key starts as []
for word in ["ant", "bee", "ape"]:
    groups[word[0]].append(word)
print(dict(groups))                # -> {'a': ['ant', 'ape'], 'b': ['bee']}
