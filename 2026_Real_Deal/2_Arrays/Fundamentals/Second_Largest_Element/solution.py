from typing import List


class Solution:
    def secondLargestElementBruteForce(self, nums: List[int]) -> int:
        """Sort a copy, scan from the end for the first value != largest.
        O(n log n) time, O(n) space. Returns -1 if no second largest exists."""
        if len(nums) < 2:
            return -1
        sorted_nums = sorted(nums)  # copy: caller's list is not mutated
        largest = sorted_nums[-1]
        for index in range(len(sorted_nums) - 2, -1, -1):
            if sorted_nums[index] != largest:
                return sorted_nums[index]
        return -1  # all elements equal

    def secondLargestElementBetter(self, nums: List[int]) -> int:
        """Pass 1 finds largest, pass 2 finds the max value below it.
        O(n) time (2 passes), O(1) space. Returns -1 if no second largest exists."""
        if len(nums) < 2:
            return -1
        largest = max(nums)
        second_largest = None  # None internally: -1 can be a real element
        for value in nums:
            if value != largest and (second_largest is None or value > second_largest):
                second_largest = value
        return -1 if second_largest is None else second_largest

    def secondLargestElementOptimized(self, nums: List[int]) -> int:
        """Single pass tracking the top two distinct values.
        O(n) time, O(1) space. Returns -1 if no second largest exists."""
        if len(nums) < 2:
            return -1
        largest = nums[0]
        second_largest = None  # None internally: -1 can be a real element
        for index in range(1, len(nums)):
            value = nums[index]
            if value > largest:
                second_largest = largest
                largest = value
            elif value < largest and (second_largest is None or value > second_largest):
                second_largest = value
        return -1 if second_largest is None else second_largest


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([3, 1, 4, 1, 5], 4),
        ([-5, -2, -9], -5),
        ([5, 5, 5], -1),
        ([1, 2], 1),
        ([2, 1], 1),
        ([7], -1),
        ([], -1),
        ([1, 2, 3, 4, 5], 4),
        ([5, 4, 3, 2, 1], 4),
        ([5, 5, 4], 4),
        ([0, -1], -1),
        ([1000, -1000], -1000),
        ([-1000, 1000], -1000),
        ([-1, -1], -1),
    ]
    for nums, expected in cases:
        original = list(nums)
        for method in (s.secondLargestElementBruteForce, s.secondLargestElementBetter, s.secondLargestElementOptimized):
            assert method(nums) == expected, (method.__name__, nums)
            assert nums == original, "input was mutated"
    print("All tests passed")
