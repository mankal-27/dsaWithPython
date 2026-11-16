"""LCM of Two Numbers: smallest positive integer divisible by both numbers."""


class Solution:
    def lcm_brute_force(self, num1: int, num2: int) -> int:
        """Try multiples of the larger number. O(a * b / gcd) time, O(1) space."""
        num1, num2 = abs(num1), abs(num2)
        if num1 == 0 or num2 == 0:
            return 0  # lcm with 0 is defined as 0
        larger = max(num1, num2)
        candidate = larger
        while candidate % num1 != 0 or candidate % num2 != 0:
            candidate += larger  # only multiples of the larger can qualify
        return candidate

    def lcm_optimized(self, num1: int, num2: int) -> int:
        """lcm(a, b) = a / gcd(a, b) * b. O(log min(a, b)) time, O(1) space."""
        num1, num2 = abs(num1), abs(num2)
        if num1 == 0 or num2 == 0:
            return 0
        return num1 // self._gcd(num1, num2) * num2  # divide first to keep numbers small

    def _gcd(self, num1: int, num2: int) -> int:
        while num2:
            num1, num2 = num2, num1 % num2
        return num1


if __name__ == "__main__":
    solution = Solution()
    cases = {(4, 6): 12, (12, 18): 36, (7, 13): 91, (5, 5): 5, (0, 9): 0,
             (1, 100): 100, (4, 8): 8, (-4, 6): 12, (21, 6): 42}
    for (a, b), expected in cases.items():
        assert solution.lcm_brute_force(a, b) == expected, (a, b)
        assert solution.lcm_optimized(a, b) == expected, (a, b)
    print("all tests passed")
