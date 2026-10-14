def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n :
        if n % i == 0 or n %(i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(n: int) -> int:
    if n <= 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            for j in range(p * p, n , p):
                is_prime[j] = False
        p += 1
    return sum(is_prime)

def build_spf(n: int) -> list[int]:
    spf = list(range(n + 1))
    p = 2
    while p * p <= n:
        if spf[p] == p:  # p is prime
            for j in range(p * p, n + 1, p):
                if spf[j] == j:
                    spf[j] = p
        p += 1
    return spf

def factorize(x: int, spf: list[int]) -> list[int]:
    factors = []
    while x > 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors