def nCr(n: int, r: int) -> int:
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    # Use symmetry: C(n, r) = C(n, n-r)
    if r > n - r:
        r = n - r

    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result


def build_pascal(n: int) -> list[list[int]]:
    dp = [[1] * (i + 1) for i in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp

# Usage: dp[n][r] gives C(n, r)

MOD = 10**9 + 7

def precompute(n: int):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    return fact, inv_fact

def nCr(n: int, r: int, fact: list, inv_fact: list) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD