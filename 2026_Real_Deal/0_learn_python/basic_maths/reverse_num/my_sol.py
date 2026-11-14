class Solution:
    # BUG 1: missing `self` -> Solution().reverse_num(123) raises TypeError
    #        (only works if called as Solution.reverse_num(123)).
    # BUG 2: `while(num > 0)` skips negatives, so -123 returns 0 instead of -321.
    def reverse_num(self,num):
        reversedNum = 0
        while(num > 0):
            lastDigit = num % 10
            reversedNum = (reversedNum * 10) + lastDigit
            num //= 10
        return reversedNum

    # BUG 3: missing `self`.
    # BUG 4: reversed() needs a sequence; reversed(123) raises TypeError.
    #        Even on a string it returns an iterator, not a number.
    #        Fix: int(str(num)[::-1]).
    def reverseNumWithMethod(self,num):
        return reversed(num)
