class Solution:
    def reverseAString(self, str):
        # BUG 1: right = len(str) is one past the last index -> IndexError on the first swap.
        #        Fix: right = len(str) - 1
        left , right = 0, len(str) - 1

        while(left < right):
            # BUG 2: Python strings are immutable, so str[left] = ... raises TypeError.
            #        Fix: convert to a list first (list(s)) and join at the end.
            str[left], str[right] = str[right], str[left]
            left += 1
            right -= 1
        # BUG 3 (follow-on): returns the input type; a list would need "".join(...) to give a string back.
        return str
