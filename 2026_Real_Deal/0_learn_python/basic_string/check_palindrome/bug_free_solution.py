class Solution:
    def check_palindrome_brute_force(self, text):
        """Build the reversed string and compare. O(n) time, O(n) extra space."""
        reversed_text = ""
        for index in range(len(text) - 1, -1, -1):
            reversed_text += text[index]
        return text == reversed_text

    def check_palindrome_optimized(self, text):
        """Two pointers moving inward, compare each pair. O(n) time, O(1) extra space."""
        left, right = 0, len(text) - 1
        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    cases = [
        ("racecar", True), ("abba", True), ("hello", False), ("ab", False),
        ("a", True), ("", True), ("aa", True), ("abca", False),
    ]
    for text, expected in cases:
        for method in (solution.check_palindrome_brute_force, solution.check_palindrome_optimized):
            assert method(text) == expected, (method.__name__, text)
    print("All tests passed")
