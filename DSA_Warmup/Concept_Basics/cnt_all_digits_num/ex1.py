import math
class Solution:
    def countDigit(self, n):
        count = 0
        if n == 0:
            return 1
        while(n > 0):
            count = count + 1
            n = math.floor(n / 10)
        return count 