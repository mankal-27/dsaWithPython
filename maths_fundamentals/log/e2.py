MOD = 10**9 + 7

def power(base, exp, mod):
    """Computes (base^exp) % mod using binary exponentiation."""
    result = 1
    base %= mod

    while exp > 0:
        if exp & 1:  # If current bit is 1
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod

    return result

def mod_inverse(a, mod):
    """Computes modular inverse of a under mod (mod must be prime)."""
    return power(a, mod - 2, mod)

def mod_subtract(a, b, mod):
    """Safe modular subtraction that avoids negative results."""
    return ((a % mod) - (b % mod) + mod) % mod

# Python also has built-in: pow(base, exp, mod) which does the same thing
print(power(2, 10, MOD))        # 1024
print(pow(2, 10, MOD))          # 1024 (built-in, equally fast)
print(mod_inverse(3, MOD))      # 333333336