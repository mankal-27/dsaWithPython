class Solution:
    def even_or_odd_modulo(self, n):
        # Brute Force - Modulo Check (see README)
        if(n % 2 != 0):
            return "Odd"
        return "Even"

    def even_or_odd_bitwise(self, n):
        # Optimized - Bitwise AND (see README)
        if n & 1:
            return "Odd"
        return "Even"
