class Solution:
    def longest_common_prefix_string(self, s):
        n = len(s)
        s.sort()

        first = s[0]
        last = s[n - 1]

        ans = ""
       
        for i in range(0, min(len(first), len(last)) ):
            print(i,first[i])
            print(i, last[i])
            if(first[i] != last[i]):
                break
            ans += first[i]
        return ans

s = Solution()
ex = ["single"]
result = s.longest_common_prefix_string(ex)
print(result)

# ---- REVIEW NOTES (bugs) ----
# 1. BUG: `sorted(s)` returns a NEW list and its result is discarded, so `s` is never sorted.
#    first/last are just the original first/last strings. Fails e.g. ["flower","flight","flow"] -> "flow" (expected "fl").
#    Fix: `s = sorted(s)` or `s.sort()`.
# 2. BUG: empty list crashes (`s[0]` IndexError). Return "" first.
# 3. The idea (after sorting, compare only first and last) is correct: they differ the most.
# 4. STYLE: debug prints, `min(len-1, len-1) + 1` is just `min(len, len)`, `if(...)` parentheses.
