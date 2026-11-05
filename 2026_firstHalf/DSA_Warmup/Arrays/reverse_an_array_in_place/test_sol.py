import unittest

from sol import Solution


class TestReverseArray(unittest.TestCase):
    METHODS = [
        "reverse_array_two_pointers",
        "reverse_array_builtin_reverse",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, nums, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                # each method mutates its input in place, so pass a fresh copy
                self.assertEqual(method(list(nums)), expected)

    def test_example_1_even_length(self):
        self._check_all_methods([1, 2, 3, 4], [4, 3, 2, 1])

    def test_example_2_odd_length_negative(self):
        self._check_all_methods([-3, -1, -2, -5, -4], [-4, -5, -2, -1, -3])

    def test_empty_array(self):
        self._check_all_methods([], [])

    def test_single_element(self):
        self._check_all_methods([7], [7])

    def test_two_elements(self):
        self._check_all_methods([1, 2], [2, 1])

    def test_odd_length_middle_element_unmoved(self):
        self._check_all_methods([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

    def test_large_array_near_length_constraint(self):
        nums = list(range(10000))
        expected = list(range(9999, -1, -1))
        self._check_all_methods(nums, expected)

    def test_returns_the_same_list_object(self):
        # both methods should reverse in place and return that same object
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                original = [1, 2, 3]
                result = method(original)
                self.assertIs(result, original)


if __name__ == "__main__":
    unittest.main()
