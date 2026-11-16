"""All Divisors of a Number: return every positive divisor in ascending order."""
import math


class Solution:
    def divisors_brute_force(self, number: int) -> list[int]:
        """Test every i in 1..number. O(n) time, O(1) extra space."""
        divisors = []
        for candidate in range(1, number + 1):  # start at 1 (no mod by 0), include number
            if number % candidate == 0:
                divisors.append(candidate)
        return divisors

    def divisors_optimized(self, number: int) -> list[int]:
        """Divisors come in pairs (i, n // i); scan only up to sqrt(n). O(sqrt n) time."""
        divisors = []
        for small in range(1, math.isqrt(number) + 1):
            if number % small == 0:
                divisors.append(small)
                partner = number // small  # integer division keeps ints
                if partner != small:  # perfect square: don't add the root twice
                    divisors.append(partner)
        return sorted(divisors)


if __name__ == "__main__":
    solution = Solution()
    cases = {1: [1], 2: [1, 2], 12: [1, 2, 3, 4, 6, 12], 36: [1, 2, 3, 4, 6, 9, 12, 18, 36],
             13: [1, 13], 100: [1, 2, 4, 5, 10, 20, 25, 50, 100]}
    for n, expected in cases.items():
        assert solution.divisors_brute_force(n) == expected, n
        assert solution.divisors_optimized(n) == expected, n
    print("all tests passed")
