class Solution:
    def bubbleSort(self, nums):
        self.helper(nums, len(nums))
        return nums

    def helper(self, nums, n):
        # BUG 2: n == 1 misses n == 0 (empty list) -> recurses forever (RecursionError). Use n <= 1.
        if n == 1:
            return
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[ i + 1] = nums[ i + 1], nums[1]  # BUG 1: RHS should be nums[i], not nums[1] (corrupts array)
        self.helper(nums, n-1)