class Solution:
    def reverse_brute_force(self, nums):
        """Build a new list by reading from the last index to 0. O(n) time, O(n) space. Input untouched."""
        result = []
        for index in range(len(nums) - 1, -1, -1):
            result.append(nums[index])
        return result

    def reverse_recursive(self, nums):
        """Your approach (copy first so input isn't mutated): swap ends, recurse inward.
        O(n) time, O(n) copy + O(n/2) stack. Fails for len > ~2000 (recursion limit)."""
        arr = list(nums)

        def helper(left, right):
            if left >= right:
                return
            arr[left], arr[right] = arr[right], arr[left]
            helper(left + 1, right - 1)

        helper(0, len(arr) - 1)
        return arr

    def reverse_optimized(self, nums):
        """In-place two-pointer loop. O(n) time, O(1) extra space, no recursion limit."""
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == "__main__":
    sol = Solution()
    for arr in [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5], list(range(500))]:
        expected = arr[::-1]
        original = list(arr)
        assert sol.reverse_brute_force(arr) == expected
        assert sol.reverse_recursive(arr) == expected
        assert arr == original  # not mutated
        assert sol.reverse_optimized(list(arr)) == expected
    big = list(range(100000))
    assert sol.reverse_optimized(list(big)) == big[::-1]
    print("all ok")
