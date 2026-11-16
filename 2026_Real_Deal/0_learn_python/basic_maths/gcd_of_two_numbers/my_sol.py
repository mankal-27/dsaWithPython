class Solution:
    # BUG 1: range(1, min(...)) excludes min itself, so gcd(4, 8) misses 4 and returns 2. Use min + 1.
    # BUG 2: `&` binds tighter than `==`, so the condition is parsed as the chain
    #        num1 % i == (0 & num2) % i == 0, which only checks num1 % i. Use `and`.
    # BUG 3: no guard for 0 or negative inputs.
    def gcd(self, num1, num2):
        largest = 1
        for i in range(1, min(num1, num2)):
            if num1 % i == 0 & num2 % i == 0:
                largest = i
        return largest

    # BUG 4: range(min, 1) has no negative step, so it is empty and the method returns None.
    #        Use range(min, 0, -1).
    # BUG 5: same `&` precedence bug as above. Use `and`.
    def gcd1(self, num1, num2):
        for i in range(min(num1, num2), 1):
            if(num1 % i == 0 & num2 % i == 0):
                return i
