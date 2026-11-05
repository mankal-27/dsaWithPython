import math

class Solution:
    def count_digits_repeated_division(self, n):
        n = abs(n)
        if(n == 0):
            return 1
        count = 0
        while(n != 0):
            n = n // 10
            count = count + 1
        return count
        

    def count_digits_string_length(self, n):
        s = str(n)
        if s.startswith("-"):
            s = s[1:]
        return len(s)

    def count_digits_logarithm(self, n):
        n = abs(n)
        if(n == 0):
            return 1
        return math.floor(math.log10(n)) + 1
