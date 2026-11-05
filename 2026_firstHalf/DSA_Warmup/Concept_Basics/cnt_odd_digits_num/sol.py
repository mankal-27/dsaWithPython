import math
class Solution:
    def countOddDigits(self, n):
        count = 0
        if n == 0:
            return 0

        while(n > 0):
            digit = n % 10
            if digit % 2 != 0:
                count = count + 1
            n = math.floor(n /10)
        return count
        