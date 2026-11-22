class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        # BUG REVIEW: logic is correct (empty, 1 char, odd/even lengths all work).
        # Only issue: recursion depth is n/2, so len(s) > ~2000 -> RecursionError.
        # Fix: use the two-pointer loop in solution.py (check_optimized).
        def helper(left, right):
            if left >= right:
                return True
            if(s[left] != s[right]):
                return False
            return helper(left + 1, right - 1)
        return helper(0, len(s) - 1)
