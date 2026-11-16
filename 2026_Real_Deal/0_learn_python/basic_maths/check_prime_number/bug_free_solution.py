"""Check Prime Number: a prime is an integer > 1 whose only divisors are 1 and itself.
Zero, one and negatives are not prime."""
import math


class Solution:
    def is_prime_brute_force(self, number: int) -> bool:
        """Try every i in [2, number). O(n) time, O(1) space."""
        if number <= 1:
            return False
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    def is_prime_optimized(self, number: int) -> bool:
        """Divisors pair up, so testing up to sqrt(number) (inclusive) is enough.
        O(sqrt n) time, O(1) space."""
        if number <= 1:
            return False
        limit = math.isqrt(number)  # integer sqrt, no float errors
        for divisor in range(2, limit + 1):  # +1 because range end is exclusive
            if number % divisor == 0:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    cases = {-7: False, 0: False, 1: False, 2: True, 3: True, 4: False, 9: False, 25: False,
             49: False, 97: True, 100: False, 7919: True, 7921: False}
    for value, expected in cases.items():
        assert solution.is_prime_brute_force(value) == expected, value
        assert solution.is_prime_optimized(value) == expected, value
    print("all tests passed")
