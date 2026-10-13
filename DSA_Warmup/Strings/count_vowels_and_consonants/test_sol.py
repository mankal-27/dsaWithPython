import unittest

from sol import Solution


class TestCountVowelsAndConsonants(unittest.TestCase):
    METHODS = [
        "count_vowels_and_consonants_linear_scan",
        "count_vowels_and_consonants_builtin",
    ]

    def setUp(self):
        self.sol = Solution()

    def _check_all_methods(self, s, expected):
        for name in self.METHODS:
            method = getattr(self.sol, name)
            with self.subTest(method=name):
                self.assertEqual(method(s), expected)

    def test_example_1(self):
        self._check_all_methods("hello", [2, 3])

    def test_example_2_with_digits_and_space(self):
        self._check_all_methods("abc123 xy", [1, 4])

    def test_empty_string(self):
        self._check_all_methods("", [0, 0])

    def test_mixed_case_vowels(self):
        # confirms case-insensitivity: A, E, I, O, U all count as vowels
        self._check_all_methods("AEIOUbcd", [5, 3])

    def test_no_vowels(self):
        self._check_all_methods("bcdfg", [0, 5])

    def test_no_consonants(self):
        self._check_all_methods("aeiou", [5, 0])

    def test_no_letters_at_all(self):
        self._check_all_methods("123 !@#", [0, 0])

    def test_long_string_near_length_constraint(self):
        s = "bcdfg" * 2000  # 10,000 characters, all consonants
        self._check_all_methods(s, [0, 10000])


if __name__ == "__main__":
    unittest.main()
