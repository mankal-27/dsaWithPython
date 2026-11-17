import math  # built-in module with math functions and constants

# ---------- Constants ----------
print(math.pi)   # 3.141592653589793 -> the value of pi
print(math.e)    # 2.718281828459045 -> Euler's number
print(math.inf)  # inf -> positive infinity
print(math.nan)  # nan -> "not a number"

# ---------- Rounding ----------
print(math.ceil(4.2))    # 5  -> rounds UP to the next integer
print(math.floor(4.8))   # 4  -> rounds DOWN to the previous integer
print(math.trunc(-4.8))  # -4 -> chops off the decimal part (toward zero)

# ---------- Powers and roots ----------
print(math.sqrt(16))     # 4.0   -> square root (always returns a float)
print(math.isqrt(17))    # 4     -> integer square root (floor of sqrt)
print(math.pow(2, 3))    # 8.0   -> 2 to the power 3 (returns a float)
print(math.exp(1))       # 2.718281828459045 -> e raised to the power 1
print(math.cbrt(27))     # 3.0   -> cube root (Python 3.11+)

# ---------- Logarithms ----------
print(math.log(math.e))  # 1.0 -> natural log (base e)
print(math.log(8, 2))    # 3.0 -> log of 8 with base 2
print(math.log2(8))      # 3.0 -> log base 2
print(math.log10(1000))  # 3.0 -> log base 10

# ---------- Absolute value and sign ----------
print(math.fabs(-7))          # 7.0   -> absolute value as a float
print(math.copysign(5, -1))   # -5.0  -> magnitude of 5 with the sign of -1

# ---------- Integer helpers ----------
print(math.factorial(5))   # 120 -> 5*4*3*2*1
print(math.gcd(12, 18))    # 6   -> greatest common divisor
print(math.lcm(4, 6))      # 12  -> least common multiple (Python 3.9+)
print(math.comb(5, 2))     # 10  -> "5 choose 2" (combinations)
print(math.perm(5, 2))     # 20  -> permutations of 2 items from 5
print(math.prod([1, 2, 3, 4]))  # 24 -> multiply all items in an iterable
print(math.fsum([0.1] * 10))    # 1.0 -> accurate float sum (plain sum gives 0.9999999999999999)

# ---------- Remainders ----------
print(math.fmod(7, 3))        # 1.0 -> remainder (sign follows the first number)
print(math.remainder(7, 3))   # 1.0 -> IEEE remainder (closest-multiple based)
print(math.modf(3.75))        # (0.75, 3.0) -> (fractional part, integer part)

# ---------- Trigonometry (angles are in RADIANS) ----------
print(math.sin(math.pi / 2))  # 1.0 -> sine
print(math.cos(0))            # 1.0 -> cosine
print(math.tan(math.pi / 4))  # ~1.0 -> tangent
print(math.asin(1))           # 1.5707963267948966 -> inverse sine
print(math.atan2(1, 1))       # 0.7853981633974483 -> angle of point (x=1, y=1)
print(math.radians(180))      # 3.141592653589793 -> degrees to radians
print(math.degrees(math.pi))  # 180.0 -> radians to degrees

# ---------- Distance ----------
print(math.hypot(3, 4))              # 5.0 -> sqrt(3**2 + 4**2)
print(math.dist((0, 0), (3, 4)))     # 5.0 -> distance between two points

# ---------- Checks (return True / False) ----------
print(math.isnan(math.nan))   # True  -> is the value NaN?
print(math.isinf(math.inf))   # True  -> is the value infinite?
print(math.isfinite(10))      # True  -> is it a normal number (not inf/nan)?
print(math.isclose(0.1 + 0.2, 0.3))  # True -> equal within a small tolerance
