"""Check Palindrome Number: is an integer the same read forwards and backwards?
Negative numbers are never palindromes ('-' has no match at the end)."""


class Solution:
    def is_palindrome_brute_force(self, number: int) -> bool:
        """Compare the string with its reverse. O(d) time, O(d) space."""
        if number < 0:
            return False
        text = str(number)
        return text == text[::-1]

    def reverse_number(self, number: int) -> int:
        """Reverse a non-negative integer using % and //. O(d) time, O(1) space."""
        reversed_number = 0
        while number > 0:
            last_digit = number % 10
            reversed_number = reversed_number * 10 + last_digit
            number //= 10
        return reversed_number

    def is_palindrome_optimized(self, number: int) -> bool:
        """Reverse the digits mathematically and compare. O(d) time, O(1) space."""
        if number < 0:
            return False
        return self.reverse_number(number) == number


if __name__ == "__main__":
    solution = Solution()
    cases = {121: True, 123: False, 0: True, -121: False, 10: False,
             7: True, 1221: True, 10**20 + 1: True, 10**20 + 2: False}
    for value, expected in cases.items():
        assert solution.is_palindrome_brute_force(value) == expected, value
        assert solution.is_palindrome_optimized(value) == expected, value
    print("all tests passed")
