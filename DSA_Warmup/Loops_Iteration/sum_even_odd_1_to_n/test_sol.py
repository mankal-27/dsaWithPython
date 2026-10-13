import unittest

from sol import Solution

# NOTE: sum_even_or_odd_step_by_two and sum_even_or_odd_formula have swapped
# bodies relative to their names (step_by_two actually runs the O(1) formula;
# formula actually runs the step-by-2 loop). Both are functionally correct
# for every case below - this file tests by method name and verifies the
# actual, current behavior. See the README's naming-mismatch note.


class TestSumEvenOrOdd(unittest.TestCase):
    METHODS = [
        "sum_even_or_odd_loop_modulo",
        "sum_even_or_odd_step_by_two",
        "sum_even_or_odd_formula",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, parity, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n, parity), expected)

    def test_example_1(self):
        self._check_all_methods(10, "even", 30)

    def test_example_2(self):
        self._check_all_methods(9, "odd", 25)

    def test_empty_range_zero(self):
        self._check_all_methods(0, "even", 0)

    def test_empty_range_one_even(self):
        self._check_all_methods(1, "even", 0)

    def test_smallest_odd(self):
        self._check_all_methods(1, "odd", 1)

    def test_max_constraint_even(self):
        self._check_all_methods(10000, "even", 25005000)

    def test_max_constraint_odd(self):
        self._check_all_methods(10000, "odd", 25000000)


if __name__ == "__main__":
    unittest.main()
