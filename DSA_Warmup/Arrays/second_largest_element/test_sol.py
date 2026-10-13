import unittest

from sol import Solution


class TestSecondLargestElement(unittest.TestCase):
    METHODS = [
        "second_largest_two_pass",
        "second_largest_one_pass",
        "second_largest_sort_distinct",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(nums), expected)

    def test_example_1(self):
        self._check_all_methods([3, 9, 5], 5)

    def test_example_2_all_same(self):
        self._check_all_methods([5, 5, 5], -1)

    def test_single_element(self):
        self._check_all_methods([7], -1)

    def test_duplicate_maximum_valid_second(self):
        self._check_all_methods([5, 5, 4], 4)

    def test_all_negative(self):
        # specifically exercises the sentinel/None handling and the
        # "largest must actually be found first" requirement
        self._check_all_methods([-5, -2, -9], -5)

    def test_large_array_near_length_constraint(self):
        # 10^5 elements: 0..99998 plus a duplicate of the max (99998)
        nums = list(range(99999)) + [99998]
        self._check_all_methods(nums, 99997)


if __name__ == "__main__":
    unittest.main()
