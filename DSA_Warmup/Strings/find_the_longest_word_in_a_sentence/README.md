# Find the Longest Word in a Sentence

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/find-the-longest-word-in-a-sentence
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a sentence s made of words separated by spaces, return the longest word in the sentence. The answer is the word itself, not its length or its position.

If two or more words share the longest length, return the first one that reaches that length. Extra spaces between words should not produce an empty word as the answer.

**Example 1**
```
Input:  s = "I love programming languages"
Output: "programming"
```

**Example 2**
```
Input:  s = "the quick brown fox"
Output: "quick"
```

**Constraints**
```
1 <= s.length <= 1000
The sentence contains at least one word.
Words are separated by spaces.
```

## How to Solve It — Thought Process

This problem is really two separate concerns stacked on top of each other, and it helps to notice that up front: first, figuring out where the words actually are in the sentence (the boundary-finding problem this repo already worked through in "Count Words in a Sentence"), and second, once the words are identified, finding the longest one (a maximum-search problem, structurally identical to finding the largest element in an array, just applied to word lengths instead of numbers). Keeping those two concerns separate makes each one simple on its own.

The most direct way to attack the first concern is to just get Python to hand back the list of words directly: calling `.split()` with no arguments treats any run of one or more spaces as a single separator and automatically discards the empty strings that a naive `split(' ')` would produce from leading, trailing, or doubled-up spaces (the same insight used in "Count Words in a Sentence" earlier in this topic). Once that list exists, the second concern — finding the longest entry — is a plain linear scan: keep track of the best word seen so far, and every time a word comes along whose length beats the current best, it becomes the new best.

The tie-breaking rule ("first word to reach that length wins") is where it's worth being careful about a single comparison operator. If the update rule were "replace the best whenever the current word's length is *at least as long*," a later word tied with the current best would overwrite it, and the answer would end up being the *last* word at the maximum length rather than the first. Using *strictly greater than* instead — only replacing the best when a word is longer, never when it's merely equal — means a tied later word is correctly ignored, leaving whichever word reached that length first still in place as the answer.

Building the whole list of words up front does cost some memory — the list holds essentially a full copy of every letter in the sentence, split apart. It's possible to avoid that entirely by never materializing separate words at all: scan the sentence character by character, and instead of extracting substrings as you go, just track *where* the word currently being read started and how many characters it's grown to. A space (or reaching the very end of the string) signals "this word is now finished" — that's the moment to compare its length against the best-so-far length and possibly update the recorded start position and length, exactly the same strictly-greater comparison as before. Reaching the end of the string needs to trigger this same "close out the current word" check, since the very last word in the sentence never gets a trailing space to signal that it's done — which is why the scan has to run one step past the last index rather than stopping exactly at the string's length.

Since finding the longest word first requires knowing where every word is, and no word's length can be known without reading through it, every character of the sentence still has to be visited in either version — the improvement from list-building to a single character scan is about avoiding *extra storage*, not about visiting fewer characters.

## Brute Force Solution — Split and Compare

```python
class Solution:
    def longest_word_split_and_compare(self, s):
        words = s.split()
        best = ""
        for word in words:
            if len(word) > len(best):
                best = word
        return best
```

## Optimized Solution — Single Pass

```python
    def longest_word_single_pass(self, s):
        best_start = 0
        best_len = 0
        cur_start = 0
        cur_len = 0
        for i in range(len(s) + 1):
            if i < len(s) and s[i] != ' ':
                if cur_len == 0:
                    cur_start = i
                cur_len += 1
            else:
                if cur_len > best_len:
                    best_len = cur_len
                    best_start = cur_start
                cur_len = 0
        return s[best_start:best_start+best_len]
```

## Additional Solution — Built-in `max()` with `key=len`

```python
    def longest_word_builtin_max(self, s):
        return max(s.split(), key=len)
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().longest_word_single_pass(s)`), not on the class directly.
>
> **Why Single Pass is "Optimized" relative to Split and Compare:** Split and Compare builds a full list of word strings via `.split()` before scanning it, which costs O(n) extra space — the list collectively holds a copy of essentially every non-space character in the sentence. Single Pass never creates that intermediate list; it tracks only a start index and a length for the current word and for the best word found so far, which is O(1) extra space (the returned slice itself is the only sizable allocation, and that's unavoidable — the answer has to be a string). Both are O(n) time, but Single Pass does the same job without the intermediate storage.
>
> **Why the built-in `max()` version counts as a genuinely different approach, not just a shorter Split and Compare:** `max(s.split(), key=len)` still builds the same word list that Split and Compare does, so it shares that O(n) space cost — but the actual "find the longest" scan is delegated entirely to Python's built-in `max()`, which runs in CPython's C implementation rather than an explicit Python `for` loop with a manual comparison. It's worth confirming the tie-breaking behavior still holds: Python's `max()` only replaces its running answer when a later element compares *strictly greater* under the given `key`, so on a tie it keeps whichever qualifying element it saw first — exactly the same first-word-wins rule the other two solutions implement explicitly.

### Algorithm — Split and Compare
1. Split the sentence into words with `.split()`, which treats runs of spaces as a single separator and discards empty words.
2. Start with an empty string as the current best word.
3. For each word, if its length is strictly greater than the best length so far, make it the new best.
4. After checking every word, return the best word.

### Algorithm — Single Pass
1. Track the start index and length of the current word, plus the best start index and best length found so far.
2. Walk through the string one character at a time, going one step past the end so the final word is closed off.
3. When the current character is non-space, extend the current word's length, marking its start if this is the first character of a new word.
4. When the current character is a space, or the scan has moved past the end, the current word is complete: if it's strictly longer than the best so far, record its start and length, then reset the current word.
5. After the scan, slice out and return the best word using its recorded start and length.

### Algorithm — Built-in `max()` with `key=len`
1. Split the sentence into words with `.split()`.
2. Call `max(words, key=len)`, which returns the first word achieving the maximum length.
3. Return the result directly.

## Dry Run

### Split and Compare — `s = "the quick brown fox"`

| Word | `len(word)` | `len(best)` before | Strictly longer? | `best` after |
|---|---|---|---|---|
| the | 3 | 0 | Yes | `"the"` |
| quick | 5 | 3 | Yes | `"quick"` |
| brown | 5 | 5 | No (tied, not strictly greater) | `"quick"` |
| fox | 3 | 5 | No | `"quick"` |

Return `"quick"`. This matches the worked example on the problem's own hints page (`brown` ties `quick`'s length but `quick` was seen first, so it wins).

