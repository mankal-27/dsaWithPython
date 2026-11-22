class Solution:
    def bubbleSortBruteForce(self, nums):
        """Brute force: n-1 full passes, always, swapping adjacent
        out-of-order pairs. O(n^2) time, O(1) space."""
        n = len(nums)
        for _ in range(n - 1):
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def bubbleSortOptimized(self, nums):
        """Optimized: each pass shrinks (the largest items bubble to the end)
        and we stop early if a pass swaps nothing.
        O(n^2) worst, O(n) best, O(1) space."""
        n = len(nums)
        for last in range(n - 1, 0, -1):
            swapped = False
            for j in range(last):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
