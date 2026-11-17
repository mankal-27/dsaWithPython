# Review: no logic bugs. Compares every pair (i, j) with j > i, so it is correct
# but O(n^2) time: this is the brute force. Equal neighbours are allowed
# (non-decreasing), and empty / single-element arrays correctly return True.
# Style only: drop the parentheses in `if (...)` and write `i + 1` with spaces.
class Solution:
    def isSortedArray(self, arr):
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i] :
                    return False
        return True
