class Solution:
    def sum_of_divisors_linear_scan(self, n):
        total = 0
        for i in range(1, n+1):
            if(n % i == 0):
                total = total + i
        return total

    def sum_of_divisors_sqrt_scan(self, n):
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                partner = n // i
                total = total + i
                if partner != i :
                    total += partner
            i += 1
        return total
