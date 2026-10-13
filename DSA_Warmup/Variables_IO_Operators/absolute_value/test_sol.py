import unittest

from sol import Solution


class TestAbsoluteValue(unittest.TestCase):
    METHODS = [
        "absolute_value_conditional",
        "absolute_value_bitwise",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1_negative(self):
        self._check_all_methods(-5, 5)

    def test_example_2_positive(self):
        self._check_all_methods(42, 42)

    def test_zero(self):
        self._check_all_methods(0, 0)

    def test_already_positive(self):
        self._check_all_methods(7, 7)

    def test_max_32bit_signed_int(self):
        self._check_all_methods(2147483647, 2147483647)

    def test_min_safely_negatable_32bit_int(self):
        self._check_all_methods(-2147483647, 2147483647)

    def test_true_int_min(self):
        # -2^31: overflows in fixed-width languages (Java/C), but Python's
        # arbitrary-precision ints handle it correctly with no special-casing.
        self._check_all_methods(-2147483648, 2147483648)

    def test_small_negative(self):
        self._check_all_methods(-1, 1)


if __name__ == "__main__":
    unittest.main()
