import math


class Solution:
    # ---------------- Brute force: O(d) time, O(1) space ----------------
    # Same idea as the original count(): chop off the last digit until nothing is left.
    # Fix: use abs() so negative numbers work (original returned 0 for them).
    def count_digits_brute_force(self, number):
        number = abs(number)      # sign is not a digit: -123 -> 123
        if number == 0:           # 0 has one digit; the loop below would run zero times
            return 1
        digit_count = 0
        while number > 0:
            number //= 10         # drop the last digit (123 -> 12)
            digit_count += 1      # one digit removed -> one digit counted
        return digit_count

    # ---------------- Optimized: O(1) time, O(1) space ----------------
    # Same idea as the original countOptimized(): digits = floor(log10(n)) + 1.
    # Fix: log10 returns a float that can round UP near a power of 10
    # (999999999999999 -> 16). Verify the estimate with exact integer math.
    def count_digits_optimized(self, number):
        number = abs(number)
        if number == 0:           # log10(0) is undefined
            return 1
        digit_count = int(math.log10(number)) + 1   # estimate, may be 1 too high
        if 10 ** (digit_count - 1) > number:        # smallest k-digit number must be <= number
            digit_count -= 1
        return digit_count
