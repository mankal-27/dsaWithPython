class Solution:
    def bubbleSortBruteForce(self, nums):
        """Brute force recursive: always recurse n-1 times, no early exit.
        O(n^2) time, O(n) recursion stack."""
        self._bruteHelper(nums, len(nums))
        return nums

    def _bruteHelper(self, nums, size):
        if size <= 1:  # also covers the empty list
            return
        for j in range(size - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        self._bruteHelper(nums, size - 1)

    def bubbleSortOptimized(self, nums):
        """Optimized recursive: stop recursing when a pass swaps nothing.
        O(n^2) worst, O(n) best, O(n) recursion stack worst case."""
        self._optimizedHelper(nums, len(nums))
        return nums

    def _optimizedHelper(self, nums, size):
        if size <= 1:
            return
        swapped = False
        for j in range(size - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            return
        self._optimizedHelper(nums, size - 1)
