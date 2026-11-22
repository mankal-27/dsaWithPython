class Solution:
    def add_digits_brute_force(self, num):
        """Loop until single digit, each round sums digits with a loop.
        Time O(log n) per round (few rounds), Space O(1)."""
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num

    def add_digits_recursive(self, num):
        """Your approach, cleaned up: recursive digit sum + recursive repeat.
        Handles negatives via abs() (digital root of |num|).
        Time O(log n) per round, Space O(log n) stack."""
        num = abs(num)
        if num < 10:
            return num
        return self.add_digits_recursive(self._digit_sum(num))

    def _digit_sum(self, num):
        """Recursive digit sum: last digit + sum of remaining digits."""
        if num == 0:
            return 0
        return num % 10 + self._digit_sum(num // 10)

    def add_digits_optimized(self, num):
        """Digital root formula: 0 -> 0, else 1 + (num - 1) % 9.
        Time O(1), Space O(1)."""
        num = abs(num)
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    s = Solution()
    for n in [0, 5, 9, 10, 38, 99, 12345, 999999999, -38, 10**18]:
        assert s.add_digits_brute_force(abs(n)) == s.add_digits_recursive(n) == s.add_digits_optimized(n), n
    print("all ok")
