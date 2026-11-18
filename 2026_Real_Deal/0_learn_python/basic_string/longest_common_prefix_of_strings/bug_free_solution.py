class Solution:
    def longest_common_prefix_brute_force(self, strs):
        """Take the first string as candidate prefix; shrink it until every string starts with it.
        O(n * m) time (n strings, m = shortest length), O(1) extra space."""
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

    def longest_common_prefix_optimized(self, strs):
        """Sort, then only the lexicographically smallest and largest strings can differ most,
        so compare just those two. O(n log n * m) time, O(1) extra space beyond the sort."""
        if not strs:
            return ""
        ordered = sorted(strs)
        first, last = ordered[0], ordered[-1]
        length = 0
        limit = min(len(first), len(last))
        while length < limit and first[length] == last[length]:
            length += 1
        return first[:length]


if __name__ == "__main__":
    solution = Solution()
    cases = [
        (["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""),
        (["single"], "single"), ([], ""), ([""], ""), (["", "a"], ""),
        (["a", "a"], "a"), (["abc", "abc", "abc"], "abc"), (["ab", "abc"], "ab"),
        (["flower", "flight", "flow"], "fl"), (["c", "acc", "ccc"], ""),
    ]
    for strs, expected in cases:
        for method in (solution.longest_common_prefix_brute_force, solution.longest_common_prefix_optimized):
            assert method(list(strs)) == expected, (method.__name__, strs)
    print("All tests passed")
