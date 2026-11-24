from typing import List, Optional


class Solution:
    def largestElementBruteForce(self, nums: List[int]) -> Optional[int]:
        """Sort a copy, take the last element. O(n log n) time, O(n) space."""
        if not nums:
            return None
        sorted_nums = sorted(nums)  # copy: caller's list is not mutated
        return sorted_nums[-1]

    def largestElementOptimized(self, nums: List[int]) -> Optional[int]:
        """Single pass keeping a running maximum. O(n) time, O(1) space."""
        if not nums:
            return None
        largest = nums[0]
        for index in range(1, len(nums)):  # nums[0] already used
            if nums[index] > largest:
                largest = nums[index]
        return largest


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([3, 1, 4, 1, 5], 5),
        ([7], 7),
        ([-5, -2, -9], -2),
        ([2, 2, 2], 2),
        ([9, 1, 2], 9),
        ([1, 2, 9], 9),
        ([], None),
    ]
    for nums, expected in cases:
        original = list(nums)
        assert s.largestElementBruteForce(nums) == expected, nums
        assert nums == original, "input was mutated"
        assert s.largestElementOptimized(nums) == expected, nums
    print("All tests passed")
