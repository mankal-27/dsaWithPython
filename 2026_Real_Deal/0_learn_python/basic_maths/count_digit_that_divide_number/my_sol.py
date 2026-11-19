class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        while(num > 0):
            lastDigit = num % 10
            # BUG: `num` is shrinking (// 10 below), so this tests the digit against
            # the remaining prefix, not the original number. Keep a copy: original = num.
            # e.g. 121 -> checks 121%1, 12%2, 1%1 -> returns 3, but the answer is 2.
            if(num % lastDigit == 0):
                count += 1
            num //= 10
        return count


lastDigit = Solution()
result = lastDigit.countDigits(121)
print(result)
