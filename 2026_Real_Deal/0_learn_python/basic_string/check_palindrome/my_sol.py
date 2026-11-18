class Solution:
    def checkPalindrome(self, str):
        left , right = 0, len(str) - 1

        while(left < right):
            if(str[left] != str[right]):
                return False
            left += 1
            right -= 1
        return True
# STYLE: parameter `str` shadows the built-in; `while(...)`/`if(...)` parentheses and
# `left , right` spacing are not idiomatic; use snake_case method name.