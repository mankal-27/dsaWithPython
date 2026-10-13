import unittest

from sol import Solution


class TestCountDigits(unittest.TestCase):
    METHODS = [
        "count_digits_repeated_division",
        "count_digits_string_length",
        "count_digits_logarithm",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1(self):
        self._check_all_methods(12345, 5)

    def test_example_2_negative(self):
        self._check_all_methods(-789, 3)

    def test_zero(self):
        self._check_all_methods(0, 1)

    def test_single_digit(self):
        self._check_all_methods(7, 1)

    def test_min_32bit_signed_int(self):
        # -2147483648, the specific overflow-risk edge case from the README
        self._check_all_methods(-2147483648, 10)

    def test_max_32bit_signed_int(self):
        self._check_all_methods(2147483647, 10)

    def test_exact_power_of_ten(self):
        # exercises the Logarithm approach's documented floating-point caveat
        self._check_all_methods(1000, 4)


if __name__ == "__main__":
    unittest.main()
