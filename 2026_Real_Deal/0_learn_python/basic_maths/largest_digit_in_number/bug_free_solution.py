"""Largest Digit in a Number: return the biggest digit of an integer.
Negative numbers use their absolute value (-472 -> 7)."""


class Solution:
    def largest_digit_brute_force(self, number: int) -> int:
        """Convert to a string and take the max character. O(d) time, O(d) space."""
        return int(max(str(abs(number))))

    def largest_digit_optimized(self, number: int) -> int:
        """Peel digits with % and //, tracking the max. O(d) time, O(1) space."""
        number = abs(number)
        largest_digit = 0
        while number > 0:
            last_digit = number % 10
            if last_digit > largest_digit:
                largest_digit = last_digit
                if largest_digit == 9:  # cannot get bigger, stop early
                    break
            number //= 10
        return largest_digit


if __name__ == "__main__":
    solution = Solution()
    cases = {472: 7, 9: 9, 0: 0, 1000: 1, 12345: 5, 99: 9, -472: 7, 10**20 + 5: 5}
    for value, expected in cases.items():
        assert solution.largest_digit_brute_force(value) == expected, value
        assert solution.largest_digit_optimized(value) == expected, value
    print("all tests passed")
