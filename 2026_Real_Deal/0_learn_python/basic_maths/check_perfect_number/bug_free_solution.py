"""Check Perfect Number: a positive integer is perfect if it equals the sum of its
proper divisors (divisors excluding itself). Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.
Zero and negative numbers are not perfect."""


class Solution:
    def perfect_brute_force(self, number: int) -> bool:
        """Try every i in [1, number). O(n) time, O(1) space."""
        if number <= 1:
            return False
        divisor_sum = 0
        for divisor in range(1, number):
            if number % divisor == 0:
                divisor_sum += divisor
        return divisor_sum == number

    def perfect_optimized(self, number: int) -> bool:
        """Collect divisor pairs (i, number // i) up to sqrt(number). O(sqrt n) time, O(1) space."""
        if number <= 1:
            return False
        divisor_sum = 1  # 1 divides everything and is always a proper divisor
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                divisor_sum += divisor
                partner = number // divisor
                if partner != divisor:  # avoid double counting perfect squares
                    divisor_sum += partner
            divisor += 1
        return divisor_sum == number


if __name__ == "__main__":
    solution = Solution()
    cases = {-6: False, 0: False, 1: False, 2: False, 4: False, 6: True, 12: False,
             28: True, 36: False, 100: False, 496: True, 8128: True, 8129: False}
    for value, expected in cases.items():
        assert solution.perfect_brute_force(value) == expected, value
        assert solution.perfect_optimized(value) == expected, value
    print("all tests passed")