### Single Pass — `s = "a bb ccc"`

| `i` | `s[i]` | Action | `cur_start` / `cur_len` | Word closed? | `best_start` / `best_len` after |
|---|---|---|---|---|---|
| 0 | a | start word | `0` / `1` | — | `0` / `0` |
| 1 | (space) | close word "a" (len 1 > 0) | reset to `0` | Yes | `0` / `1` |
| 2 | b | start word | `2` / `1` | — | `0` / `1` |
| 3 | b | extend | `2` / `2` | — | `0` / `1` |
| 4 | (space) | close word "bb" (len 2 > 1) | reset to `0` | Yes | `2` / `2` |
| 5 | c | start word | `5` / `1` | — | `2` / `2` |
| 6 | c | extend | `5` / `2` | — | `2` / `2` |
| 7 | c | extend | `5` / `3` | — | `2` / `2` |
| 8 | (past end) | close word "ccc" (len 3 > 2) | reset to `0` | Yes | `5` / `3` |

`s[5:8]` → `"ccc"`. Return `"ccc"`.

### Built-in `max()` — `s = "I love programming languages"`

`s.split()` → `["I", "love", "programming", "languages"]`. Lengths: `1, 4, 11, 9`. `max(..., key=len)` returns `"programming"` (length 11, the unique maximum). Return `"programming"`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Split and Compare | O(n) | O(n) | `.split()` builds a full list of word strings before scanning; the list's total size is proportional to the sentence length. |
| Single Pass | O(n) | O(1) beyond the output | Never builds a word list — tracks only a handful of index counters while scanning the sentence once. The most memory-efficient of the three. |
| Built-in `max()` with `key=len` | O(n) | O(n) | Same O(n) space as Split and Compare (it also calls `.split()` first), but the max-finding scan itself runs in CPython's C implementation instead of an explicit Python loop. |

## Real-World Use Case

Finding the "biggest" item in a collection according to some measurement — here, word length — is one of the most common patterns in everyday data processing, and this problem's specific combination (tokenize, then find an extreme value with a tie-breaking rule) shows up directly in several places:

- **Text analytics and readability tools** — identifying the longest word (or the longest sentence, by a similar pattern) in a document is a real metric used by some readability and writing-style analysis tools.
- **UI layout and truncation logic** — determining the longest label, word, or entry in a set of strings is a common step when sizing UI elements (column widths, button sizes) to fit their content without overflow.
- **Leaderboards and "best of" selection with tie rules** — the general pattern of "scan a collection, track the best-so-far, and use a specific tie-breaking rule (first, last, or some other criterion)" reused here is the same pattern behind leaderboard logic, finding the earliest record to hit a threshold, and similar "first winner" selection problems.
- **Word games and puzzle generators** — finding the longest valid word from a set of candidates is a direct building block in word games (Scrabble-style scoring, word-search puzzle generation, crossword construction tools).

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports which specific method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"I love programming languages"` | `"programming"` |
| `test_example_2` | `"the quick brown fox"` | `"quick"` |
| `test_single_word_sentence` | `"hello"` | `"hello"` |
| `test_tie_first_word_wins` | `"cat dog bat"` | `"cat"` (first word to reach length 3) |
| `test_multiple_consecutive_spaces` | `"the   quickest   fox"` | `"quickest"` |
| `test_leading_and_trailing_spaces` | `"   hi there world   "` | `"there"` |
| `test_longest_word_at_the_end` | `"a bb extraordinary"` | `"extraordinary"` |
| `test_long_sentence_near_length_constraint` | 109 × `"aaaaaaaa"` + one 16-char word, 997 characters | the 16-char word |

All 8 tests (24 sub-assertions across the 3 methods) pass against the current `sol.py`. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

**Update:** the first version of `longest_word_single_pass` had a bug — its bounds check read `if len(s) and s[i] != ' ':` instead of `if i < len(s) and s[i] != ' ':`, which raised `IndexError: string index out of range` on every non-empty input. That's since been fixed to properly bound `i` against `len(s)`. All 8 tests, including `longest_word_single_pass`, now pass.

Run with:
```bash
cd Strings/find_the_longest_word_in_a_sentence
python3 -m unittest -v
```
