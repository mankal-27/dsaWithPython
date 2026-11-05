class Solution:
    def is_prime_trial_division(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True

    def is_prime_sqrt_scan(self, n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def is_prime_six_k_optimization(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
        
