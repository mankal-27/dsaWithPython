class Solution:
    def count_vowels_and_consonants_linear_scan(self, s):
        vowels = 0
        consonants = 0
        vowel_set = "aeiou"
        for char in s:
            lowered = char.lower()
            if not lowered.isalpha():
                continue
            if lowered in vowel_set:
                vowels += 1
            else:
                consonants += 1
        return [vowels, consonants]

    def count_vowels_and_consonants_builtin(self, s):
        lowered = s.lower()
        vowels = sum(1 for char in lowered if char in "aeiou")
        consonants = sum(1 for char in lowered if char.isaplha() and char not in "aeiou")
        return [vowels, consonants]
