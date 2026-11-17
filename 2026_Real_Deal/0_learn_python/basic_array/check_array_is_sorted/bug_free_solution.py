"""Check if Array Is Sorted: return True if the array is in non-decreasing order."""


class Solution:
    def is_sorted_brute_force(self, numbers: list[int]) -> bool:
        """Compare every pair (i, j) with i < j. O(n^2) time, O(1) space."""
        size = len(numbers)
        for first in range(size):
            for second in range(first + 1, size):
                if numbers[second] < numbers[first]:
                    return False
        return True

    def is_sorted_optimized(self, numbers: list[int]) -> bool:
        """Compare only adjacent elements in one pass. O(n) time, O(1) space."""
        for index in range(1, len(numbers)):
            if numbers[index] < numbers[index - 1]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    cases = {(): True, (5,): True, (1, 2, 3): True, (1, 1, 2): True, (3, 2, 1): False,
             (1, 3, 2, 4): False, (-5, -1, 0, 7): True, (2, 2, 2): True, (1, 2, 3, 2): False}
    for arr, expected in cases.items():
        assert solution.is_sorted_brute_force(list(arr)) == expected, arr
        assert solution.is_sorted_optimized(list(arr)) == expected, arr
    print("all tests passed")
