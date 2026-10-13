import unittest

from sol import Solution


class TestCheckIfArrayIsSorted(unittest.TestCase):
    METHODS = [
        "is_sorted_adjacent_comparison",
        "is_sorted_builtin_all_zip",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(nums), expected)

    def test_example_1_with_duplicates(self):
        self._check_all_methods([1, 2, 2, 3], True)

    def test_example_2_not_sorted(self):
        self._check_all_methods([3, 1, 2], False)

    def test_empty_array(self):
        self._check_all_methods([], True)

    def test_single_element(self):
        self._check_all_methods([5], True)

    def test_violation_near_the_end(self):
        # confirms the full scan is necessary, not just an early check
        self._check_all_methods([1, 2, 3, 4, 0], False)

    def test_strictly_decreasing(self):
        self._check_all_methods([5, 4, 3, 2, 1], False)

    def test_large_sorted_array_near_length_constraint(self):
        nums = list(range(100000))
        self._check_all_methods(nums, True)


if __name__ == "__main__":
    unittest.main()
