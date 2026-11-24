from typing import List


class Solution:
    def linearSearchBruteForce(self, nums: List[int], target: int) -> int:
        """Index-based scan: check every index 0..n-1."""
        for index in range(len(nums)):  # len(nums), not len(nums)-1
            if nums[index] == target:
                return index
        return -1

    def linearSearchOptimized(self, nums: List[int], target: int) -> int:
        """Same O(n) idea, but uses enumerate and avoids index lookups.
        Linear search cannot beat O(n) on unsorted data; this is the cleanest form."""
        for index, value in enumerate(nums):
            if value == target:
                return index
        return -1


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([4, 2, 7, 1], 7, 2),
        ([1, 2, 3], 3, 2),   # last element (the bug case)
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 9, -1),
        ([], 5, -1),
        ([5], 5, 0),
        ([2, 2, 2], 2, 0),   # first occurrence
    ]
    for nums, target, expected in cases:
        assert s.linearSearchBruteForce(nums, target) == expected
        assert s.linearSearchOptimized(nums, target) == expected
    print("all passed")
