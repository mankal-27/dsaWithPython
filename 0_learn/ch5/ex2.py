# Version 1: original (case-insensitive, but compares raw characters).
# Bug/limitation: spaces and punctuation are NOT ignored, so
# "A man, a plan, a canal: Panama" returns False.
# Minor inefficiency: lower() is called twice and the reversed copy is built
# before lowercasing; the if/return True/return False is redundant.
def isPalindrome(s1):
    if s1.lower() == s1[:: -1].lower():
        return True
    return False


# Version 2: simplified, same behaviour.
# Lowercase once, return the comparison directly.
# Time O(n), space O(n) (one lowered copy + one reversed copy).
def isPalindrome_v2(s):
    s = s.lower()
    return s == s[::-1]


# Version 3: ignores non-alphanumeric characters (the usual "valid palindrome"
# definition, e.g. LeetCode 125). Fixes the bug in version 1.
# Time O(n), space O(n).
def isPalindrome_clean(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


# Version 4: two pointers, O(1) extra space, and exits early on the first
# mismatch (no copies of the string are made).
# Skips non-alphanumeric characters, so it handles the same inputs as version 3.
# Time O(n), space O(1).
def isPalindrome_two_pointers(s):
    left, right = 0, len(s) - 1
    while left < right:
        # move inward past characters we don't care about
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False  # early exit on first mismatch
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    tests = ["", "a", "Aba", "racecar", "hello", "A man, a plan, a canal: Panama", "race a car"]
    for t in tests:
        print(repr(t), isPalindrome(t), isPalindrome_v2(t),
              isPalindrome_clean(t), isPalindrome_two_pointers(t))
