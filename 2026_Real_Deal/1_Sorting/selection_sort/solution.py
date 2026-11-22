class Solution:
    def selectionSortBruteForce(self, nums):
        """Brute force: repeatedly find the min of the remaining items,
        remove it and append to a NEW list. O(n^2) time, O(n) extra space."""
        remaining = list(nums)  # copy so the input is untouched
        sorted_nums = []
        while remaining:
            min_index = 0
            for j in range(1, len(remaining)):
                if remaining[j] < remaining[min_index]:
                    min_index = j
            sorted_nums.append(remaining.pop(min_index))
        return sorted_nums

    def selectionSortOptimized(self, nums):
        """Optimized: in-place selection sort. Grow a sorted prefix by swapping
        the minimum of the unsorted suffix into position i.
        O(n^2) time, O(1) extra space, at most n-1 swaps."""
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
