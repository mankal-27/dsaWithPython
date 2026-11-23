class Solution:
    def insertionSortBruteForce(self, nums):
        """Brute force: insert each item by swapping it left, one adjacent
        swap at a time, until it meets a smaller-or-equal item.
        O(n^2) time, O(1) space (3 writes per step)."""
        n = len(nums)
        for i in range(1, n):
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
        return nums

    def insertionSortOptimized(self, nums):
        """Optimized: hold the item as `key`, shift bigger items right by one
        (1 write per step), then drop `key` into the gap.
        O(n^2) worst, O(n) best (sorted), O(1) space, stable."""
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums
