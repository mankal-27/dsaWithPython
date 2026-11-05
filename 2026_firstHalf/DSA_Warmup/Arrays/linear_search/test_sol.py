import unittest

from sol import Solution


class TestLinearSearch(unittest.TestCase):
    METHODS = [
        "linear_search_scan",
        "linear_search_builtin_index",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, target, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(nums, target), expected)

    def test_example_1(self):
        self._check_all_methods([5, 3, 8, 1], 8, 2)

    def test_example_2_not_found(self):
        self._check_all_methods([4, 2, 7, 9], 6, -1)

    def test_empty_array(self):
        self._check_all_methods([], 5, -1)

    def test_duplicate_target_returns_first_occurrence(self):
        self._check_all_methods([3, 7, 3, 7], 7, 1)

    def test_target_at_first_index(self):
        self._check_all_methods([9, 1, 2], 9, 0)

    def test_target_at_last_index(self):
        self._check_all_methods([1, 2, 3, 4, 5], 5, 4)

    def test_large_array_near_length_constraint(self):
        nums = list(range(10000))
        self._check_all_methods(nums, 9999, 9999)


if __name__ == "__main__":
    unittest.main()
