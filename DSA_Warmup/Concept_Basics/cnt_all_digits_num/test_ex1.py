import unittest

from ex1 import Solution


class TestCountDigit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_single_digit(self):
        self.assertEqual(self.sol.countDigit(4), 1)

    def test_example_2_two_digits(self):
        self.assertEqual(self.sol.countDigit(14), 2)

    def test_example_3_three_digits(self):
        self.assertEqual(self.sol.countDigit(234), 3)

    def test_zero_edge_case(self):
        # n = 0 has 1 digit, not 0 - this is the case the early return guards against.
        self.assertEqual(self.sol.countDigit(0), 1)

    def test_single_digit_boundary_low(self):
        self.assertEqual(self.sol.countDigit(1), 1)

    def test_single_digit_boundary_high(self):
        self.assertEqual(self.sol.countDigit(9), 1)

    def test_two_digit_boundary(self):
        self.assertEqual(self.sol.countDigit(10), 2)

    def test_four_digit_number(self):
        self.assertEqual(self.sol.countDigit(1000), 4)

    def test_max_constraint_value(self):
        # Upper bound from the problem constraints: 0 <= n <= 5000
        self.assertEqual(self.sol.countDigit(5000), 4)

    def test_power_of_ten(self):
        self.assertEqual(self.sol.countDigit(100), 3)


if __name__ == "__main__":
    unittest.main()
