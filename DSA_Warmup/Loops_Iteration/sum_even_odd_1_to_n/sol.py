class Solution:
    def sum_even_or_odd_loop_modulo(self, n, parity):
        target = 0 if parity == "even" else 1
        total = 0
        for i in range(1, n+1):
            if i % 2 == target:
                total += i
        return total


    def sum_even_or_odd_formula(self, n, parity):
        if parity == "even":
            k = n // 2
            return k * (k + 1)
        else:
            k = (n + 1) // 2
            return k * k

    def sum_even_or_odd_step_by_two(self, n, parity):
        start = 2 if parity == "even" else 1
        total = 0
        i = start
        while i <= n:
            total += i
            i += 2
        return total
