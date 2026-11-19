"""2520. Count the Digits That Divide a Number.

Constraints: 1 <= num <= 10^9, and num contains no 0 digit.
"""


class Solution:
    def count_digits_brute_force(self, num: int) -> int:
        """Convert to a string and test every character. O(d) time, O(d) space."""
        divisor_count = 0
        for digit_char in str(num):
            if num % int(digit_char) == 0:
                divisor_count += 1
        return divisor_count

    def count_digits_optimized(self, num: int) -> int:
        """Peel digits with % and //, keeping the original. O(d) time, O(1) space."""
        original = num                # FIX: num shrinks, so remember the full value
        divisor_count = 0
        while num > 0:
            last_digit = num % 10
            if original % last_digit == 0:
                divisor_count += 1
            num //= 10
        return divisor_count


if __name__ == "__main__":
    solution = Solution()
    cases = {7: 1, 121: 2, 1248: 4, 12: 2, 15: 2, 24: 2, 1122: 4, 999999999: 9}
    for value, expected in cases.items():
        assert solution.count_digits_brute_force(value) == expected, value
        assert solution.count_digits_optimized(value) == expected, value
    print("all tests passed")
