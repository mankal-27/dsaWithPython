import unittest

from sol import Solution


class TestPrintPrimesUpToN(unittest.TestCase):
    METHODS = [
        "primes_up_to_n_trial_division",
        "primes_up_to_n_sieve_of_eratosthenes",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1(self):
        self._check_all_methods(10, [2, 3, 5, 7])

    def test_example_2_below_smallest_prime(self):
        self._check_all_methods(1, [])

    def test_zero(self):
        self._check_all_methods(0, [])

    def test_smallest_prime_boundary(self):
        self._check_all_methods(2, [2])

    def test_just_above_smallest_prime(self):
        self._check_all_methods(3, [2, 3])

    def test_mid_range(self):
        # primes from 2 to 30
        self._check_all_methods(30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_upper_bound_is_prime(self):
        # n itself is prime and must be included
        self._check_all_methods(29, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_larger_range_count(self):
        # sanity check at a larger scale: there are 168 primes below 1000
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(len(method(1000)), 168)


if __name__ == "__main__":
    unittest.main()
