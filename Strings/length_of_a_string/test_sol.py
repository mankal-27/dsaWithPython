import unittest

from sol import Solution


class TestLengthOfAString(unittest.TestCase):
    METHODS = [
        "length_of_string_char_loop",
        "length_of_string_builtin_len",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s), expected)

    def test_example_1(self):
        self._check_all_methods("hello", 5)

    def test_example_2_with_space(self):
        self._check_all_methods("open ai", 7)

    def test_empty_string(self):
        self._check_all_methods("", 0)

    def test_single_character(self):
        self._check_all_methods("a", 1)

    def test_all_spaces(self):
        self._check_all_methods("   ", 3)

    def test_string_with_digits(self):
        self._check_all_methods("a1b2c3", 6)

    def test_long_string_near_length_constraint(self):
        s = "x" * 10000
        self._check_all_methods(s, 10000)


if __name__ == "__main__":
    unittest.main()
