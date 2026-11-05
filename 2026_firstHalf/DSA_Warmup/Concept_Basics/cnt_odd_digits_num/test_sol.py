import unittest

from sol import Solution


class TestCountOddDigits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_single_odd_digit(self):
        self.assertEqual(self.sol.countOddDigits(5), 1)

    def test_example_2_one_odd_one_even(self):
        self.assertEqual(self.sol.countOddDigits(25), 1)

    def test_example_3_two_odd_digits(self):
        self.assertEqual(self.sol.countOddDigits(15), 2)

    def test_zero_edge_case(self):
        self.assertEqual(self.sol.countOddDigits(0), 0)

    def test_all_even_digits(self):
        self.assertEqual(self.sol.countOddDigits(2468), 0)

    def test_all_odd_digits(self):
        self.assertEqual(self.sol.countOddDigits(1357), 4)

    def test_max_constraint_value(self):
        # Upper bound from the problem constraints: 0 <= n <= 5000 -> digits 5,0,0,0
        self.assertEqual(self.sol.countOddDigits(5000), 1)

    def test_single_odd_digit(self):
        self.assertEqual(self.sol.countOddDigits(9), 1)

    def test_single_even_digit(self):
        self.assertEqual(self.sol.countOddDigits(8), 0)

    def test_mixed_digits(self):
        # 4321 -> 3, 1 are odd
        self.assertEqual(self.sol.countOddDigits(4321), 2)

    def test_three_digit_mixed(self):
        # 357 -> all odd
        self.assertEqual(self.sol.countOddDigits(357), 3)


if __name__ == "__main__":
    unittest.main()
