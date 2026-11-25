from typing import List


class Solution:
    def maxConsecutiveOnesBruteForce(self, nums: List[int]) -> int:
        """From every index, extend a run of 1s as far as possible.
        O(n^2) time (all-ones input), O(1) space."""
        longest_run = 0
        for start in range(len(nums)):
            run_length = 0
            index = start
            while index < len(nums) and nums[index] == 1:
                run_length += 1
                index += 1
            longest_run = max(longest_run, run_length)
        return longest_run

    def maxConsecutiveOnesOptimized(self, nums: List[int]) -> int:
        """Single pass: grow the current run on 1, reset on 0.
        O(n) time, O(1) space."""
        current_run = 0
        longest_run = 0
        for value in nums:
            if value == 1:
                current_run += 1
                longest_run = max(longest_run, current_run)
            else:
                current_run = 0
        return longest_run
