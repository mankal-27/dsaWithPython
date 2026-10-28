def factorial(n):
    product = 1

    while n > 0:
        product = product * n
        n = n - 1
    return product

print(factorial(5))

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))

def printn(n):
    for i in range(1 , n+1):
        print(i)

printn(5)

def printnRecrusively(n):
    if n == 0:
        return
    printnRecrusively(n - 1)
    print(n)

printnRecrusively(5)