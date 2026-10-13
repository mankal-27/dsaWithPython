import unittest

from sol import Solution


class TestSumOfArrayElements(unittest.TestCase):
    METHODS = [
        "sum_of_array_elements_linear_scan",
        "sum_of_array_elements_builtin_sum",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(nums), expected)

    def test_example_1(self):
        self._check_all_methods([3, 9, 5], 17)

    def test_example_2_mixed_signs(self):
        self._check_all_methods([-3, 10, -7, 4], 4)

    def test_empty_array(self):
        self._check_all_methods([], 0)

    def test_single_element(self):
        self._check_all_methods([42], 42)

    def test_all_negative(self):
        self._check_all_methods([-5, -10, -3], -18)

    def test_large_array_near_32bit_boundary(self):
        # 10^5 elements at the 32-bit signed max; the sum (~2.1*10^14) would
        # overflow a 32-bit accumulator in a fixed-width-integer language,
        # though Python's arbitrary-precision ints make this a non-issue here
        nums = [2147483647] * 100000
        self._check_all_methods(nums, 2147483647 * 100000)


if __name__ == "__main__":
    unittest.main()
