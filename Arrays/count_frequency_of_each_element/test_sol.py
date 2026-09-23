import unittest

from sol import Solution


class TestCountFrequencyOfEachElement(unittest.TestCase):
    METHODS = [
        "count_frequency_nested_loop",
        "count_frequency_hash_map",
        "count_frequency_builtin_counter",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(list(nums)), expected)

    def test_example_1(self):
        self._check_all_methods([1, 2, 2, 3], [[1, 1], [2, 2], [3, 1]])

    def test_example_2(self):
        self._check_all_methods([-1, -1, 2, -1, 2], [[-1, 3], [2, 2]])

    def test_empty_array(self):
        self._check_all_methods([], [])

    def test_first_appearance_order_differs_from_numeric_order(self):
        self._check_all_methods([9, 8, 9, 8, 7], [[9, 2], [8, 2], [7, 1]])

    def test_all_distinct_elements(self):
        self._check_all_methods([4, 1, 7, 3], [[4, 1], [1, 1], [7, 1], [3, 1]])

    def test_all_same_element(self):
        self._check_all_methods([2, 2, 2, 2], [[2, 4]])

    def test_single_element(self):
        self._check_all_methods([5], [[5, 1]])

    def test_large_array_near_length_constraint(self):
        # 10,000 elements total (the stated constraint's upper bound),
        # with the last value repeated once so a duplicate is exercised too.
        nums = list(range(9999)) + [9998]
        expected = [[v, 1] for v in range(9998)] + [[9998, 2]]
        self._check_all_methods(nums, expected)


if __name__ == "__main__":
    unittest.main()
