class Solution:
    def linearSearch(self, nums, target):
        # BUG: range(len(nums)-1) stops at index len-2, so the LAST element is never checked.
        #      e.g. nums=[1,2,3], target=3 returns -1 instead of 2. Fix: range(len(nums)).
        for i in range(len(nums)):
            if(nums[i] == target):
                return i
        return -1
