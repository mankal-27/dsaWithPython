"""
namedtuple  (from the collections module)
-----------------------------------------
- A normal tuple, but every position also gets a NAME.
  Normal tuple : p[0], p[1]   -> hard to remember what 0 and 1 mean
  namedtuple   : p.x, p.y     -> readable, and p[0], p[1] still work
- It is IMMUTABLE (like a tuple): you cannot change a field after creating it.
- It uses no more memory than a plain tuple (lighter than a class/dict).
- namedtuple(...) itself returns a NEW CLASS; calling that class makes objects.
- Variant: typing.NamedTuple (same idea, written like a class with type hints).
"""

from collections import namedtuple

# namedtuple(typename, field_names) -> returns a new class called "Point".
# field_names can be a list, or a string like "x y" / "x, y".
Point = namedtuple("Point", ["x", "y"])

# ---------- CREATE ----------
p = Point(3, 4)                  # by position -> Point(x=3, y=4)
q = Point(x=10, y=20)            # by name     -> Point(x=10, y=20)
print(p)                         # -> prints: Point(x=3, y=4)
print(q)                         # -> prints: Point(x=10, y=20)

# ---------- READ ----------
print(p.x)                       # by name, returns 3          -> prints: 3
print(p[1])                      # by index, returns 4         -> prints: 4
x, y = p                         # unpacking works like a tuple (x=3, y=4)
print(x, y)                      # -> prints: 3 4
print(len(p))                    # number of fields, returns 2 -> prints: 2
print(p == (3, 4))               # equals a plain tuple with same values -> prints: True

# ---------- CHANGE (you can't edit, but you can make a copy with a change) ----------
# p.x = 99 would raise AttributeError: can't set attribute (immutable!)
p2 = p._replace(x=99)            # returns a NEW Point; p itself is unchanged
print(p2)                        # -> prints: Point(x=99, y=4)
print(p)                         # -> prints: Point(x=3, y=4)

# ---------- INSPECT ----------
print(p._fields)                 # tuple of field names, returns ('x', 'y') -> prints: ('x', 'y')
print(p._asdict())               # converts to a dict (regular dict in Python 3.8+)
                                 # -> prints: {'x': 3, 'y': 4}

# ---------- BUILD FROM OTHER DATA ----------
r = Point._make([7, 8])          # makes a Point from any iterable (list, tuple...) -> Point(x=7, y=8)
print(r)                         # -> prints: Point(x=7, y=8)
d = {"x": 1, "y": 2}
s = Point(**d)                   # ** unpacks a dict into keyword args -> Point(x=1, y=2)
print(s)                         # -> prints: Point(x=1, y=2)

# ---------- TUPLE METHODS STILL WORK ----------
print(p.count(3))                # how many times 3 appears, returns 1 -> prints: 1
print(p.index(4))                # position of first 4, returns 1      -> prints: 1

# ---------- DEFAULT VALUES ----------
# defaults=[...] gives defaults to the LAST fields (those can then be skipped).
Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
print(Person("Asha", 30))        # city skipped -> prints: Person(name='Asha', age=30, city='Unknown')
print(Person._field_defaults)    # dict of defaults -> prints: {'city': 'Unknown'}

# ---------- SORTING / MAX (handy with lists of namedtuples) ----------
people = [Person("Ravi", 25, "Delhi"), Person("Asha", 30, "Pune"), Person("Meera", 22, "Goa")]
print(sorted(people, key=lambda t: t.age))   # new list sorted by age
# -> prints: [Person(name='Meera', age=22, city='Goa'), Person(name='Ravi', age=25, city='Delhi'), Person(name='Asha', age=30, city='Pune')]
print(max(people, key=lambda t: t.age).name) # oldest person's name -> prints: Asha

# Typical use: return several values from a function, or store (row, col) / (node, dist)
# pairs in DSA problems, e.g. queue.append(Cell(row=0, col=1)) instead of queue.append((0, 1)).
