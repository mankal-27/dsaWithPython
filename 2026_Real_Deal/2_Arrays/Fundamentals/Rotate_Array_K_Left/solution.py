from typing import List


class Solution:
    def rotateLeftByKBruteForce(self, nums: List[int], k: int) -> List[int]:
        """Rotate left one step at a time, k times.
        O(n * k) time, O(1) space. Modifies nums in place and returns it."""
        length = len(nums)
        if length <= 1:
            return nums
        k %= length
        for _ in range(k):
            first_element = nums[0]
            for index in range(1, length):
                nums[index - 1] = nums[index]
            nums[-1] = first_element
        return nums

    def rotateLeftByKOptimized(self, nums: List[int], k: int) -> List[int]:
        """Save first k elements, shift the rest left by k, append the saved ones.
        O(n) time, O(k) space. Modifies nums in place and returns it."""
        length = len(nums)
        if length <= 1:
            return nums
        k %= length
        if k == 0:
            return nums
        saved_elements = nums[:k]
        for index in range(k, length):
            nums[index - k] = nums[index]
        for offset in range(k):
            nums[length - k + offset] = saved_elements[offset]
        return nums
