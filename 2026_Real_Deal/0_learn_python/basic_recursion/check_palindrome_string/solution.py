class Solution:
    def check_brute_force(self, s):
        """Build the reversed string and compare. O(n) time, O(n) space."""
        reversed_s = "".join(s[index] for index in range(len(s) - 1, -1, -1))
        return s == reversed_s

    def check_recursive(self, s):
        """Your approach: compare ends, recurse inward.
        O(n) time, O(n/2) stack. Fails for len > ~2000 (recursion limit)."""

        def helper(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return helper(left + 1, right - 1)

        return helper(0, len(s) - 1)

    def check_optimized(self, s):
        """Two-pointer loop, same comparisons without recursion.
        O(n) time, O(1) space, no stack growth."""
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    cases = ["", "a", "ab", "aa", "aba", "abba", "abca", "racecar", "hello", "a" * 500]
    for text in cases:
        expected = text == text[::-1]
        assert sol.check_brute_force(text) == sol.check_recursive(text) == sol.check_optimized(text) == expected
    big = "ab" * 50000 + "ba" * 50000
    assert sol.check_optimized(big) is True
    print("all ok")
