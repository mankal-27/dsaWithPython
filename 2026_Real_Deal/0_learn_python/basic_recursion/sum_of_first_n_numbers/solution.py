class Solution:
    def sum_brute_force(self, n):
        """Iterative loop: add 1..n one by one. O(n) time, O(1) space."""
        total = 0
        for number in range(1, n + 1):
            total += number
        return total

    def sum_recursive(self, n):
        """Your approach, fixed: n <= 0 is the base case (no infinite recursion).
        O(n) time, O(n) stack space. Fails for n > ~990 (recursion limit)."""
        if n <= 0:
            return 0
        return n + self.sum_recursive(n - 1)

    def sum_optimized(self, n):
        """Gauss formula: n * (n + 1) / 2. O(1) time, O(1) space."""
        if n <= 0:
            return 0
        return n * (n + 1) // 2


if __name__ == "__main__":
    s = Solution()
    for n in [0, 1, 4, 10, 100, -3]:
        assert s.sum_brute_force(n) == s.sum_recursive(n) == s.sum_optimized(n)
        print(n, s.sum_optimized(n))
    print(s.sum_optimized(10**6))
