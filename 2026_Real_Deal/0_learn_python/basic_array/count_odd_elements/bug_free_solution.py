"""Count Odd Elements: return how many numbers in the array are odd."""


class Solution:
    def count_odd_brute_force(self, numbers: list[int]) -> int:
        """Check each value with % 2 and count. O(n) time, O(1) space."""
        odd_count = 0
        for value in numbers:  # value is the element itself, NOT an index
            if value % 2 != 0:  # works for negatives too: -3 % 2 == 1 in Python
                odd_count += 1
        return odd_count

    def count_odd_optimized(self, numbers: list[int]) -> int:
        """Generator + sum() does the same single pass in one expression. O(n) time, O(1) space."""
        return sum(value & 1 for value in numbers)  # bitwise: last bit is 1 for odd numbers


if __name__ == "__main__":
    solution = Solution()
    cases = {(): 0, (2,): 0, (3,): 1, (1, 2, 3): 2, (10, 20): 0, (0, 0, 5): 1, (-3, -2, 7): 2}
    for arr, expected in cases.items():
        assert solution.count_odd_brute_force(list(arr)) == expected, arr
        assert solution.count_odd_optimized(list(arr)) == expected, arr
    print("all tests passed")
