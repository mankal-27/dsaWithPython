import unittest

from sol import Solution


class TestCountWordsInASentence(unittest.TestCase):
    METHODS = [
        "count_words_strip_split",
        "count_words_transition_counting",
        "count_words_builtin_split",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s), expected)

    def test_example_1(self):
        self._check_all_methods("hello world", 2)

    def test_example_2_leading_and_trailing_and_multiple_spaces(self):
        self._check_all_methods("  leading and trailing  ", 3)

    def test_empty_string(self):
        self._check_all_methods("", 0)

    def test_only_spaces(self):
        self._check_all_methods("     ", 0)

    def test_single_word_no_surrounding_spaces(self):
        self._check_all_methods("single", 1)

    def test_multiple_consecutive_spaces_between_words(self):
        self._check_all_methods("multiple   spaces   here", 3)

    def test_leading_spaces_only(self):
        self._check_all_methods("  leading", 1)

    def test_trailing_spaces_only(self):
        self._check_all_methods("trailing  ", 1)

    def test_long_string_near_length_constraint(self):
        # 10,000 characters: 2000 single-character words separated by
        # double spaces, exercising both the length bound and repeated spaces.
        s = "a  " * 3333
        s = s.strip()
        expected = 3333
        self._check_all_methods(s, expected)


if __name__ == "__main__":
    unittest.main()
