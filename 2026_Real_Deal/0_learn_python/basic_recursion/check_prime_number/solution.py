class Solution:
    def check_prime_brute_force(self, num):
        """Try every divisor 2..num-1. O(n) time, O(1) space."""
        if num <= 1:
            return False
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True

    def check_prime_recursive(self, num):
        """Your approach: recursive trial division up to sqrt(num).
        O(sqrt n) time, O(sqrt n) stack. RecursionError for primes > ~1e6."""
        if num <= 1:
            return False

        def helper(divisor):
            if divisor * divisor > num:
                return True
            if num % divisor == 0:
                return False
            return helper(divisor + 1)

        return helper(2)

    def check_prime_optimized(self, num):
        """Trial division up to sqrt(num), skipping evens, iterative (no
        recursion limit). O(sqrt n) time, O(1) space."""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True


if __name__ == "__main__":
    s = Solution()
    for n in range(-3, 500):
        assert s.check_prime_brute_force(n) == s.check_prime_recursive(n) == s.check_prime_optimized(n)
    assert s.check_prime_optimized(1_000_000_007)
    assert not s.check_prime_optimized(1_000_000_007 * 3)
    print("all ok")
