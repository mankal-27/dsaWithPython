"""Count Odd Digits: return how many digits of an integer are odd (sign ignored)."""


class Solution:
    ODD_DIGITS = set("13579")

    def count_odd_digits_brute_force(self, number: int) -> int:
        """Convert to a string and test every character. O(d) time, O(d) space."""
        odd_count = 0
        for digit_char in str(abs(number)):
            if digit_char in self.ODD_DIGITS:
                odd_count += 1
        return odd_count

    def count_odd_digits_optimized(self, number: int) -> int:
        """Peel digits with % and //. O(d) time, O(1) space."""
        number = abs(number)          # negatives would skip the loop otherwise
        odd_count = 0
        while number > 0:             # number == 0 naturally returns 0
            last_digit = number % 10
            if last_digit & 1:        # same as last_digit % 2 == 1
                odd_count += 1
            number //= 10
        return odd_count


if __name__ == "__main__":
    solution = Solution()
    cases = {12345: 3, 0: 0, -135: 3, 2468: 0, 9: 1, 10**20 + 1: 2}
    for value, expected in cases.items():
        assert solution.count_odd_digits_brute_force(value) == expected, value
        assert solution.count_odd_digits_optimized(value) == expected, value
    print("all tests passed")
