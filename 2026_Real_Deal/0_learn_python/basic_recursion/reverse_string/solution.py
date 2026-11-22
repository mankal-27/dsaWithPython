class Solution:
    def reverse_brute_force(self, s):
        """Loop from last index to 0, collecting chars. O(n) time, O(n) space."""
        result = []
        for index in range(len(s) - 1, -1, -1):
            result.append(s[index])
        return "".join(result)

    def reverse_recursive(self, s):
        """Your approach: swap ends, recurse inward.
        O(n) time, O(n) list + O(n/2) stack. Fails for len > ~2000 (recursion limit)."""
        chars = list(s)

        def helper(left, right):
            if left >= right:
                return
            chars[left], chars[right] = chars[right], chars[left]
            helper(left + 1, right - 1)

        helper(0, len(chars) - 1)
        return "".join(chars)

    def reverse_optimized(self, s):
        """Two-pointer loop, same swaps without recursion.
        O(n) time, O(n) space (list copy), O(1) stack."""
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)


if __name__ == "__main__":
    sol = Solution()
    for text in ["", "a", "ab", "abc", "hello", "racecar", "a" * 500]:
        assert sol.reverse_brute_force(text) == sol.reverse_recursive(text) == sol.reverse_optimized(text) == text[::-1]
    big = "xy" * 50000
    assert sol.reverse_optimized(big) == big[::-1]
    print("all ok")
