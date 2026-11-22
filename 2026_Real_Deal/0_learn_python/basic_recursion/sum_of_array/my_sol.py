class Solution:
    def arraySum(self, nums):
        #your code goes here
        # BUG REVIEW: logic is correct (empty list -> 0 too).
        # Only limitation: recursion depth == len(nums), so len(nums) > ~990
        # raises RecursionError in Python. Use a loop or sum() for big inputs.
        def helper(i):
            if i == len(nums):
                return 0
            return nums[i] + helper(i + 1)
        return helper(0)
