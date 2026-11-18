from collections import Counter


class Solution:
    """Sum of highest and lowest frequency.
    Count how often each value appears, then return (largest count) + (smallest count).
    Returns 0 for an empty array. With one distinct value, max == min so it is 2 * count."""

    def sum_highest_lowest_frequency_brute(self, nums):
        # O(n^2) time, O(k) space: count each value by scanning the array
        if not nums:
            return 0
        counts = {}
        for candidate in nums:
            if candidate not in counts:
                counts[candidate] = sum(1 for other in nums if other == candidate)
        return max(counts.values()) + min(counts.values())

    def sum_highest_lowest_frequency_optimized(self, nums):
        # O(n) time, O(k) space: hash map, then one pass tracking max and min count
        if not nums:
            return 0
        freq_map = Counter(nums)

        max_freq = 0
        min_freq = len(nums)
        for count in freq_map.values():  # fixes my_sol bug: .items() gave tuples
            max_freq = max(max_freq, count)
            min_freq = min(min_freq, count)
        return max_freq + min_freq


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([], 0), ([5], 2), ([1, 1, 2, 2], 4),
        ([1, 2, 2, 3, 3, 3], 4), ([1, 1, 2, 3], 3),
        ([-1, -1, -1, 0, 0, 5], 4),
        ([4, 4, 4, 4, 1, 2, 2], 5),
        ([7, 7, 7], 6),
    ]
    for arr, want in cases:
        for f in (s.sum_highest_lowest_frequency_brute, s.sum_highest_lowest_frequency_optimized):
            assert f(arr) == want, (f.__name__, arr, f(arr), want)
    print("all passed")
