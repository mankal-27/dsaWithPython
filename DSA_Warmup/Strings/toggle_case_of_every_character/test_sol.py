import unittest

from sol import Solution


class TestToggleCaseOfEveryCharacter(unittest.TestCase):
    METHODS = [
        "toggle_case_ascii_arithmetic",
        "toggle_case_builtin_swapcase",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s), expected)

    def test_example_1(self):
        self._check_all_methods("Hello World", "hELLO wORLD")

    def test_example_2(self):
        self._check_all_methods("ABCabc", "abcABC")

    def test_empty_string(self):
        self._check_all_methods("", "")

    def test_no_letters(self):
        self._check_all_methods("123 !@#", "123 !@#")

    def test_all_uppercase(self):
        self._check_all_methods("ABCDE", "abcde")

    def test_all_lowercase(self):
        self._check_all_methods("abcde", "ABCDE")

    def test_mixed_letters_digits_punctuation(self):
        self._check_all_methods("Hi 9!", "hI 9!")

    def test_long_string_near_length_constraint(self):
        s = "a" * 500 + "B" * 500  # 1000 characters
        expected = "A" * 500 + "b" * 500
        self._check_all_methods(s, expected)


if __name__ == "__main__":
    unittest.main()
