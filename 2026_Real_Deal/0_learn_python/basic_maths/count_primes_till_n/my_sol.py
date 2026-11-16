import math

class Solution:
    def isPrime(self, number):
        if number <= 1:
            return False
        limiter = math.isqrt(number)
        for divisor in range(2, limiter + 1):
            if(number % divisor == 0):
                return False
        return True

    # BUG 1: name says "print" but it returns a count
    def printPrimeNumberTillN(self, number):
        count = 0
        # BUG 2: range(number) stops at number-1, so n itself is skipped (n = 7 gives 3, not 4)
        for num in range(number):
            if(self.isPrime(num)):
                count += 1
        return count
    
