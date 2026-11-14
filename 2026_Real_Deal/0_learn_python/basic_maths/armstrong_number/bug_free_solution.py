"""Armstrong Number: a number is Armstrong if the sum of each digit raised to the
power of the digit count equals the number itself (153 = 1^3 + 5^3 + 3^3).
Negative numbers are not Armstrong numbers."""


class Solution:
    def armstrong_brute_force(self, number: int) -> bool:
        """Convert to string, power each digit. O(d) time, O(d) space (d = digits)."""
        if number < 0:
            return False
        digits = str(number)
        digit_count = len(digits)
        total = sum(int(char) ** digit_count for char in digits)
        return total == number

    def armstrong_optimized(self, number: int) -> bool:
        """Peel digits with % and //, integer powers only. O(d) time, O(1) space."""
        if number < 0:
            return False
        digit_count = self._count_digits(number)
        remaining = number
        total = 0
        while remaining > 0:
            total += (remaining % 10) ** digit_count
            remaining //= 10
        return total == number

    def _count_digits(self, number: int) -> int:
        if number == 0:
            return 1
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count


if __name__ == "__main__":
    solution = Solution()
    cases = {0: True, 1: True, 9: True, 10: False, 153: True, 154: False,
             370: True, 371: True, 407: True, 1634: True, 9474: True,
             9475: False, 548834: True, -153: False}
    for value, expected in cases.items():
        assert solution.armstrong_brute_force(value) == expected, value
        assert solution.armstrong_optimized(value) == expected, value
    print("all tests passed")
