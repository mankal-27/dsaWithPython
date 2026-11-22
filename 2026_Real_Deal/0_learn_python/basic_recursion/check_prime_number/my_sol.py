class Solution:
    def checkPrime(self, num):
        #your code goes here
        if num <= 1:
            return False
        def helper(i):
            if i * i > num:
                return True
            if num % i == 0:
                return False
            return helper(i + 1)
        return helper(2)
# BUG REVIEW:
# - Logic is correct (num <= 1 -> False; 2 and 3 -> True; trial division up to sqrt).
# - Recursion depth is ~sqrt(num). For num > ~1,000,000 (prime) this hits Python's
#   recursion limit (~1000) -> RecursionError. See solution.py for a safe version.
