class Solution:
    def factorial(self, n):
        #Your code goes here
        # BUG REVIEW:
        # - Logic is correct for n >= 0 (base case n is 0 or 1, then n * factorial(n-1)).
        # - Bug: n < 0 never hits the base case -> infinite recursion (RecursionError).
        #   Fix: raise ValueError for negative n (factorial is undefined there),
        #   or at least use `if n <= 1: return 1`.
        # - Limit: Python's recursion depth is ~1000, so n > ~990 raises RecursionError.
        #   For large n use a loop or math.factorial.
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)
