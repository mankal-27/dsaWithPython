class Solution:
    def reverseString(self,s):
        #your code goes here
        char = list(s)

        def helper(left, right):
            if left >= right:
                return
            char[left], char[right] = char[right], char[left]
            helper(left+1, right-1)
        helper(0, len(char) - 1)
        return "".join(char)