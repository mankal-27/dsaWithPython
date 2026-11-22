class Solution:
    def fib_brute_force(self, n):
        """Your approach: plain recursion. O(2^n) time, O(n) stack."""
        self._check(n)
        if n <= 1:
            return n
        return self.fib_brute_force(n - 1) + self.fib_brute_force(n - 2)

    def fib_memo(self, n):
        """Recursion + cache. O(n) time, O(n) space."""
        self._check(n)
        cache = {0: 0, 1: 1}

        def helper(k):
            if k not in cache:
                cache[k] = helper(k - 1) + helper(k - 2)
            return cache[k]

        return helper(n)

    def fib_optimized(self, n):
        """Iterate with two variables. O(n) time, O(1) space, no recursion limit."""
        self._check(n)
        previous, current = 0, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous

    def _check(self, n):
        if n < 0:
            raise ValueError("n must be >= 0")


if __name__ == "__main__":
    s = Solution()
    for n in range(0, 20):
        assert s.fib_brute_force(n) == s.fib_memo(n) == s.fib_optimized(n)
    assert s.fib_optimized(10) == 55
    assert s.fib_optimized(90) == 2880067194370816120
    print("all ok")
