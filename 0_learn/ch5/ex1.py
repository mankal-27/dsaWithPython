import collections


def normalize(s):
    # Drop spaces and ignore case so "Dormitory" ~ "dirty room"
    return s.replace(' ', '').lower()


def is_anagram(str1, str2):
    s1 = normalize(str1)
    s2 = normalize(str2)

    # Edge case: different lengths can never be anagrams
    if len(s1) != len(s2):
        return False

    # Two strings are anagrams if their sorted characters are identical
    # Time: O(n log n) because of sorting, Space: O(n)
    return sorted(s1) == sorted(s2)


def is_anagaram_coll(str1, str2):
    s1 = normalize(str1)
    s2 = normalize(str2)

    if len(s1) != len(s2):
        return False

    # Counter maps each char to its count; equal counts means anagram
    # Time: O(n), Space: O(n)
    return collections.Counter(s1) == collections.Counter(s2)


def is_anagram_dict(str1, str2):
    s1 = normalize(str1)
    s2 = normalize(str2)

    if len(s1) != len(s2):
        return False

    # Count up for s1, count down for s2
    # Time: O(n), Space: O(k) where k = distinct characters
    counts = {}
    for ch in s1:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in s2:
        # Char missing or used up more times than in s1 -> not an anagram
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1

    # Lengths are equal, so if no char went negative every count is 0
    return True


def is_anagram_array(str1, str2):
    # Only valid for a-z; fixed-size array instead of a dict
    s1 = normalize(str1)
    s2 = normalize(str2)

    if len(s1) != len(s2):
        return False

    # Time: O(n), Space: O(1) (always 26 slots)
    counts = [0] * 26
    for a, b in zip(s1, s2):
        counts[ord(a) - ord('a')] += 1
        counts[ord(b) - ord('a')] -= 1

    return all(c == 0 for c in counts)
