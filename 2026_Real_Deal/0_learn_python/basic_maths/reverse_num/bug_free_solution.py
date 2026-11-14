"""Reverse Number: reverse the digits of an integer (sign kept, trailing zeros dropped)."""


class Solution:
    def reverse_num_brute_force(self, number: int) -> int:
        """Reverse the string form. O(d) time, O(d) space."""
        sign = -1 if number < 0 else 1
        reversed_text = str(abs(number))[::-1]
        return sign * int(reversed_text)

    def reverse_num_optimized(self, number: int) -> int:
        """Peel digits with % and //, rebuild reversed. O(d) time, O(1) space."""
        sign = -1 if number < 0 else 1
        number = abs(number)
        reversed_number = 0
        while number > 0:
            last_digit = number % 10
            reversed_number = reversed_number * 10 + last_digit
            number //= 10
        return sign * reversed_number


if __name__ == "__main__":
    solution = Solution()
    cases = {123: 321, 120: 21, 0: 0, -123: -321, 7: 7, 10**20 + 1: 10**20 + 1}
    for value, expected in cases.items():
        assert solution.reverse_num_brute_force(value) == expected, value
        assert solution.reverse_num_optimized(value) == expected, value
    print("all tests passed")
