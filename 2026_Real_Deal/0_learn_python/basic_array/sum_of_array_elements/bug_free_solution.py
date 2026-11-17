"""Sum of Array Elements: return the sum of all numbers in the array."""


class Solution:
    def sum_brute_force(self, numbers: list[int]) -> int:
        """Add elements one by one with a running total. O(n) time, O(1) space."""
        total = 0  # also the correct answer for an empty array
        for value in numbers:
            total += value
        return total

    def sum_optimized(self, numbers: list[int]) -> int:
        """Built-in sum() does the same loop in C, so it is faster in practice. O(n) time, O(1) space."""
        return sum(numbers)


if __name__ == "__main__":
    solution = Solution()
    cases = {(): 0, (5,): 5, (1, 2, 3): 6, (-1, -2, 3): 0, (10, 20, 30, 40): 100}
    for arr, expected in cases.items():
        assert solution.sum_brute_force(list(arr)) == expected, arr
        assert solution.sum_optimized(list(arr)) == expected, arr
    print("all tests passed")
