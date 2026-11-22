class Solution:
    def fib(self, n):
        #your code goes here
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)