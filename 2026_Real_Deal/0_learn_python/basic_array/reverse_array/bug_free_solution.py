"""Reverse Array: return the array with its elements in reverse order."""


class Solution:
    def reverse_brute_force(self, numbers: list[int]) -> list[int]:
        """Copy elements into a new array from the back. O(n) time, O(n) space."""
        size = len(numbers)
        reversed_numbers = [None] * size
        for index in range(size - 1, -1, -1):
            reversed_numbers[size - index - 1] = numbers[index]
        return reversed_numbers

    def reverse_optimized(self, numbers: list[int]) -> list[int]:
        """Swap mirrored pairs with two pointers, in place. O(n) time, O(1) space."""
        left, right = 0, len(numbers) - 1
        while left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
        return numbers


if __name__ == "__main__":
    solution = Solution()
    cases = {(): [], (5,): [5], (1, 2, 3): [3, 2, 1], (1, 2, 3, 4): [4, 3, 2, 1], (-1, 0, 7): [7, 0, -1]}
    for arr, expected in cases.items():
        assert solution.reverse_brute_force(list(arr)) == expected, arr
        assert solution.reverse_optimized(list(arr)) == expected, arr
    print("all tests passed")
