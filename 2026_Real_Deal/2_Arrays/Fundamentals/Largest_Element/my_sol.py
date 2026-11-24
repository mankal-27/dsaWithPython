class Solution:
    def largestElementBruteForce(self, nums):
        # BUG: nums.sort() sorts the caller's list in place (side effect: input is mutated).
        #      Fix: use sorted(nums)[-1] or work on a copy.
        # BUG: empty list -> IndexError on nums[-1]. Fix: guard for empty input.
        nums.sort()
        return nums[-1]

    def largestElementOptimized(self, nums):
        # BUG: empty list -> IndexError on nums[0]. Fix: guard for empty input.
        # NOTE: loop starts at i=0 and compares nums[0] with itself (harmless, one wasted step); start at 1.
        largest = nums[0]
        for i in range(len(nums)):
            if (nums[i] > largest):
                largest = nums[i]
        return largest
