class Solution:
    def length_of_string_char_loop(self, s):
        count = 0
        for char in s:
            count += 1
        return count

    def length_of_string_builtin_len(self, s):
        return len(s)