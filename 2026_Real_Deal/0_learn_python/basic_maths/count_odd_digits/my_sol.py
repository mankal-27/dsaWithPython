class Solution:
    def count_odd_digits(self, num):
        num = abs(num)
        if num == 0 :
            return 0
        count = 0
        while(num > 0):
            lastDigit = num % 10
            if(lastDigit % 2 == 1):
                count = count + 1
            num = num // 10
        return count
        