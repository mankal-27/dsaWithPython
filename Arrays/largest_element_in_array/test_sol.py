import unittest

from sol import Solution


class TestLargestElementInArray(unittest.TestCase):
    METHODS = [
        "largest_element_linear_scan",
        "largest_element_builtin_max",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(nums), expected)

    def test_example_1(self):
        self._check_all_methods([3, 9, 5], 9)

    def test_example_2_all_negative(self):
        # specifically exercises seeding with nums[0], not 0
        self._check_all_methods([-5, -2, -9], -2)

    def test_single_element(self):
        self._check_all_methods([42], 42)

    def test_duplicate_maximum(self):
        self._check_all_methods([4, 7, 7, 2], 7)

    def test_32bit_boundary_values(self):
        self._check_all_methods([-2147483648, 0, 2147483647], 2147483647)

    def test_large_array_near_length_constraint(self):
        # 10^4 elements, the largest at the end
        nums = list(range(10000))
        self._check_all_methods(nums, 9999)


if __name__ == "__main__":
    unittest.main()
