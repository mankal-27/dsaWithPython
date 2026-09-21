import unittest

from sol import Solution


class TestEvenOrOdd(unittest.TestCase):
    METHODS = [
        "even_or_odd_modulo",
        "even_or_odd_bitwise",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1_even(self):
        self._check_all_methods(4, "Even")

    def test_example_2_negative_odd(self):
        self._check_all_methods(-3, "Odd")

    def test_zero(self):
        self._check_all_methods(0, "Even")

    def test_positive_odd(self):
        self._check_all_methods(7, "Odd")

    def test_negative_even(self):
        self._check_all_methods(-4, "Even")

    def test_small_positive_odd(self):
        self._check_all_methods(1, "Odd")

    def test_max_32bit_signed_int_odd(self):
        self._check_all_methods(2147483647, "Odd")

    def test_min_32bit_signed_int_even(self):
        self._check_all_methods(-2147483648, "Even")


if __name__ == "__main__":
    unittest.main()
