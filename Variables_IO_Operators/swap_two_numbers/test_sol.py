import unittest

from sol import Solution


class TestSwapTwoNumbers(unittest.TestCase):
    """
    Note: the methods on Solution take `self`, so they're instance methods -
    call them on an instance (Solution().method(a, b)), not on the class
    directly. Solution.method(a, b) would bind `a` to `self` and leave `b`
    unfilled, raising a TypeError.
    """

    METHODS = [
        "swap_two_num_with_built_in_method",
        "swap_two_num_with_temp",
        "swap_two_num_with_arithmetic",
        "swap_two_num_with_or",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, a, b, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(a, b), expected)

    def test_example_1(self):
        self._check_all_methods(5, 7, [7, 5])

    def test_example_2_negative(self):
        self._check_all_methods(-3, 9, [9, -3])

    def test_equal_values(self):
        self._check_all_methods(4, 4, [4, 4])

    def test_one_value_zero(self):
        self._check_all_methods(0, 6, [6, 0])

    def test_both_zero(self):
        self._check_all_methods(0, 0, [0, 0])

    def test_both_negative(self):
        self._check_all_methods(-8, -2, [-2, -8])

    def test_max_32bit_signed_boundary(self):
        self._check_all_methods(2147483647, -2147483648, [-2147483648, 2147483647])


if __name__ == "__main__":
    unittest.main()
