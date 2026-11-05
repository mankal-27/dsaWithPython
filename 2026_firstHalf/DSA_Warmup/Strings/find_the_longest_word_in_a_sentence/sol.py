class Solution:
    def longest_word_split_and_compare(self, s):
        words = s.split()
        best = ""
        for word in words:
            if len(word) > len(best):
                best = word
        return best

    def longest_word_single_pass(self, s):
        best_start = 0
        best_len = 0
        cur_start = 0
        cur_len = 0
        for i in range(len(s) + 1):
            if i < len(s) and s[i] != ' ':
                if cur_len == 0:
                    cur_start = i
                cur_len += 1
            else:
                if cur_len > best_len:
                    best_len = cur_len
                    best_start = cur_start
                cur_len = 0
        return s[best_start:best_start+best_len]

    def longest_word_builtin_max(self, s):
        return max(s.split(), key=len)
