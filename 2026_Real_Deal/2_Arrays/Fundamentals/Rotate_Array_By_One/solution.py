from typing import List


class Solution:
    def rotateArrayByOneBruteForce(self, nums: List[int]) -> List[int]:
        """Build a rotated copy and write it back into nums.
        O(n) time, O(n) space. Modifies nums in place and returns it."""
        if len(nums) <= 1:
            return nums
        rotated = nums[1:] + [nums[0]]
        for index in range(len(nums)):
            nums[index] = rotated[index]
        return nums

    def rotateArrayByOneOptimized(self, nums: List[int]) -> List[int]:
        """Save first element, shift the rest left, place saved value last.
        O(n) time, O(1) space. Modifies nums in place and returns it."""
        if len(nums) <= 1:
            return nums
        first_element = nums[0]
        for index in range(1, len(nums)):
            nums[index - 1] = nums[index]
        nums[-1] = first_element
        return nums
