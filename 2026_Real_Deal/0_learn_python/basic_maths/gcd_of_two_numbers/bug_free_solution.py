"""GCD of Two Numbers: largest integer that divides both numbers."""


class Solution:
    def gcd_brute_force(self, num1: int, num2: int) -> int:
        """Try every candidate from min down to 1. O(min(a, b)) time, O(1) space."""
        num1, num2 = abs(num1), abs(num2)
        if num1 == 0 or num2 == 0:
            return num1 + num2  # gcd(a, 0) = a
        for divisor in range(min(num1, num2), 0, -1):  # first hit is the largest
            if num1 % divisor == 0 and num2 % divisor == 0:
                return divisor
        return 1

    def gcd_optimized(self, num1: int, num2: int) -> int:
        """Euclid: gcd(a, b) = gcd(b, a % b). O(log min(a, b)) time, O(1) space."""
        num1, num2 = abs(num1), abs(num2)
        while num2:
            num1, num2 = num2, num1 % num2
        return num1


if __name__ == "__main__":
    solution = Solution()
    cases = {(12, 18): 6, (4, 8): 4, (7, 13): 1, (5, 5): 5, (0, 9): 9, (9, 0): 9,
             (1, 100): 1, (100, 75): 25, (-12, 18): 6, (48, 180): 12}
    for (a, b), expected in cases.items():
        assert solution.gcd_brute_force(a, b) == expected, (a, b)
        assert solution.gcd_optimized(a, b) == expected, (a, b)
    print("all tests passed")
