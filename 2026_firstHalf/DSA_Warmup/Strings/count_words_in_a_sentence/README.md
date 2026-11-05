# Count Words in a Sentence

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/count-words-in-a-sentence
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s, count the number of words it contains. A word is a contiguous run of non-space characters, and words are separated by one or more spaces.

Handle leading spaces, trailing spaces, and multiple spaces between words correctly. An empty string or a string of only spaces contains zero words.

**Example 1**
```
Input:  s = "hello world"
Output: 2
```

**Example 2**
```
Input:  s = "  leading and trailing  "
Output: 3
```

**Constraints**
```
0 <= s.length <= 10^4
s consists of printable ASCII characters, including spaces.
```

## How to Solve It — Thought Process

The obvious first instinct, if you already know a string can be split apart, is to just split this one on spaces and count how many pieces come back. That instinct is directionally right — words are exactly what's left between the spaces — but it runs into trouble the moment the spacing isn't clean. Splitting `"  leading and trailing  "` on a single space character produces `["", "", "leading", "and", "trailing", "", ""]`: every run of consecutive spaces, and the leading/trailing spaces themselves, manufactures an empty string in the result, because splitting on a literal `' '` treats every space as its own separator regardless of what's next to it. So a plain split-and-count would report 7 "words" instead of 3. The fix that keeps this approach honest is to strip the string's outer spaces first (so the ends don't contribute empty pieces) and then explicitly discard any empty piece left over from a run of multiple spaces in the middle — counting only the pieces that actually have characters in them.

That works, but it's doing more than it needs to: it builds a whole list of substrings (some of which are immediately thrown away) just to answer a question that's really about counting, not splitting. Stepping back, a "word" isn't really a piece of the string that has to be extracted — it's a *moment* that happens exactly once per word: the instant a non-space character shows up right after either a space or the very beginning of the string. That's the one and only point where a new word "starts." If instead of splitting the string you just walk through it once and count those starting moments, you never have to build or discard anything — you're counting events during a single pass rather than materializing pieces and filtering them afterward. A character at position `i` marks such a start exactly when it isn't a space, and either `i` is the very first position or the character right before it was a space. Multiple spaces between words don't cause any problem here, because only the *first* non-space character after a run of spaces satisfies "the character before me is a space" — every character after that first one in the same word has another non-space character right before it, so it doesn't trigger a second count.

The empty-string and all-spaces cases fall out of this the same way they always do with a scanning approach: if there are no characters, or every character is a space, the "non-space that follows a space or the start" condition is never true anywhere in the string, so the counter that starts at `0` simply never gets incremented.

Since Python's `str.split()` already implements exactly the "trim the ends, split on runs of whitespace" behavior for free when called with no arguments — unlike `split(' ')`, which splits on every single space character and is what produces the empty-string problem above — there's also a Pythonic one-liner that sidesteps the whole issue: split with no argument and count what comes back.

## Brute Force Solution — Strip and Split (builds and filters a list of substrings; works, but does more work than it needs to)

```python
class Solution:
    def count_words_strip_split(self, s):
        trimmed = s.strip()
        if not trimmed:
            return 0
        parts = trimmed.split(' ')
        count = 0
        for part in parts:
            if part:
                count += 1
        return count
```

## Optimized Solution — Transition Counting

```python
    def count_words_transition_counting(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or (s[i - 1]) == ' '):
                count += 1
        return count
```

## Additional Solution — Built-in `str.split()` with No Arguments

```python
    def count_words_builtin_split(self, s):
        return len(s.split())
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().count_words_transition_counting(s)`), not on the class directly.
>
> **Why Transition Counting is "Optimized" relative to Strip and Split:** Strip and Split builds an entire list of substrings (`trimmed.split(' ')`) — including the empty strings from any run of repeated spaces — just to filter most of it away, which costs O(n) extra space for that intermediate list. Transition Counting never materializes any substrings at all; it looks at each character (and, at most, the one character before it) and updates a single integer counter, which is O(1) extra space rather than O(n). Both are O(n) time, but Transition Counting does the same job with strictly less memory and no wasted allocation.
>
> **Why `str.split()` with no arguments counts as a genuinely different (and simplest) approach:** calling `.split()` with *no* separator argument isn't the same operation as `.split(' ')` — Python special-cases the no-argument form to split on any run of whitespace and to automatically discard leading/trailing whitespace, which is precisely the "trim, then split on runs of spaces" logic that the Brute Force solution above has to implement by hand (`.strip()` plus a manual empty-string filter). That built-in behavior collapses the whole problem into one line, `len(s.split())`, at the cost of the same O(n) space for the resulting list that Strip and Split has, but without needing any of the manual filtering.

