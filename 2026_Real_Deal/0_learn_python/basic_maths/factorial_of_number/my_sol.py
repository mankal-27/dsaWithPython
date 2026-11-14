class Solution:
    def factorial_number(self, num):
        if num == 0 :
            return 1
        result = 1
        # BUG 1: range(num) starts at 0, so result * 0 makes the answer 0 for every num >= 1.
        #        Fix: range(1, num + 1) so the loop multiplies 1, 2, ..., num.
        for i in range(num):
            result = result * i
        # BUG 2: negative input is not handled (factorial is undefined); should raise ValueError.
        return result
