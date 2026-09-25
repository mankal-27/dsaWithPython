class Solution:
    def count_occurrence_linear_scan(self, s, c):
        count = 0
        for char in s:
            if char == c:
                count += 1
        return count

    def count_occurrence_builtin_count(self, s, c):
        return s.count(c)
