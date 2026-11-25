class Solution:
    def rotateArrayByOne(self, nums):
        if len(nums) == 0: return
        temp = nums[0]
        for i in range(1, len(nums)):
            nums[i-1] = nums[i]
        nums[-1] = temp
