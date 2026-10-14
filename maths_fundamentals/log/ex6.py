MOD = 10**9 + 7

def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def mat_pow(M, p):
    n = len(M)
    # Start with identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    while p > 0:
        if p & 1:
            result = multiply(result, M)
        M = multiply(M, M)
        p >>= 1
    return result

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    T = [[1, 1], [1, 0]]
    res = mat_pow(T, n)
    return res[0][1]

print(fibonacci(6))   # 8
print(fibonacci(10))  # 55