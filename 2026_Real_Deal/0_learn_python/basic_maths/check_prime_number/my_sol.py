import math
class Solution:
    def isPrimeBrute(self, number):
        if number <= 1 :
            return False
        for num in range(2,number):
            if(number % num == 0):
                return False
        return True

    # BUG 1 again: missing `self`
    def isPrimeOptimized(self, number):
        if number <= 1:
            return False
        # BUG 4: math.sqrt returns a float -> range() raises TypeError
        # BUG 5: range end is exclusive, so even with int() it misses sqrt(n) itself (n = 4, 9, 25 would wrongly be prime)
        for num in range(2, math.isqrt(number)):
            if(number % num == 0):
                return False
        return True
