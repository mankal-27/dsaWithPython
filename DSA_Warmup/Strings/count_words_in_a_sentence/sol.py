class Solution:
    def count_words_strip_split(self, s):
        trimmed = s.strip()
        if not trimmed:
            return 0
        parts = trimmed.split(' ')
        count = 0
        for part in parts:
            if part:
                count += 1
        return count

    def count_words_transition_counting(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or (s[i - 1]) == ' '):
                count += 1
        return count

    def count_words_builtin_split(self, s):
        return len(s.split())
