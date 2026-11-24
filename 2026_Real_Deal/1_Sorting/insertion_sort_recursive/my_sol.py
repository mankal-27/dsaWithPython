class Solution:
    def insertionSort(self, nums):
        self.helper(nums, len(nums))
        return nums

    def helper(self, nums, size):
                # BUG: helper has no body -> IndentationError/SyntaxError, file won't even import.
        # Needs: base case `if size <= 1: return`, recurse `self.helper(nums, size - 1)`
        # to sort the first size-1 items, then insert nums[size-1] into that sorted prefix.
