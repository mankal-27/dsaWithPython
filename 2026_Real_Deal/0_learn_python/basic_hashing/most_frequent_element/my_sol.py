from collections import Counter

class Solution:
    def most_frequency_element(self, arr):
        if not arr:
            return None

        freq_map = {}
        max_count = 0
        most_frequent = None

        for num in arr:
            #increment frequency count
            freq_map[num] = freq_map.get(num, 0) + 1

            #update max_count and result on the fly
            if freq_map[num] > max_count:
                max_count = freq_map[num]
                most_frequent = num

        # BUG (tie-break): on ties this returns whichever value *reaches* the max first,
        # e.g. [1,2,2,1] -> 2, but Counter-based version returns 1. Inconsistent results.
        return most_frequent

    # BUG: missing `self` -> Solution().most_frequent_pythonic(arr) raises TypeError
    def most_frequent_pythonic(arr):
        if not arr:
            return None

        counts = Counter(arr)

        return counts.most_common(1)[0][0]
        