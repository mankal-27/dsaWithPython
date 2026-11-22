class Solution:
    def reverseArray(self, nums):
        #your code goes here
        def helper(left, right):
            if left >= right:
                return
            nums[left], nums[right] = nums[right], nums[left]
            helper(left + 1, right - 1)

        # BUG/NOTE 1: reverses `nums` in place (mutates the caller's list). Fine if intended, else copy first.
        # BUG/NOTE 2: recursion depth is n/2 -> RecursionError for len(nums) > ~2000.
        helper(0, len(nums) - 1)
        return nums