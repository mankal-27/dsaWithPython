import unittest

from sol import Solution


class TestPrimeNumberCheck(unittest.TestCase):
    # is_prime_sqrt_scan is excluded from the full-coverage sweep below: its
    # while loop never increments `i` (missing `i += 1`), so it hangs forever
    # on any odd n >= 5 where 2 isn't a divisor (i.e. every odd input except
    # n = 3). See the "Known bug" callout in README.md. It's only exercised
    # here with inputs where that's provably safe: n <= 3 (loop body never
    # runs) and even n (the very first candidate, i = 2, always resolves the
    # loop on iteration one, whether n is 2 itself or an even composite).
    FULL_METHODS = [
        "is_prime_trial_division",
        "is_prime_six_k_optimization",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, n, expected):
        for name in self.FULL_METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(n), expected)

    def test_example_1(self):
        self._check_all_methods(17, True)

    def test_example_2(self):
        self._check_all_methods(18, False)

    def test_negative(self):
        self._check_all_methods(-7, False)

    def test_zero(self):
        self._check_all_methods(0, False)

    def test_one(self):
        self._check_all_methods(1, False)

    def test_two_smallest_prime(self):
        self._check_all_methods(2, True)

    def test_three(self):
        self._check_all_methods(3, True)

    def test_larger_prime(self):
        self._check_all_methods(997, True)

    def test_larger_composite(self):
        self._check_all_methods(1000, False)

    def test_perfect_square_composite(self):
        # 49 = 7*7 - its only nontrivial divisor sits exactly at the sqrt bound
        self._check_all_methods(49, False)

    # --- is_prime_sqrt_scan: only inputs verified safe from the hang above ---

    def test_sqrt_scan_boundary_and_even_inputs_only(self):
        safe_cases = [
            (-3, False),   # n <= 1 guard, loop body never runs
            (0, False),    # n <= 1 guard
            (1, False),    # n <= 1 guard
            (2, True),     # i*i=4 > 2, loop body never runs, returns True
            (3, True),     # i*i=4 > 3, loop body never runs, returns True
            (4, False),    # i=2 resolves on the very first check (4 % 2 == 0)
            (18, False),   # i=2 resolves on the very first check (18 % 2 == 0)
            (1000, False), # i=2 resolves on the very first check (1000 % 2 == 0)
        ]
        for n, expected in safe_cases:
            with self.subTest(n=n):
                self.assertEqual(self.sol.is_prime_sqrt_scan(n), expected)


if __name__ == "__main__":
    unittest.main()
