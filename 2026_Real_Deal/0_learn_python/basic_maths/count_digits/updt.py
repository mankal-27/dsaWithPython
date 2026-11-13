class Solution:
    # Fix for count(): take abs() first so negative numbers work.
    # O(d) time, O(1) space, d = number of digits.
    def count_fixed(self, num):
        num = abs(num)  # -123 -> 123
        if num == 0:  # 0 has one digit
            return 1
        count = 0
        while num > 0:
            num //= 10  # drop last digit
            count += 1
        return count

    # Fix for countOptimized(): avoid float precision issues by correcting
    # the log estimate with an exact integer check against 10**k.
    # O(1) for typical ints (log + one pow), O(1) space.
    def count_log_fixed(self, num):
        import math
        num = abs(num)
        if num == 0:
            return 1
        digits = int(math.log10(num)) + 1  # estimate, may be off by 1 for huge n
        if 10 ** (digits - 1) > num:  # estimate too big -> e.g. 999..9 rounded up
            digits -= 1
        return digits

    # Most optimized / idiomatic: Python ints are arbitrary precision, and
    # str() is exact. O(d) time, O(d) space for the temporary string,
    # but it is a single C-level call and always correct.
    def count_str(self, num):
        return len(str(abs(num)))
