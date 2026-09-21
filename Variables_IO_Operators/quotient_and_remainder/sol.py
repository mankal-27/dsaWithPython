class Solution:
   def quotient_remainder_brute(self,dividend, divisor):
    if dividend == 0:
        return [0, 0]

    sign_differs = (dividend < 0) != (divisor < 0)
    a, b = abs(dividend), abs(divisor)

    count = 0
    while a >= b:
        a -= b        # subtract one whole copy of the divisor's magnitude
        count += 1    # ... and count it

    # `count` and the leftover `a` are truncating-division results (magnitudes only).
    # Adjust for Python's floor-division convention when signs differ and there's a remainder:
    if sign_differs and a != 0:
        quotient = -(count + 1)
    else:
        quotient = -count if sign_differs else count

    # Recompute remainder from the identity, so it's guaranteed consistent with quotient:
    remainder = dividend - divisor * quotient
    return [quotient, remainder]


    def quotient_remainder_optimized(self, dividend, divisor):
        # Optimized - Built-in Integer Division and Modulo (see README)
        quotient = dividend // divisor
        remainder = dividend % divisor
        return [quotient, remainder]
