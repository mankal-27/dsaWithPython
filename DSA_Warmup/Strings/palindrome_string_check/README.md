# Palindrome String Check

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/palindrome-string-check
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s made of lowercase alphanumeric characters, return true if it reads the same forward and backward, and false otherwise.

The input is already lowercase with no spaces or punctuation, so the characters can be compared directly. An empty string and a single character both count as palindromes, since there is no mismatched pair.

**Example 1**
```
Input:  s = "racecar"
Output: true
```

**Example 2**
```
Input:  s = "hello"
Output: false
```

**Constraints**
```
0 <= s.length <= 1000
The string contains only lowercase alphanumeric characters.
```

## How to Solve It — Thought Process

"Reads the same forward and backward" translates almost literally into code once you notice it's really a claim about *equality*: a string is a palindrome exactly when it's identical to its own reverse. That gives an immediate, very direct way to check it — construct the reversed version of the string, and compare the two. Nothing about the algorithm needs to be clever here; it just needs a way to build the reverse, which can be done the same way any sequence gets reversed by hand: walk from the last character back to the first, building up a new string one character at a time.

The catch with that approach is that it does more work than the question actually needs. Checking "is this a palindrome" doesn't require ever producing the reversed string as a standalone object — it only requires confirming that each character has a matching mirror-image partner somewhere else in the same string. The first and last characters need to match each other, the second and second-to-last need to match each other, and so on, converging toward the middle. That's a comparison that can be done entirely *in place*, on the original string, without ever allocating a second one: keep one index that starts at the front and another that starts at the back, compare the characters they point at, and if they ever disagree, the string isn't a palindrome — stop immediately, no need to check anything else. If they agree, step the front index forward and the back index backward and repeat. Once the two indices meet or pass each other, every pair has been checked and agreed, so the string is a palindrome.

This in-place, two-pointer approach has two real advantages over building the reversed copy: it doesn't need the extra memory to hold a second string, and it can bail out the instant it finds a mismatch — for a string that fails early (like `"hello"`, which fails on the very first comparison, `h` vs `o`), the reversed-copy approach still had to build the entire reverse before it could even start comparing, while the two-pointer approach never looks past the first disagreement.

The empty-string and single-character cases both work out for free with the two-pointer approach specifically because of how the loop's stopping condition is phrased: the loop only runs `while left < right`. For an empty string, `left = 0` and `right = -1`, so `left < right` is already false and the loop body never executes — no mismatch is ever found, so it's correctly reported as a palindrome. For a single character, `left` and `right` both start at index `0`, so `left < right` is false immediately for the same reason — there's no second character to compare against, so nothing can disagree.

Since the problem statement guarantees the input is already lowercase with no spaces or punctuation, there's no normalization step needed before comparing characters — unlike a "real-world" palindrome checker (which typically has to fold case and strip non-alphanumeric characters first), this version can compare characters exactly as they appear.

## Brute Force Solution — Reverse and Compare

```python
class Solution:
    def palindrome_check_reverse_and_compare(self, s):
        reversed_char = []
        for i in range(len(s) - 1, -1, -1):
            reversed_char.append(s[i])
        reversed_s = "".join(reversed_char)
        return s == reversed_s
```

## Optimized Solution — Two Pointers

