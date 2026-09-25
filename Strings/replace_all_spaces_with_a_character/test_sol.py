import unittest

from sol import Solution


class TestReplaceAllSpacesWithACharacter(unittest.TestCase):
    METHODS = [
        "replace_spaces_linear_scan",
        "replace_spaces_builtin_replace",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, ch, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s, ch), expected)

    def test_example_1(self):
        self._check_all_methods("a b c", "_", "a_b_c")

    def test_example_2(self):
        self._check_all_methods("hello world", "-", "hello-world")

    def test_empty_string(self):
        self._check_all_methods("", "*", "")

    def test_no_spaces(self):
        self._check_all_methods("nospaces", "_", "nospaces")

    def test_all_spaces(self):
        self._check_all_methods("   ", "#", "###")

    def test_multiple_consecutive_spaces(self):
        self._check_all_methods("a  b", "_", "a__b")

    def test_leading_space(self):
        self._check_all_methods(" lead", "_", "_lead")

    def test_trailing_space(self):
        self._check_all_methods("trail ", "_", "trail_")

    def test_long_string_near_length_constraint(self):
        s = "a " * 500  # 1000 characters
        expected = "aX" * 500
        self._check_all_methods(s, "X", expected)


if __name__ == "__main__":
    unittest.main()
