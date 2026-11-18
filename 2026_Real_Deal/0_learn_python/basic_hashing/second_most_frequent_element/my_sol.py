from collections import Counter

class Solution:
    def second_most_frequent(self, arr):
        if not arr:
            return None

        freq_map = Counter(arr)

        max_freq = sec_max_freq = 0
        max_ele = sec_max_ele = -1

        for ele, count in freq_map.items():
            if count > max_freq:
                sec_max_ele = max_freq  # BUG 1: should be sec_max_freq = max_freq (old max becomes 2nd)
                sec_max_ele = max_ele
                max_freq = count
                max_ele = ele
            elif count == max_freq:
                max_ele = min(max_ele, ele)
            elif count > sec_max_freq:
                sec_max_freq = count
                sec_max_ele = ele
            elif count == sec_max_freq:
                sec_max_ele = min(sec_max_ele, ele)
        # BUG 2: -1 is used as 'no answer' but is also a valid array value; return None instead
        return sec_max_ele
