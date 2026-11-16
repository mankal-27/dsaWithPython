"""Count Primes Till N: return how many primes p satisfy 2 <= p <= n."""
import math


class Solution:
    def is_prime(self, number: int) -> bool:
        """Trial division up to isqrt(number). O(sqrt n) time, O(1) space."""
        if number <= 1:
            return False
        for divisor in range(2, math.isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    def count_primes_brute_force(self, n: int) -> int:
        """Test every number in [2, n] on its own. O(n sqrt n) time, O(1) space."""
        count = 0
        for number in range(2, n + 1):  # +1 so n itself is included
            if self.is_prime(number):
                count += 1
        return count

    def count_primes_optimized(self, n: int) -> int:
        """Sieve of Eratosthenes. O(n log log n) time, O(n) space."""
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for number in range(2, math.isqrt(n) + 1):
            if is_prime[number]:
                # smaller multiples were already crossed out by smaller primes
                for multiple in range(number * number, n + 1, number):
                    is_prime[multiple] = False
        return sum(is_prime)


if __name__ == "__main__":
    solution = Solution()
    cases = {-5: 0, 0: 0, 1: 0, 2: 1, 3: 2, 4: 2, 7: 4, 10: 4, 25: 9, 100: 25, 1000: 168}
    for value, expected in cases.items():
        assert solution.count_primes_brute_force(value) == expected, value
        assert solution.count_primes_optimized(value) == expected, value
    print("all tests passed")
