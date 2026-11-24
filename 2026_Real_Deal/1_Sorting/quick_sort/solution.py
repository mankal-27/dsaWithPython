import random


class Solution:
    # ---------- Brute force: build new lists around the pivot ----------
    def quickSortBruteForce(self, nums):
        if len(nums) <= 1:
            return nums[:]
        pivot = nums[len(nums) // 2]
        smaller = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        larger = [x for x in nums if x > pivot]
        return self.quickSortBruteForce(smaller) + equal + self.quickSortBruteForce(larger)

    # ---------- Optimized: in-place partition on index ranges ----------
    def quickSortOptimized(self, nums):
        self.sortRange(nums, 0, len(nums) - 1)
        return nums

    def sortRange(self, nums, low, high):
        while low < high:
            pivot_index = self.partition(nums, low, high)
            # recurse on the smaller side, loop on the larger: stack stays O(log n)
            if pivot_index - low < high - pivot_index:
                self.sortRange(nums, low, pivot_index - 1)
                low = pivot_index + 1
            else:
                self.sortRange(nums, pivot_index + 1, high)
                high = pivot_index - 1

    def partition(self, nums, low, high):
        # random pivot avoids O(n^2) on already sorted input
        random_index = random.randint(low, high)
        nums[random_index], nums[high] = nums[high], nums[random_index]
        pivot = nums[high]
        boundary = low  # everything before boundary is < pivot
        for scan in range(low, high):
            if nums[scan] < pivot:
                nums[scan], nums[boundary] = nums[boundary], nums[scan]
                boundary += 1
        nums[boundary], nums[high] = nums[high], nums[boundary]  # pivot to its final spot
        return boundary
