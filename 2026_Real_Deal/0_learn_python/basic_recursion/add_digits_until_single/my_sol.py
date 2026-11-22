class Solution:
    def addDigits(self, num):
        #your code goes here
        if num < 10:
            return num
        total = 0
        while num > 0:
            lastDigit = num % 10
            total = total + lastDigit
            num //= 10
        return self.addDigits(total)

# BUG REVIEW:
# 1. Correct for num >= 0 (the problem's constraint).
# 2. num < 0: `while num > 0` never runs, total = 0, returns 0 (silently wrong). Guard or use abs().
# 3. Digit sum is a loop; only the "repeat" is recursive. Fine, but the digit sum itself
#    can be recursive (num % 10 + f(num // 10)) if the topic demands pure recursion.
# 4. Missing `return` type/edge: num == 0 is handled by `num < 10` (ok).
