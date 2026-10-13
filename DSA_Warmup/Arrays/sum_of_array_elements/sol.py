class Solution:
    def sum_of_array_elements_linear_scan(self, nums):
        total = 0
        for num in nums:
            total += num
        return total

    def sum_of_array_elements_builtin_sum(self, nums):
        return sum(nums)
