"""Factorial of a Number: return n! = 1 * 2 * ... * n, with 0! = 1.
Negative numbers have no factorial, so they raise ValueError."""


class Solution:
    def factorial_brute_force(self, number: int) -> int:
        """Recursive: n! = n * (n-1)!. O(n) time, O(n) space (call stack)."""
        if number < 0:
            raise ValueError("factorial is undefined for negative numbers")
        if number <= 1:  # base case: 0! = 1! = 1
            return 1
        return number * self.factorial_brute_force(number - 1)

    def factorial_optimized(self, number: int) -> int:
        """Iterative product of 1..n. O(n) time, O(1) extra space."""
        if number < 0:
            raise ValueError("factorial is undefined for negative numbers")
        result = 1
        for multiplier in range(2, number + 1):  # 1 never changes the product
            result *= multiplier
        return result


if __name__ == "__main__":
    solution = Solution()
    cases = {0: 1, 1: 1, 2: 2, 3: 6, 5: 120, 10: 3628800, 20: 2432902008176640000}
    for value, expected in cases.items():
        assert solution.factorial_brute_force(value) == expected, value
        assert solution.factorial_optimized(value) == expected, value
    for solver in (solution.factorial_brute_force, solution.factorial_optimized):
        try:
            solver(-3)
            raise AssertionError("expected ValueError")
        except ValueError:
            pass
    print("all tests passed")
