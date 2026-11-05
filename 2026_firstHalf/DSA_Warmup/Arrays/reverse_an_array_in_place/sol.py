class Solution:
    def reverse_array_two_pointers(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def reverse_array_builtin_reverse(self, nums):
        nums.reverse()
        return nums
