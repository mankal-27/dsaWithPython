from collections import Counter


class Solution:
    """Most frequent element. Tie rule: the smallest value wins."""

    def most_frequent_brute(self, arr):
        # O(n^2) time, O(1) space: count every element by scanning the whole array
        if not arr:
            return None
        best_value, best_count = None, 0
        for candidate in arr:
            count = 0
            for other in arr:
                if other == candidate:
                    count += 1
            if count > best_count or (count == best_count and candidate < best_value):  # tie -> smaller value
                best_value, best_count = candidate, count
        return best_value

    def most_frequent_optimized(self, arr):
        # O(n) time, O(k) space: hash map of counts, then pick max count, smaller value on ties
        if not arr:
            return None
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
        best_value, best_count = None, 0
        for num, count in freq_map.items():
            if count > best_count or (count == best_count and num < best_value):
                best_value, best_count = num, count
        return best_value

    def most_frequent_pythonic(self, arr):
        if not arr:
            return None
        freq = Counter(arr)
        return min(freq, key=lambda x: (-freq[x], x))  # max count, then smallest value


if __name__ == "__main__":
    s = Solution()
    cases = [([], None), ([5], 5), ([1, 2, 2, 3, 3, 3], 3), ([1, 2, 2, 1], 1), ([2, 2, 1, 1], 1), ([10000, 10000, 9999, 9999], 9999), ([-1, -1, 0], -1)]
    for arr, want in cases:
        for f in (s.most_frequent_brute, s.most_frequent_optimized, s.most_frequent_pythonic):
            assert f(arr) == want, (f.__name__, arr, f(arr), want)
    print("all passed")
