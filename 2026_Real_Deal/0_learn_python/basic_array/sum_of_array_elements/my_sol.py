class Solution:
    def sumOfArrayElement(self, arr):
        # No functional bug: correct for [], negatives, and any length.
        # Style notes: range(len(arr)) + arr[i] works, but `for value in arr` is more Pythonic.
        total = 0
        for i in range(len(arr)):
            total = total + arr[i]
        return total

    def sumOfArrayElementInBuilt(self, arr):
        return sum(arr)

# Note: these lines run on import; prefer `if __name__ == "__main__":` (see bug_free_solution.py)
s = Solution()
arr = [1,2,3]
print(s.sumOfArrayElement(arr))
print(s.sumOfArrayElementInBuilt(arr))