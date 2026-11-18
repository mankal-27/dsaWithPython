class Solution:
    def reverse_string_brute_force(self, s):
        """Copy the characters out in reverse, then write them back. O(n) time, O(n) extra space.
        Modifies s in place; returns nothing."""
        reversed_copy = []
        for index in range(len(s) - 1, -1, -1):
            reversed_copy.append(s[index])
        for index in range(len(s)):
            s[index] = reversed_copy[index]

    def reverse_string_optimized(self, s):
        """Two pointers swapping in place. O(n) time, O(1) extra space.
        Modifies s in place; returns nothing."""
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = Solution()
    cases = [("hello", "olleh"), ("ab", "ba"), ("a", "a"), ("", ""), ("abcd", "dcba"), ("racecar", "racecar")]
    for text, expected in cases:
        for method in (solution.reverse_string_brute_force, solution.reverse_string_optimized):
            s = list(text)
            result = method(s)
            assert result is None, "must not return anything"
            assert "".join(s) == expected, (text, s)
    print("All tests passed")
