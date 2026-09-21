class Solution:
    def swap_two_num_with_built_in_method(a,b):
        a,b = b, a
        return [a, b]

    def swap_two_num_with_temp(a,b):
        temp = a
        a = b
        b = temp
        return [a, b]

    def swap_two_num_with_arithmetic(a,b):
        a = a + b
        b = a - b
        a = a - b
        return [a, b]

    def swap_two_num_with_or(a,b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return [a, b]
    