class Solution:
    def secondLargestElementBruteForce(self, nums):
        if len(nums) < 2:
            return -1
        sorted_nums = sorted(nums)
        largest = sorted_nums[-1]
        second_largest = -1  # BUG: -1 sentinel is ambiguous when the array has negatives; use None
        for i in range(len(sorted_nums) - 1, -1, -1):
            if(sorted_nums[i] != largest):
                second_largest = sorted_nums[i]
                break
        return second_largest

    def secondLargestElementBetter(self, nums):
        if len(nums) < 2:
            return -1
        largest = nums[0]
        second_largest = -1  # BUG: -1 sentinel breaks for negatives, e.g. [-5, -2, -9] returns -1 instead of -5
        for index in range(len(nums)):
            if nums[index] > largest:
                largest = nums[index]

        for index in range(len(nums)):
            if(nums[index] > second_largest and nums[index] != largest):
                second_largest = nums[index]
        return second_largest

    def secondLargestElementOptimized(self, nums):
        if len(nums) < 2:
            return -1

        largest = nums[0]
        secondLargest = -1  # BUG: same -1 sentinel issue
        # BUG: method is unfinished (no loop, no return) -> returns None for every input

        