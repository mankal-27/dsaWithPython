class Solution:
    def print_1_to_n_recursive(self, n):
        result = []

        def helper(i):
            if i > n :
                return
            result.append(i)
            helper(i + 1)
        helper(1)
        return result

    def print_1_to_n_iterative(self, n):
        result = []
        i = 1
        while(i <= n):
            result.append(i)
            i += 1
        return result
