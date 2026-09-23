class Solution:
    def primes_up_to_n_trial_division(self, n):
        result = []
        for m in range(2, n+1):
            is_prime = True
            d = 2
            while d*d <= n:
                if m % d == 0 :
                    is_prime = False
                    break
                d += 1
                if is_prime:
                    result.append(m)
        return result
        
    def primes_up_to_n_sieve_of_eratosthenes(self, n):
        if n < 2:
            return []
        is_prime = [True] * [n + 1]
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1
        return [i for i in range(2, n + 1) if is_prime[i]]
