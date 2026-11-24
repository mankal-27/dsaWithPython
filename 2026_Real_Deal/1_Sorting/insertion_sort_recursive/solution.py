class Solution:
    def insertionSortBruteForce(self, nums):
        """Recursive insertion sort, insert by repeated adjacent swaps.
        O(n^2) time, O(n) recursion stack."""
        self._sortPrefix(nums, len(nums))
        return nums

    def _sortPrefix(self, nums, size):
        if size <= 1:  # also covers the empty list
            return
        self._sortPrefix(nums, size - 1)         # first size-1 items now sorted
        self._swapDown(nums, size - 1)           # insert nums[size-1]

    def _swapDown(self, nums, index):
        if index <= 0 or nums[index - 1] <= nums[index]:
            return
        nums[index - 1], nums[index] = nums[index], nums[index - 1]
        self._swapDown(nums, index - 1)

    def insertionSortOptimized(self, nums):
        """Recursive insertion sort, insert by shifting (one write per step
        instead of a 2-element swap). O(n^2) worst, O(n) best, O(n) stack."""
        self._sortPrefixShift(nums, len(nums))
        return nums

    def _sortPrefixShift(self, nums, size):
        if size <= 1:
            return
        self._sortPrefixShift(nums, size - 1)
        self._shiftInsert(nums, size - 2, nums[size - 1])

    def _shiftInsert(self, nums, index, key):
        """Shift larger items right, drop key into the gap."""
        if index >= 0 and nums[index] > key:
            nums[index + 1] = nums[index]
            self._shiftInsert(nums, index - 1, key)
        else:
            nums[index + 1] = key
