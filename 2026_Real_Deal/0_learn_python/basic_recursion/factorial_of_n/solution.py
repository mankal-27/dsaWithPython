import math


class Solution:
    def factorial_brute_force(self, n):
        """Iterative loop: multiply 1..n one by one. O(n) time, O(1) space."""
        self._check_input(n)
        result = 1
        for number in range(2, n + 1):
            result *= number
        return result

    def factorial_recursive(self, n):
        """Your approach, fixed: negative n is rejected (no infinite recursion).
        O(n) time, O(n) stack space. Fails for n > ~990 (recursion limit)."""
        self._check_input(n)
        if n <= 1:
            return 1
        return n * self.factorial_recursive(n - 1)

    def factorial_optimized(self, n):
        """Library routine math.factorial (C implementation, no recursion limit,
        uses divide-and-conquer multiplication). Same O(n) multiplications, O(1) stack."""
        self._check_input(n)
        return math.factorial(n)

    def _check_input(self, n):
        if n < 0:
            raise ValueError("factorial is not defined for negative numbers")


if __name__ == "__main__":
    s = Solution()
    for n in [0, 1, 2, 5, 10, 20]:
        assert s.factorial_brute_force(n) == s.factorial_recursive(n) == s.factorial_optimized(n)
        print(n, s.factorial_optimized(n))
    assert s.factorial_brute_force(2000) == s.factorial_optimized(2000)
    try:
        s.factorial_recursive(-3)
    except ValueError as e:
        print("negative:", e)
