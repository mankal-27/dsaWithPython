# string methods
#
# A str is TEXT in Python, e.g. "hello".
# Key idea: strings are IMMUTABLE (cannot be changed in place).
#   Every method below returns a NEW string (or a number/bool/list);
#   the original string is never modified. To keep a result, store it in a variable.
#
# Theme: we clean up and inspect one messy user-typed sentence.

s = "  Hello, World! Python is fun.  "

# ---------- 1. Cleaning whitespace ----------
print(s.strip())             # removes spaces from BOTH ends, returns new str
                             # -> prints: Hello, World! Python is fun.
print(s.lstrip())            # removes spaces from the LEFT end only
                             # -> prints: Hello, World! Python is fun.
print(s.rstrip())            # removes spaces from the RIGHT end only
                             # -> prints:   Hello, World! Python is fun.

t = s.strip()                # save the cleaned version; s itself is unchanged
print(t)                     # -> prints: Hello, World! Python is fun.

# ---------- 2. Changing case ----------
print(t.upper())             # all capitals, returns new str
                             # -> prints: HELLO, WORLD! PYTHON IS FUN.
print(t.lower())             # all small letters
                             # -> prints: hello, world! python is fun.
print(t.title())             # First Letter Of Each Word Capital
                             # -> prints: Hello, World! Python Is Fun.
print(t.capitalize())        # only the very first letter capital, rest small
                             # -> prints: Hello, world! python is fun.
print(t.swapcase())          # flips upper <-> lower
                             # -> prints: hELLO, wORLD! pYTHON IS FUN.

# ---------- 3. Searching ----------
print(t.find("World"))       # index of first match, -1 if not found (never errors)
                             # -> prints: 7
print(t.find("Java"))        # -> prints: -1
print(t.index("World"))      # like find, but raises ValueError if not found
                             # -> prints: 7
print(t.count("o"))          # how many times the piece appears (returns int)
                             # -> prints: 3
print(t.startswith("Hello")) # True if string begins with it (returns bool)
                             # -> prints: True
print(t.endswith("fun."))    # True if string ends with it
                             # -> prints: True
print("World" in t)          # 'in' operator: True/False (not a method, but very common)
                             # -> prints: True

# ---------- 4. Replacing ----------
print(t.replace("fun", "great"))  # swaps ALL matches, returns new str
                                  # -> prints: Hello, World! Python is great.
print(t.replace("o", "0", 1))     # 3rd argument = max number of replacements
                                  # -> prints: Hell0, World! Python is fun.

# ---------- 5. Split and join ----------
words = t.split()            # splits on any whitespace, returns a LIST of strings
print(words)                 # -> prints: ['Hello,', 'World!', 'Python', 'is', 'fun.']
print(t.split(","))          # split on a chosen separator
                             # -> prints: ['Hello', ' World! Python is fun.']
print(" ".join(words))       # glues a list of strings together using " " between
                             # -> prints: Hello, World! Python is fun.
print("-".join(words))       # -> prints: Hello,-World!-Python-is-fun.
print("a\nb\nc".splitlines())  # splits at line breaks, returns a list
                             # -> prints: ['a', 'b', 'c']
print(t.partition(" "))      # splits at FIRST separator into 3 parts (tuple)
                             # -> prints: ('Hello,', ' ', 'World! Python is fun.')

# ---------- 6. Checking what kind of text it is (all return bool) ----------
print("abc".isalpha())       # only letters?              -> prints: True
print("123".isdigit())       # only digits?               -> prints: True
print("abc123".isalnum())    # only letters/digits?       -> prints: True
print("   ".isspace())       # only whitespace?           -> prints: True
print("hello".islower())     # all lowercase?             -> prints: True
print("HELLO".isupper())     # all uppercase?             -> prints: True

# ---------- 7. Padding and alignment ----------
print("7".zfill(3))          # pad with zeros on the left to width 3
                             # -> prints: 007
print("hi".center(6, "*"))   # center in width 6, fill with '*'
                             # -> prints: **hi**
print("hi".ljust(5, "."))    # left-align, pad right
                             # -> prints: hi...
print("hi".rjust(5, "."))    # right-align, pad left
                             # -> prints: ...hi

# ---------- 8. Basics that are not methods but used all the time ----------
print(len(t))                # number of characters (returns int)
                             # -> prints: 28
print(t[0])                 # first character (indexing)  -> prints: H
print(t[-1])                 # last character              -> prints: .
print(t[0:5])                # slice, chars 0 up to (not incl.) 5 -> prints: Hello
print(t[::-1])               # reversed copy
                             # -> prints: .nuf si nohtyP !dlroW ,olleH
print("ab" * 3)              # repeat                      -> prints: ababab
print("Hi " + "there")       # concatenate                 -> prints: Hi there
print(f"{t[:5]} has {len(t)} chars")  # f-string: put values inside text
                             # -> prints: Hello has 28 chars

# ---------- 9. Immutability proof ----------
print(s)                     # original is still untouched (spaces and all)
                             # -> prints:   Hello, World! Python is fun.
# t[0] = "J"                 # would raise TypeError: str does not allow item assignment

# Typical use: s.strip().lower().split() -> clean user input, then get its words.
# Palindrome check: word == word[::-1]
