class Solution:
    def perfectNumber(self, num):
        target = 0
        # BUG 2: O(n) loop; divisors come in pairs, so looping to sqrt(n) is enough
        for i in range(1, num):
            if(num % i == 0):
                target = target + i
        # BUG 3: num = 0 -> loop is empty, sum = 0, so 0 == 0 returns True (0 is NOT perfect)
        return target == num
