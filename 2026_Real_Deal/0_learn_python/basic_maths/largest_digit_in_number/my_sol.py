class Solution:
    # BUG 1: negative input (e.g. -472) skips the loop (num > 0 is False) and silently returns 0
    #        instead of 7. Use abs(num) first.
    # BUG 2 (style): camelCase names, `while(...)`/`if(...)` parentheses, no trailing newline.
    # The loop is otherwise correct for num >= 0 (0 returns 0, which is right).
    def largest_digit_num(self, num):
        largest = 0

        while(num > 0):
            lastDigit = num % 10
            if(lastDigit > largest):
                largest = lastDigit
            num //= 10
        return largest
