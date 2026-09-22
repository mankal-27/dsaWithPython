import unittest

from sol import Solution


class TestSumOfDivisors(unittest.TestCase):
    METHODS = [
        "sum_of_divisors_linear_scan",
        "sum_of_divisors_sqrt_scan",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1(self):
        self._check_all_methods(12, 28)

    def test_example_2(self):
        self._check_all_methods(6, 12)

    def test_min_boundary(self):
        self._check_all_methods(1, 1)

    def test_prime(self):
        # a prime's only divisors are 1 and itself
        self._check_all_methods(13, 14)

    def test_perfect_square(self):
        # exercises the middle-divisor double-counting guard (partner == i at i=4)
        self._check_all_methods(16, 31)

    def test_perfect_square_larger(self):
        # a second perfect square (5*5) to further confirm the guard generalizes
        self._check_all_methods(25, 31)

    def test_max_constraint(self):
        # n = 10^6, the largest value allowed by the stated constraints
        self._check_all_methods(1000000, 2480437)


if __name__ == "__main__":
    unittest.main()
