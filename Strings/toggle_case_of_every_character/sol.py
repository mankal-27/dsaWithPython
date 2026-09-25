class Solution:
    def toggle_case_ascii_arithmetic(self, s):
        result = []
        for char in s:
            code = ord(char)
            if ord('A') <= code <= ord('Z'):
                result.append(chr(code + 32))
            elif ord('a') <= code <= ord('z'):
                result.append(chr(code - 32))
            else:
                result.append(char)
        return "".join(result)

    def toggle_case_builtin_swapcase(self, s):
        return s.swapcase()
