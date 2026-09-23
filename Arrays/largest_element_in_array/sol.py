class Solution:
    def largest_element_linear_scan(self, nums):
        largest = nums[0]
        for i in range(1, len(nums) ):
            if(nums[i] > largest):
                largest = nums[i]
        return largest

    def largest_element_builtin_max(self, nums):
        return max(nums)
