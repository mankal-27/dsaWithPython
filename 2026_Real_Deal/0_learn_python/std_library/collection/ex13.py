# dict methods
# A dict stores key -> value pairs. Keys must be hashable (str, int, tuple...).

d = {"a": 1, "b": 2, "c": 3}
print("start:", d)  # {'a': 1, 'b': 2, 'c': 3}

# ---- Reading ----
print(d["a"])           # d[key] -> value; raises KeyError if key is missing
print(d.get("a"))       # get(key) -> value, or None if missing (no error)
print(d.get("z", 0))    # get(key, default) -> default if missing -> 0
print(d.keys())         # keys() -> view of all keys: dict_keys(['a','b','c'])
print(d.values())       # values() -> view of all values: dict_values([1,2,3])
print(d.items())        # items() -> view of (key, value) tuples
print(len(d))           # len() -> number of pairs -> 3
print("a" in d)         # in -> True if key exists (checks keys only)

# ---- Adding / updating ----
d["d"] = 4              # assign: adds the key, or overwrites if it exists
print(d)                # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d.update({"a": 10, "e": 5})  # update(other) -> merges in; returns None
print(d)                # 'a' overwritten to 10, 'e' added

print(d.setdefault("f", 6))  # setdefault(key, default) -> returns value;
                             # inserts key=default only if key was missing -> 6
print(d.setdefault("a", 99)) # 'a' exists, so nothing changes -> returns 10

# ---- Removing ----
print(d.pop("f"))       # pop(key) -> removes key, returns its value -> 6
print(d.pop("zzz", None))  # pop(key, default) -> default if missing, no error
print(d.popitem())      # popitem() -> removes & returns LAST inserted pair
                        # -> ('e', 5)   (LIFO order, Python 3.7+)
del d["d"]              # del d[key] -> removes key; KeyError if missing
print(d)                # {'a': 10, 'b': 2, 'c': 3}

# ---- Copying ----
c = d.copy()            # copy() -> shallow copy (new dict, same inner objects)
c["a"] = 0
print(d["a"], c["a"])   # 10 0 -> original unaffected

# ---- Creating ----
print(dict.fromkeys(["x", "y"], 0))  # fromkeys(keys, value) -> {'x':0,'y':0}
print(dict(zip("ab", [1, 2])))       # dict(pairs) -> {'a': 1, 'b': 2}

# ---- Looping ----
for k, v in d.items():  # most common way: unpack key and value together
    print(k, v)

# ---- Merging (Python 3.9+) ----
print({"a": 1} | {"b": 2})  # | -> new merged dict {'a':1,'b':2}

# ---- Sorting ----
print(sorted(d))                       # sorted keys -> ['a', 'b', 'c']
print(sorted(d.items(), key=lambda kv: kv[1]))  # pairs sorted by value

# ---- Comprehension ----
print({k: v * 2 for k, v in d.items()})  # build a new dict from d

# ---- Clearing ----
d.clear()               # clear() -> removes everything; returns None
print(d)                # {}
