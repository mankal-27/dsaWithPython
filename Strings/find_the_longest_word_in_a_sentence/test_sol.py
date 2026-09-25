import unittest

from sol import Solution


class TestFindTheLongestWordInASentence(unittest.TestCase):
    METHODS = [
        "longest_word_split_and_compare",
        "longest_word_single_pass",
        "longest_word_builtin_max",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s), expected)

    def test_example_1(self):
        self._check_all_methods("I love programming languages", "programming")

    def test_example_2(self):
        self._check_all_methods("the quick brown fox", "quick")

    def test_single_word_sentence(self):
        self._check_all_methods("hello", "hello")

    def test_tie_first_word_wins(self):
        # "cat", "dog", "bat" are all length 3 -> first one wins
        self._check_all_methods("cat dog bat", "cat")

    def test_multiple_consecutive_spaces(self):
        self._check_all_methods("the   quickest   fox", "quickest")

    def test_leading_and_trailing_spaces(self):
        self._check_all_methods("   hi there world   ", "there")

    def test_longest_word_at_the_end(self):
        self._check_all_methods("a bb extraordinary", "extraordinary")

    def test_long_sentence_near_length_constraint(self):
        # 997 characters: 109 words of "aaaaaaaa" (8 chars) separated by
        # single spaces, ending with one 16-char word as the unique longest.
        words = ["aaaaaaaa"] * 109 + ["b" * 16]
        s = " ".join(words)
        self.assertLessEqual(len(s), 1000)
        self._check_all_methods(s, "b" * 16)


if __name__ == "__main__":
    unittest.main()