### Algorithm — Strip and Split
1. Strip leading and trailing spaces from `s`.
2. If the trimmed string is empty, return `0`.
3. Split the trimmed string on single-space characters.
4. Count how many of the resulting pieces are non-empty (a run of multiple spaces produces empty pieces between the real words; discard those).
5. Return that count.

### Algorithm — Transition Counting
1. Initialize `count` to `0`.
2. Walk through the string by index, from the first character to the last.
3. At index `i`, check whether `s[i]` is a non-space character.
4. If it is non-space, and either `i == 0` or `s[i - 1]` is a space, a new word has started — increment `count`.
5. After the scan, return `count`.

### Algorithm — Built-in `str.split()`
1. Call `s.split()` with no argument — Python trims the string and splits it on any run of whitespace, discarding empty pieces automatically.
2. Return the length of the resulting list.

## Dry Run

### Strip and Split — `s = "  leading and trailing  "`

1. `s.strip()` → `"leading and trailing"` (outer spaces removed).
2. `"leading and trailing".split(' ')` → `["leading", "and", "trailing"]` (single spaces between words, so no empty pieces here).
3. All 3 pieces are non-empty → `count = 3`.

Return `3`. ✅ matches expected output.

### Transition Counting — `s = " a  bb"`

| `i` | `s[i]` | Non-space? | `i == 0` or `s[i-1] == ' '`? | New word starts? | `count` after |
|---|---|---|---|---|---|
| 0 | (space) | No | — | No | 0 |
| 1 | a | Yes | Yes (`s[0]` is a space) | Yes | 1 |
| 2 | (space) | No | — | No | 1 |
| 3 | (space) | No | — | No | 1 |
| 4 | b | Yes | Yes (`s[3]` is a space) | Yes | 2 |
| 5 | b | Yes | No (`s[4]` is `b`, not a space) | No | 2 |

Return `2`. This matches the worked example on the problem's own hints page (` a  bb` → 2 words: "a" and "bb").

### Built-in `str.split()` — `s = "hello world"`

`"hello world".split()` (no argument) → `["hello", "world"]`. `len([...])` → `2`. Return `2`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Strip and Split | O(n) | O(n) | `.strip()` and `.split(' ')` each scan the string once; the resulting list of pieces (including the discarded empty ones from repeated spaces) is proportional to the input length. |
| Transition Counting | O(n) | O(1) | A single pass; each character is inspected once, with at most a one-character lookback. Only a counter is kept, regardless of input size — the most memory-efficient of the three. |
| Built-in `str.split()` | O(n) | O(n) | Same asymptotic time as the others; Python's C implementation handles the whitespace-trimming and run-collapsing internally, at the same O(n) space cost as Strip and Split for the resulting list, but with none of the manual filtering. |

## Real-World Use Case

Counting words by scanning for the boundaries between them, rather than materializing every substring, is a pattern that shows up anywhere text needs to be measured or tokenized efficiently:

- **Word-count and readability tools** — document editors and writing tools (word processors, blogging platforms, essay/character-limit checkers) need a running word count, and the transition-counting technique is exactly how that can be computed in a single pass without allocating a token list.
- **Text editors and IDEs** — features like "jump to next word" or "select word" rely on the same space-to-non-space transition logic to find word boundaries as the cursor moves through text.
- **Log and command-line parsing** — splitting a command line or a log line into tokens while correctly handling multiple/irregular whitespace is a direct application of this same word/token boundary detection.
- **Search indexing and NLP preprocessing** — tokenizing raw text into words before further processing (indexing, stemming, embedding) commonly needs to handle exactly the messy-whitespace cases this problem calls out: leading, trailing, and repeated spaces.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports exactly which method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"hello world"` | 2 |
| `test_example_2_leading_and_trailing_and_multiple_spaces` | `"  leading and trailing  "` | 3 |
| `test_empty_string` | `""` | 0 |
| `test_only_spaces` | `"     "` | 0 |
| `test_single_word_no_surrounding_spaces` | `"single"` | 1 |
| `test_multiple_consecutive_spaces_between_words` | `"multiple   spaces   here"` | 3 |
| `test_leading_spaces_only` | `"  leading"` | 1 |
| `test_trailing_spaces_only` | `"trailing  "` | 1 |
| `test_long_string_near_length_constraint` | `("a  " * 3333).strip()` (9,997 characters) | 3333 |

All 9 tests (27 sub-assertions across the 3 methods) pass against the current `sol.py` — no bugs were found in any of the three implementations. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

Run with:
```bash
cd Strings/count_words_in_a_sentence
python3 -m unittest -v
```
