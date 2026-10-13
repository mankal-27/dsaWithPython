import unittest

from sol import Solution

# print_1_to_n_recursive is tested up to n=950, not the constraint's full
# n=1000. With Python's default recursion limit (1000) and unittest's own
# call-stack overhead, n around 985+ raises RecursionError for this
# implementation — see the README's "Recursion Depth Limit" note. This is a
# real, worth-knowing limitation, not something this test suite works around.
# print_1_to_n_iterative has no such limit (no recursion), so it's tested at
# the full n=1000.


class TestPrint1ToN(unittest.TestCase):
    METHODS = [
        "print_1_to_n_recursive",
        "print_1_to_n_iterative",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1(self):
        self._check_all_methods(5, [1, 2, 3, 4, 5])

    def test_example_2(self):
        self._check_all_methods(3, [1, 2, 3])

    def test_min_boundary(self):
        self._check_all_methods(1, [1])

    def test_large_n_within_recursion_limit(self):
        self._check_all_methods(950, list(range(1, 951)))

    def test_max_constraint_iterative_only(self):
        # Only the iterative method here: recursive hits Python's default
        # recursion limit at n=1000 (see note above).
        self.assertEqual(
            self.sol.print_1_to_n_iterative(1000), list(range(1, 1001))
        )


if __name__ == "__main__":
    unittest.main()
