class Solution:
    def multiplication_table_repeated_addition(self, n):
        result = [0] * 10
        total = 0
        for i in range(1, 11):
            total = total + n
            result[i-1] = total
        return result

    def multiplication_table_multiply(self, n):
        result = [0] * 10
        for i in range(1, 11):
            result[i-1] = n * i
        return result
