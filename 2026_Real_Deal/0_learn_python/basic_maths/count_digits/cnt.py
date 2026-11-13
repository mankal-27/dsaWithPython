import math


class Solution:
    # Brute force: repeatedly chop off the last digit and count how many chops it takes.
    # BUG: for negative input the loop condition (num > 0) is False immediately -> returns 0.
    #      (fixed in updt.py -> count_fixed)
    def count(self, num):
        # 0 has exactly one digit, but the loop below would run zero times -> special case
        if num == 0:
            return 1
        count = 0  # number of digits seen so far
        while num > 0:
            num = num // 10  # integer-divide drops the last digit (123 -> 12)
            count = count + 1  # one digit removed -> one digit counted
        return count

    # Optimized: digits = floor(log10(n)) + 1  (O(1) arithmetic).
    # BUG: log10 returns a float; for large n close to a power of 10
    #      (e.g. 999999999999999) the float rounds up to the next integer,
    #      so the result is off by one. (fixed in updt.py -> count_log_fixed)
    def countOptimized(self, num):
        if num == 0:  # log10(0) is undefined (math domain error)
            return 1
        # abs() handles negatives; int() truncates the float (floor for positives)
        result = int(math.log10(abs(num)) + 1)
        return result
