class Solution:
    def absolute_value_conditional(self, n):
        # Brute Force - Conditional Negation (see README)
        if(n < 0): 
            return -n
        return n
        

    def absolute_value_bitwise(self, n):
        # Optimized - Bit Manipulation, branch-free (see README)
        mask = n >> 31
        return (n ^ mask) - mask

