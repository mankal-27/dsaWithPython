import unittest

from sol import Solution


class TestMultiplicationTable(unittest.TestCase):
    METHODS = [
        "multiplication_table_repeated_addition",
        "multiplication_table_multiply",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1(self):
        self._check_all_methods(5, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

    def test_example_2(self):
        self._check_all_methods(7, [7, 14, 21, 28, 35, 42, 49, 56, 63, 70])

    def test_zero(self):
        self._check_all_methods(0, [0] * 10)

    def test_negative(self):
        self._check_all_methods(-3, [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30])

    def test_one(self):
        self._check_all_methods(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min_constraint(self):
        self._check_all_methods(-1000, [-1000 * i for i in range(1, 11)])

    def test_max_constraint(self):
        self._check_all_methods(1000, [1000 * i for i in range(1, 11)])


if __name__ == "__main__":
    unittest.main()
