import math
class Solution:
    def divsorOfNumBruteForce(self, number):
        finalList = []
        # BUG 1: range(number) starts at 0 -> number % 0 raises ZeroDivisionError
        # BUG 2: it also stops at number-1, so the number itself is never listed
        # FIX: range(1, number + 1)
        for i in range(number):
            if(number % i == 0):
                finalList.append(i)
        return finalList

    def divisorOfNumOptim(self, number):
        finalList = []
        for i in range(1, math.isqrt(number) + 1 ):
            if(number % i == 0):
                finalList.append(i)
                # BUG 3: number / i is float division -> returns 12.0 instead of 12
                # FIX: use number // i
                if(i != number // i):
                    finalList.append(number // i)
        return sorted(finalList)

    def divisors_optimized(self, number: int) -> list[int]:
            """Divisors come in pairs (i, n // i); scan only up to sqrt(n). O(sqrt n) time."""
            divisors = []
            smallDivisors = []
            largeDivisors = []
            for small in range(1, math.isqrt(number) + 1):
                if number % small == 0:
                    smallDivisors.append(small)
                    partner = number // small  # integer division keeps ints
                    if partner != small:  # perfect square: don't add the root twice
                        largeDivisors.append(partner)
            divisors = [*smallDivisors, *reversed(largeDivisors)]
            return divisors

newDivisor = Solution()
print(newDivisor.divisors_optimized(36))