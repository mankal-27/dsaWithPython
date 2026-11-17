class Solution:
    def findOddElemFromArray(self, arr):
        total = 0
        for value in arr:
            if(value % 2 != 0):
                total += 1
        return total
