class Solution:
    def linear_search_scan(self, nums, target):
        for i in range(len(nums)):
            if(nums[i] == target):
                return i
        return -1

    def linear_search_builtin_index(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            return -1
