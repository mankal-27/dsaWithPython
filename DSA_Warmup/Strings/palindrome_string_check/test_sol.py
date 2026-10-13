import unittest

from sol import Solution


class TestPalindromeStringCheck(unittest.TestCase):
    METHODS = [
        "palindrome_check_reverse_and_compare",
        "palindrome_check_two_pointers",
        "palindrome_check_builtin_slice",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s), expected)

    def test_example_1(self):
        self._check_all_methods("racecar", True)

    def test_example_2_not_a_palindrome(self):
        self._check_all_methods("hello", False)

    def test_empty_string(self):
        self._check_all_methods("", True)

    def test_single_character(self):
        self._check_all_methods("a", True)

    def test_even_length_palindrome(self):
        self._check_all_methods("abba", True)

    def test_odd_length_palindrome_with_middle_character(self):
        self._check_all_methods("level", True)

    def test_fails_on_first_character_pair(self):
        # exercises the two-pointer early-exit path
        self._check_all_methods("zello", False)

    def test_alphanumeric_palindromes(self):
        self._check_all_methods("1221", True)
        self._check_all_methods("12321", True)

    def test_long_palindrome_near_length_constraint(self):
        # 1000 characters (the stated upper bound), even-length so there's
        # no middle character: a 500-character half followed by its reverse.
        half = "ab" * 250  # 500 characters
        s = half + half[::-1]
        self.assertEqual(len(s), 1000)
        self._check_all_methods(s, True)


if __name__ == "__main__":
    unittest.main()
