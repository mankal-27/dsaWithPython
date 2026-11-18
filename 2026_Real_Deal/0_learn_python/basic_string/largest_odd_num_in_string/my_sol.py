class Solution:
    def find_largest_odd_num_string(self, str):
        ind = -1
        for i in range(len(str)-1, -1, -1):
            if(int(str[i]) % 2 == 1):
                ind = i
                break
        i = 0
        while i <= ind and str[i] == '0':
            i += 1

        return str[i:ind + 1]

# REVIEW (logic is correct; no functional bug found):
# - The leading-zero skip is REQUIRED: input may have leading zeros, output must not
#   (e.g. "0035" -> "35"). Your loop handles it correctly.
# - STYLE: parameter `str` shadows the built-in; `if(...)` parentheses.
# - NOTE: `str[i] in "13579"` avoids converting each char with int().
# - File had no trailing newline.
