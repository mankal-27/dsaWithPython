import math
class Solution:
    def armstrongNumber(self, number):
    
        # BUG 2: `sum` shadows the built-in sum()
        sum = 0 
        # BUG 1: number == 0 -> log10(0) raises ValueError (0 is an Armstrong number)
        # BUG 4: float log10 can mis-count digits on big numbers; use len(str(number))
        count_of_digit = int(math.log10(abs(number)) + 1)
        duplicate_num = number
        while(number > 0):
            last_digit = number % 10
            # BUG 3: math.pow returns float -> precision loss for large numbers; use last_digit ** count
            sum = sum + math.pow(last_digit, count_of_digit)
            number //= 10
        return duplicate_num == sum
