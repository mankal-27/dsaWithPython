class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)
        # BUG 1: if nums is empty, n == 0 and `k % n` raises ZeroDivisionError. Guard with `if n == 0: return`.
        k = k % n

        temp = []

        for i in range(k):
            temp.append(nums[i])

        for i in range(k, n):
            nums[i-k] = nums[i]

        for i in range(k):
            
            nums[n-k+i] = temp[i]
        # BUG 3 (minor): nothing is returned; add `return nums` if the judge expects a result.
