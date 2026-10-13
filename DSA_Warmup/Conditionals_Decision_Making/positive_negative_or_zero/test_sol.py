import unittest

from sol import Solution


class TestClassifySign(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_positive(self):
        self.assertEqual(self.sol.classify_sign(5), "Positive")

    def test_example_2_zero(self):
        self.assertEqual(self.sol.classify_sign(0), "Zero")

    def test_negative(self):
        self.assertEqual(self.sol.classify_sign(-7), "Negative")

    def test_small_positive_boundary(self):
        self.assertEqual(self.sol.classify_sign(1), "Positive")

    def test_small_negative_boundary(self):
        self.assertEqual(self.sol.classify_sign(-1), "Negative")

    def test_max_32bit_signed_int_positive(self):
        self.assertEqual(self.sol.classify_sign(2147483647), "Positive")

    def test_min_32bit_signed_int_negative(self):
        self.assertEqual(self.sol.classify_sign(-2147483648), "Negative")


if __name__ == "__main__":
    unittest.main()
