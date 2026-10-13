class Solution:
    def replace_spaces_linear_scan(self, s, ch):
        result = []
        for char in s:
            if char == " ":
                result.append(ch)
            else:
                result.append(char)
        return "".join(result)

    def replace_spaces_builtin_replace(self, s, ch):
        return s.replace(' ', ch)
