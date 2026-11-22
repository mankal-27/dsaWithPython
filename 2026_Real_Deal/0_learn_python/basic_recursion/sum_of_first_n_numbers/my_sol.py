class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        # BUG REVIEW:
        # - Logic is correct for N >= 0 (base case N == 0, then N + sum(N-1)).
        # - Bug: N < 0 never hits the base case -> infinite recursion (RecursionError).
        #   Fix: use `if N <= 0: return 0`.
        # - Limit: Python's recursion depth is ~1000, so N > ~990 raises RecursionError.
        #   For large N use the formula N * (N + 1) // 2 or a loop.
        if N == 0:
            return 0
        return N + self.NnumbersSum(N - 1)
