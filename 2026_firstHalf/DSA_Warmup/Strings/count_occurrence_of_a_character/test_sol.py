import unittest

from sol import Solution


class TestCountOccurrenceOfACharacter(unittest.TestCase):
    METHODS = [
        "count_occurrence_linear_scan",
        "count_occurrence_builtin_count",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, c, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s, c), expected)

    def test_example_1(self):
        self._check_all_methods("banana", "a", 3)

    def test_example_2(self):
        self._check_all_methods("hello", "l", 2)

    def test_empty_string(self):
        self._check_all_methods("", "a", 0)

    def test_character_never_appears(self):
        self._check_all_methods("abc", "z", 0)

    def test_every_character_matches(self):
        self._check_all_methods("aaaa", "a", 4)

    def test_case_sensitivity(self):
        self._check_all_methods("Aardvark", "a", 2)
        self._check_all_methods("Aardvark", "A", 1)

    def test_long_string_near_length_constraint(self):
        s = "x" * 999 + "y"
        self._check_all_methods(s, "x", 999)


if __name__ == "__main__":
    unittest.main()
