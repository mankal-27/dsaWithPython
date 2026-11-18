from collections import Counter


class Solution:
    """Second most frequent element.
    Rank by distinct frequency: the 2nd-highest frequency, smallest value on ties.
    Returns -1 if the array is empty or has only one distinct frequency."""

    def second_most_frequent_brute(self, arr):
        # O(n^2) time, O(n) space: count each value by scanning the array
        if not arr:
            return -1
        counts = {}
        for candidate in arr:
            if candidate not in counts:
                counts[candidate] = sum(1 for other in arr if other == candidate)
        max_count = max(counts.values())
        lower = [c for c in counts.values() if c < max_count]
        if not lower:
            return -1
        second_count = max(lower)
        return min(v for v, c in counts.items() if c == second_count)

    def second_most_frequent_optimized(self, arr):
        # O(n) time, O(k) space: hash map, then one pass tracking top-2 frequencies
        if not arr:
            return -1
        freq_map = Counter(arr)

        max_freq = sec_freq = 0
        max_ele = sec_ele = -1

        for ele, count in freq_map.items():
            if count > max_freq:
                sec_freq, sec_ele = max_freq, max_ele  # old max is demoted (fixes my_sol bug)
                max_freq, max_ele = count, ele
            elif count == max_freq:
                max_ele = min(max_ele, ele)  # keep smallest of tied max values, it is what gets demoted later
            elif count > sec_freq:
                sec_freq, sec_ele = count, ele
            elif count == sec_freq:
                sec_ele = min(sec_ele, ele)
        return sec_ele


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([], -1), ([5], -1), ([1, 1, 2, 2], -1),
        ([1, 2, 2, 3, 3, 3], 2), ([1, 1, 2, 2, 3, 3, 3], 1),
        ([3, 3, 3, 1, 2, 2], 2), ([-1, -1, -1, 0, 0, 5], 0),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4], 2),
        ([4, 4, 4, 1, 2, 2, 3, 3, 3], 2),
        ([1, 2, 3, 3], 1),
        ([3, 5, 4, 2, 2, 5, 1, 2, 3, 5, 4, 3, 2, 4, 1], 3),
        ([5, 5, 3, 3, 2, 2, 2], 3),
    ]
    for arr, want in cases:
        for f in (s.second_most_frequent_brute, s.second_most_frequent_optimized):
            assert f(arr) == want, (f.__name__, arr, f(arr), want)
    print("all passed")
