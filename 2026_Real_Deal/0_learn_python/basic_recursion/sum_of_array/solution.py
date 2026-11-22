class Solution:
    def sum_brute_force(self, nums):
        """Loop: add every element. O(n) time, O(1) space."""
        total = 0
        for value in nums:
            total += value
        return total

    def sum_recursive(self, nums):
        """Your approach: sum(i) = nums[i] + sum(i+1), base case i == len.
        O(n) time, O(n) stack. Fails for len > ~990 (recursion limit)."""
        def helper(index):
            if index == len(nums):
                return 0
            return nums[index] + helper(index + 1)
        return helper(0)

    def sum_optimized(self, nums):
        """Divide and conquer recursion: split in halves, depth O(log n),
        so no recursion-limit problem. O(n) time, O(log n) stack."""
        def helper(low, high):  # sums nums[low:high]
            if low >= high:
                return 0
            if high - low == 1:
                return nums[low]
            mid = (low + high) // 2
            return helper(low, mid) + helper(mid, high)
        return helper(0, len(nums))


if __name__ == "__main__":
    s = Solution()
    for arr in [[], [5], [1, 2, 3, 4], [-1, 2, -3], list(range(1, 501))]:
        assert s.sum_brute_force(arr) == s.sum_recursive(arr) == s.sum_optimized(arr) == sum(arr)
    big = list(range(100000))
    assert s.sum_optimized(big) == sum(big)
    print("all ok")
