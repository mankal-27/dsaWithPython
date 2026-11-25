class Solution:
    def maxConsecutiveOnes(self, arr):
        count = 0
        maximumOnes = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                maximumOnes = max(count, maximumOnes)
            else:
                count = 0
        return maximumOnes

# Bug review: no bugs found. Handles [] (returns 0), all-zeros (0) and all-ones (n).
# Note: max() could be computed once at the end of each run instead of every 1,
# but that is only a micro-optimization; complexity is already O(n) time, O(1) space.
