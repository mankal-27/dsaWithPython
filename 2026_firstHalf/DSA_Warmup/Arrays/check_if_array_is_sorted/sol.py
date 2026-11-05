class Solution:
    def is_sorted_adjacent_comparison(self, nums):
        if(len(nums) <= 1):
            return True
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i+1]):
                return False
        return True

    def is_sorted_builtin_all_zip(self, nums):
        return all(a <= b for a, b in zip(nums, nums[1:]))
