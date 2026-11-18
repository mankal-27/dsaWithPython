from collections import Counter

class Solution:
    def sum_highest_lowest_frequency(self, nums):
        if not nums:
            return 0

        freq_map = Counter(nums)

        max_freq = 0
        min_freq = len(nums)  # OK: a count can never exceed len(nums), so it is a safe 'infinity'

        # BUG 1: .items() yields (value, count) tuples, so `count > max_freq` compares tuple with int -> TypeError.
        #        Fix: iterate freq_map.values().
        for count in freq_map.items():
            if count > max_freq:
                max_freq = count
            if count < min_freq:
                min_freq = count
        return max_freq + min_freq
    