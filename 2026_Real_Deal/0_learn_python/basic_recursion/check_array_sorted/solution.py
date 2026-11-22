class Solution:
    def check_brute_force(self, nums):
        """Compare against the sorted copy. O(n log n) time, O(n) space."""
        return nums == sorted(nums)

    def check_recursive(self, nums):
        """Your approach: compare neighbours, recurse right.
        O(n) time, O(n) stack. Fails for len > ~1000 (recursion limit)."""

        def helper(index):
            if index >= len(nums) - 1:
                return True
            if nums[index] > nums[index + 1]:
                return False
            return helper(index + 1)

        return helper(0)

    def check_optimized(self, nums):
        """Single pass loop, early exit on first descent.
        O(n) time, O(1) space, no stack growth."""
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    cases = [[], [5], [1, 2], [2, 1], [1, 1, 1], [1, 2, 2, 3], [1, 3, 2, 4], [-3, -1, 0, 7], [3, 2, 1]]
    for nums in cases:
        expected = nums == sorted(nums)
        assert sol.check_brute_force(nums) == sol.check_recursive(nums) == sol.check_optimized(nums) == expected
    big = list(range(100000))
    assert sol.check_optimized(big) is True
    print("all ok")