```python
    def palindrome_check_two_pointers(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

## Additional Solution — Built-in Slice Reversal

```python
    def palindrome_check_builtin_slice(self, s):
        return s == s[::-1]
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().palindrome_check_two_pointers(s)`), not on the class directly.
>
> **Why Two Pointers is "Optimized" relative to Reverse and Compare:** Reverse and Compare has to build an entirely new string holding every character of `s` before it can compare anything, which costs O(n) extra space and means it always does the full amount of work even when the answer becomes obvious almost immediately (e.g. `"hello"` fails on the very first character pair). Two Pointers never allocates a second string — it compares mirrored characters directly on the original — so it uses O(1) extra space, and it returns `False` the instant it finds a mismatch instead of finishing a full reversal first.
>
> **Why the built-in slice version is kept separate from Reverse and Compare, not merged with it:** `s[::-1]` and the hand-written reversal loop both build a full reversed copy of the string, so asymptotically they're doing the same O(n) time, O(n) space work — but `s[::-1]` is Python's built-in step-slicing syntax, implemented in C, rather than a Python-level loop appending characters one at a time and then joining them. It's included as its own "Additional Solution" because it's the version most Python developers would actually reach for in practice, even though the underlying algorithmic idea is identical to the Brute Force solution above.

### Algorithm — Reverse and Compare
1. Build a new string holding the characters of `s` in reverse order.
2. Compare the reversed string with the original `s`.
3. Return `True` if they're equal, `False` otherwise.

### Algorithm — Two Pointers
1. Set `left = 0` and `right = len(s) - 1`.
2. While `left < right`, compare `s[left]` and `s[right]`.
3. If they differ, return `False` immediately.
4. Otherwise, increment `left` and decrement `right`, and repeat.
5. If the loop finishes without a mismatch, return `True`.

### Algorithm — Built-in Slice Reversal
1. Build the reversed string in one step with `s[::-1]`.
2. Compare it to `s` and return the result of that comparison directly.

## Dry Run

### Reverse and Compare — `s = "abca"`

| `i` | `s[i]` | `reversed_char` after append |
|---|---|---|
| 3 | a | `['a']` |
| 2 | c | `['a', 'c']` |
| 1 | b | `['a', 'c', 'b']` |
| 0 | a | `['a', 'c', 'b', 'a']` |

`reversed_s = "acba"`. Compare `"abca" == "acba"` → `False`. Return `False`. This matches the worked example on the problem's own hints page (`"abca"` is not a palindrome).

### Two Pointers — `s = "racecar"`

| `left` | `right` | `s[left]` | `s[right]` | Match? | Action |
|---|---|---|---|---|---|
| 0 | 6 | r | r | Yes | `left=1, right=5` |
| 1 | 5 | a | a | Yes | `left=2, right=4` |
| 2 | 4 | c | c | Yes | `left=3, right=3` |

`left < right` is now `3 < 3` → `False`, loop ends with no mismatch found. Return `True`. ✅ matches expected output.

### Built-in Slice Reversal — `s = "hello"`

`s[::-1]` → `"olleh"`. Compare `"hello" == "olleh"` → `False`. Return `False`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Reverse and Compare | O(n) | O(n) | Builds a full reversed copy via a hand-written loop before comparing; always does the full amount of work regardless of where a mismatch (if any) occurs. |
| Two Pointers | O(n) worst case | O(1) | No extra copy — compares mirrored characters directly on the original string, with only two index variables as extra state. Returns `False` on the first mismatch found, so a non-palindrome that fails early finishes faster in practice. |
| Built-in Slice Reversal | O(n) | O(n) | Same asymptotic complexity as Reverse and Compare — still builds a full reversed copy — but the reversal is done by Python's built-in slicing (implemented in C) instead of a hand-written loop. |

## Real-World Use Case

Checking whether a sequence reads the same forwards and backwards, and the two-pointer "converge from both ends" technique specifically, come up well beyond just string puzzles:

- **Data validation with symmetric formats** — validating identifiers that are designed to be palindromic as a built-in checksum-like property (some numbering schemes use this) reuses this exact check.
- **DNA and bioinformatics** — detecting palindromic sequences in DNA (regions that read the same on the complementary strand) is a real, common operation in computational biology, built on the same forward/backward comparison idea.
- **Two-pointer technique generally** — the "start from both ends and converge" pattern used here is a foundational technique reused far beyond palindromes: it's the same approach behind problems like "reverse an array in place" (seen earlier in this repo), finding a pair in a sorted array that sums to a target, and partitioning problems.
- **Text and puzzle games** — palindrome detection is a direct building block in word games, puzzle generators, and text-based coding challenges/interview screens, which is exactly the context this problem itself comes from.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports exactly which method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"racecar"` | True |
| `test_example_2_not_a_palindrome` | `"hello"` | False |
| `test_empty_string` | `""` | True |
| `test_single_character` | `"a"` | True |
| `test_even_length_palindrome` | `"abba"` | True |
| `test_odd_length_palindrome_with_middle_character` | `"level"` | True |
| `test_fails_on_first_character_pair` | `"zello"` | False (exercises the Two Pointers early-exit path) |
| `test_alphanumeric_palindromes` | `"1221"`, `"12321"` | True |
| `test_long_palindrome_near_length_constraint` | `"ab"*250 + ("ab"*250)[::-1]` (1,000 characters, even-length) | True |

All 9 tests (25 sub-assertions across the 3 methods) pass against the current `sol.py` — no bugs were found in any of the three implementations. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

Run with:
```bash
cd Strings/palindrome_string_check
python3 -m unittest -v
```
