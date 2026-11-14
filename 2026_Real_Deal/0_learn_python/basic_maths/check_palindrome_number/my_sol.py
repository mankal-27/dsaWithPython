class Solution:
    def reverseNumber(self, num):
        reverse_num = 0
        while(num > 0):
            last_digit = num % 10
            reverse_num = reverse_num * 10 + last_digit
            num //= 10
        return reverse_num

    # BUG 1: missing `self` -> Solution().checkPalindrome(121) raises TypeError.
    # BUG 2: `reverseNumb` is a typo AND is not a bare name: must be self.reverseNumber(num)
    #        (NameError as written).
    # BUG 3: negatives only return False because reverseNumber gives 0; make that explicit
    #        with `if num < 0: return False`.
    def checkPalindrome(self,num):
        reverse_num = self.reverseNumber(num)
        return reverse_num == num
