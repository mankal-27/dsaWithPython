import unittest

from sol import Solution


class TestQuotientRemainder(unittest.TestCase):
    METHODS = [
        "quotient_remainder_brute",
        "quotient_remainder_optimized",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, dividend, divisor, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(dividend, divisor), expected)

    def test_example_1(self):
        self._check_all_methods(17, 5, [3, 2])

    def test_example_2(self):
        self._check_all_methods(3, 8, [0, 3])

    def test_zero_dividend(self):
        self._check_all_methods(0, 5, [0, 0])

    def test_exact_division(self):
        self._check_all_methods(10, 5, [2, 0])

    def test_dividend_equals_divisor(self):
        self._check_all_methods(5, 5, [1, 0])

    def test_negative_dividend_positive_divisor(self):
        self._check_all_methods(-17, 5, [-4, 3])

    def test_positive_dividend_negative_divisor(self):
        self._check_all_methods(17, -5, [-4, -3])

    def test_both_negative(self):
        self._check_all_methods(-17, -5, [3, -2])

    def test_divisor_of_one(self):
        self._check_all_methods(12345, 1, [12345, 0])

    def test_max_32bit_signed_dividend_optimized_only(self):
        # Only the optimized method here: quotient_remainder_brute is
        # O(dividend / divisor), and with divisor=2 this dividend forces
        # ~2^30 loop iterations (~80s in practice) - exactly the scaling
        # problem the README's complexity section calls out. Not practical
        # to run on every test invocation, so this checks the O(1) method.
        self.assertEqual(
            self.sol.quotient_remainder_optimized(2147483647, 2), [1073741823, 1]
        )


if __name__ == "__main__":
    unittest.main()
