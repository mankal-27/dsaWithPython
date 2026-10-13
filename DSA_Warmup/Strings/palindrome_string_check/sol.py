class Solution:
    def palindrome_check_reverse_and_compare(self, s):
        reversed_char = []
        for i in range(len(s) - 1, -1, -1):
            reversed_char.append(s[i])
        reversed_s = "".join(reversed_char)
        return s == reversed_s

    def palindrome_check_two_pointers(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindrome_check_builtin_slice(self, s):
        return s == s[::-1]
