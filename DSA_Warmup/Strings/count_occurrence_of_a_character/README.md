# Count Occurrence of a Character

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/count-occurrence-of-a-character
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s and a character c, return the number of times c appears in s. The answer is a plain count, so a string with no matches returns 0 rather than an error or a position.

The comparison is case sensitive. An uppercase A and a lowercase a are treated as different characters, so only an exact match adds to the count. An empty string contains nothing to match, so its answer is always 0.

**Example 1**
```
Input:  s = "banana", c = 'a'
Output: 3
```

**Example 2**
```
Input:  s = "hello", c = 'l'
Output: 2
```

**Constraints**
```
0 <= s.length <= 1000
s consists of printable ASCII characters.
c is a single character.
```

## How to Solve It — Thought Process

It's worth pausing on why this problem is a *counting* problem rather than a *searching* one, because the two look deceptively similar at first glance — both involve scanning a string for a target character. Something like "does `c` appear in `s`" or "where is the first `c`" is a search: the moment a match is found, the answer is settled and the scan can stop. This problem is different — it wants to know *how many* matches there are in total, and there's no way to know that without accounting for every single occurrence. Stopping at the first match would give the wrong answer for `"banana"` looking for `'a'`, since there are two more matches waiting further along. So unlike a search, this can't short-circuit; every character in the string has to be visited, because any one of them, including the very last, might be a match that still needs to be counted.

Once that's clear, the mechanism itself is the simplest possible version of a tally: keep a counter starting at zero, and increase it by one every time the character being visited equals `c`. Characters that don't match just get passed over without changing anything. By the time the scan reaches the end of the string, the counter has been incremented exactly once for every real match — no more, no less — so it already holds the answer.

Case sensitivity here isn't really an extra step to add; it falls out of using ordinary equality (`==`) to compare characters. `'A'` and `'a'` are different values in Python, so a straightforward `character == c` check already treats them as distinct without any special-casing — the "case sensitive" requirement in the problem statement is just describing what plain equality already does, rather than asking for something additional to be built.

The empty-string case, and the "character never appears" case, both resolve the same way any scanning approach handles a state that's never triggered: if there's nothing to iterate over (an empty string) or nothing that matches what's being iterated over (an absent character), the counter that starts at `0` is never incremented, so it correctly stays `0` all the way through.

Since every character has to be inspected to know whether it contributes to the count, a single linear pass is already the best this problem can do — there's no way to count occurrences without looking at each candidate position at least once.

## Brute Force Solution — Linear Scan (this is already optimal; every character must be inspected once to know whether it's a match, so a single linear pass can't be improved on)

```python
class Solution:
    def count_occurrence_linear_scan(self, s, c):
        count = 0
        for char in s:
            if char == c:
                count += 1
        return count
```

## Additional Solution — Built-in `str.count()`

```python
    def count_occurrence_builtin_count(self, s, c):
        return s.count(c)
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().count_occurrence_linear_scan(s, c)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a shorter version of the same loop:** `str.count()` performs exactly the same O(n) tally that the hand-written loop does, but the counting itself runs inside CPython's C implementation of the `str` type rather than as an interpreted Python `for` loop — each iteration of a Python-level loop carries interpreter overhead (bytecode dispatch, attribute lookups) that a call into a single built-in method avoids. Same algorithmic idea, same asymptotic complexity, but typically faster in practice for the same amount of work, the same tradeoff seen with `sum()`/`max()`/`len()` in earlier problems in this repo.

### Algorithm — Linear Scan
1. Initialize `count` to `0`.
2. Walk through the string one character at a time.
3. If the current character equals `c`, increment `count`.
4. After the scan, return `count`.

### Algorithm — Built-in `str.count()`
1. Call `s.count(c)`, which tallies every exact match internally.
2. Return the result directly.

## Dry Run

### Linear Scan — `s = "banana"`, `c = 'a'`

| Character | Match? | `count` after |
|---|---|---|
| b | No | 0 |
| a | Yes | 1 |
| n | No | 1 |
| a | Yes | 2 |
| n | No | 2 |
| a | Yes | 3 |

Return `3`. ✅ matches expected output.

### Linear Scan — `s = "hello"`, `c = 'l'`

| Character | Match? | `count` after |
|---|---|---|
| h | No | 0 |
| e | No | 0 |
| l | Yes | 1 |
| l | Yes | 2 |
| o | No | 2 |

Return `2`. ✅ matches expected output.

### Built-in `str.count()` — `s = "Mississippi"`, `c = 's'`

`"Mississippi".count('s')` tallies every lowercase `s` internally — the capital `M` and the four lowercase `s` characters at positions 2, 3, 5, and 6 are the only relevant characters; case sensitivity means the uppercase `M` never enters into the comparison at all, and there's no uppercase `S` in this example to worry about either. Return `4`.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Linear Scan | O(n) | O(1) | Single pass; every character is inspected once and compared to `c`. Already optimal — counting requires visiting every character, unlike a search which can stop early. |
| Built-in `str.count()` | O(n) | O(1) | Same asymptotic complexity as Linear Scan; the tally runs in CPython's C implementation instead of an interpreted loop, which is typically faster in practice for the same work. |

## Real-World Use Case

Tallying how many times a specific character appears in a body of text is a small operation that underlies a range of everyday text-processing tasks:

- **Text statistics and analytics** — character-frequency counts feed directly into things like letter-frequency analysis, simple cryptography exercises (frequency analysis of ciphertext), and basic text statistics tools.
- **Input validation** — checking that a password contains at least a certain number of a required character class, or that a formatted string (like a CSV row) has the expected number of delimiters, reduces to counting occurrences of a specific character.
- **Parsing and format checking** — verifying balanced or well-formed input (counting opening/closing delimiters, counting decimal points in a numeric string before further parsing) commonly starts with a character-occurrence count as a first, cheap sanity check.
- **Data cleaning** — flagging or filtering records based on how many times a particular character (a comma, a special symbol, a specific letter) appears is a common early step in cleaning messy text data.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"banana"`, `'a'` | 3 |
| `test_example_2` | `"hello"`, `'l'` | 2 |
| `test_empty_string` | `""`, `'a'` | 0 |
| `test_character_never_appears` | `"abc"`, `'z'` | 0 |
| `test_every_character_matches` | `"aaaa"`, `'a'` | 4 |
| `test_case_sensitivity` | `"Aardvark"`, `'a'` / `'A'` | 2 / 1 |
| `test_long_string_near_length_constraint` | `"x"*999 + "y"`, `'x'` | 999 |

**Update:** the first version of `sol.py` had a missing colon after `for char in s`, which raised a `SyntaxError` and made the whole file fail to import (documented as a "Known bug" in an earlier version of this README, with the test run then reporting a single collection-level error rather than 7 individual results). That's since been fixed — `sol.py` now imports and runs cleanly. All 7 tests (16 sub-assertions across the 2 methods) pass against the current `sol.py` — no further bugs were found in either implementation. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

Run with:
```bash
cd Strings/count_occurrence_of_a_character
python3 -m unittest -v
```
