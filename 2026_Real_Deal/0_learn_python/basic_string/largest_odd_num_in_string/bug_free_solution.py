class Solution:
    def largest_odd_number_brute_force(self, num):
        """Check every prefix (longest first); first odd-ending one wins, then strip leading zeros.
        O(n^2) time, O(n) space."""
        for end in range(len(num), 0, -1):
            prefix = num[:end]
            if int(prefix[-1]) % 2 == 1:
                return prefix.lstrip("0")
        return ""

    def largest_odd_number_optimized(self, num):
        """Find the last odd digit, then skip leading zeros of the prefix ending there.
        O(n) time, O(1) extra space (besides the returned slice)."""
        last_odd = -1
        for index in range(len(num) - 1, -1, -1):
            if num[index] in "13579":
                last_odd = index
                break
        if last_odd == -1:
            return ""
        start = 0
        while start < last_odd and num[start] == "0":
            start += 1
        return num[start:last_odd + 1]


if __name__ == "__main__":
    solution = Solution()
    cases = [
        ("52", "5"), ("4206", ""), ("35427", "35427"), ("2468135", "2468135"),
        ("8", ""), ("7", "7"), ("", ""), ("2420", ""), ("1230", "123"),
        ("0035", "35"), ("0012", "1"), ("000", ""), ("0", ""), ("0001", "1"),
    ]
    for num, expected in cases:
        for method in (solution.largest_odd_number_brute_force, solution.largest_odd_number_optimized):
            assert method(num) == expected, (method.__name__, num)
    print("All tests passed")
