def mod_inverse(a: int, m: int) -> int:
    """Returns the modular inverse of a mod m, or -1 if it does not exist."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return -1                     # inverse exists iff gcd(a, m) == 1
    return (x % m + m) % m            # normalize to [0, m)

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def gcd(a: int, b: int) -> int:
    """Iterative GCD using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a: int, b: int) -> int:
    """Recursive GCD."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm(a: int, b: int) -> int:
    """LCM via GCD. Python handles big ints natively, but the pattern still applies."""
    if a == 0 or b == 0:
        return 0
    a, b = abs(a), abs(b)
    return (a // gcd(a, b)) * b

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def gcd_array(nums: list[int]) -> int:
    """GCD of an entire array using reduce pattern."""
    from functools import reduce
    return reduce(gcd, nums)