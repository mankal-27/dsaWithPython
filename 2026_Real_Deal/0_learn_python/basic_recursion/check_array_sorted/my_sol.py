class Solution:
    def isSorted(self, nums):
        #your code goes here
        # BUG REVIEW: logic is correct (empty, single, equal neighbours all fine).
        # Only issue: recursion depth is n-1, so len(nums) > ~1000 -> RecursionError.
        # Use the loop version in solution.py (check_optimized) for large inputs.
        if len(nums) <= 1:
            return True
        def helper(i):
            if i == len(nums) - 1:
                return True
            if nums[i] > nums[i + 1]:
                return False
            return helper( i + 1)
        return helper(0)
