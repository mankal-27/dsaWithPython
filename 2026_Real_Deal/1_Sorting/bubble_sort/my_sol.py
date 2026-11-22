class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            isSwapped = False
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    isSwapped = True
            if not isSwapped:
                break
        return nums