# Count Vowels and Consonants

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/count-vowels-and-consonants
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s, count how many characters are vowels and how many are consonants. Vowels are a, e, i, o, and u, compared without regard to case. A consonant is any other letter of the alphabet.

Return the result as an array [vowelCount, consonantCount]. Ignore digits, spaces, and other characters that are not letters.

**Example 1**
```
Input:  s = "hello"
Output: [2, 3]
```

**Example 2**
```
Input:  s = "abc123 xy"
Output: [1, 4]
```

**Constraints**
```
0 <= s.length <= 10^4
s consists of printable ASCII characters.
```

## How to Solve It — Thought Process

This is really two decisions layered on top of the same single-pass counting pattern from "Length of a String": instead of incrementing one counter for every character, each character now has to be sorted into one of three buckets — vowel, consonant, or "doesn't count at all" — before anything gets incremented. So the core loop shape doesn't change; what changes is that each visit now needs a short chain of classification questions before it updates a counter.

The case-insensitivity requirement is the kind of detail that's easy to handle badly by duplicating work — checking a character against both `'A'`/`'a'`, `'E'`/`'e'`, and so on would mean ten comparisons where five would do. The cleaner move is to normalize the character once, by lowercasing it, and then only ever compare against the five lowercase vowels. That converts a case-insensitive problem into a case-sensitive one before any comparison happens, which is generally the right order of operations whenever "insensitive to X" shows up in a requirement — normalize first, compare second.

The "ignore anything that isn't a letter" requirement is where it matters to get the *order* of the checks right. A digit or a space has to be filtered out before asking "is this a vowel," because neither a digit nor a space is a vowel *or* a consonant — it's simply not part of either count. So the natural structure per character is: first ask "is this even a letter," and only if the answer is yes, ask the second question of "is it one of the five vowels, or everything else (a consonant)." Skipping the first question would silently miscount, since a bare `if char in vowels / else consonant` split would wrongly file every digit and space into the consonant bucket.

Python offers a cleaner way to ask "is this a letter" than the ASCII-range check (`'a' <= c <= 'z'`) that a language without a built-in classifier would reach for: `str.isalpha()` directly answers "is this character alphabetic," which reads as exactly what the requirement says and sidesteps needing to hardcode the alphabet's boundary characters. Since this problem is squarely about classifying characters, letting the string type's own classification method do that first filtering step (rather than reimplementing the ASCII range test by hand) is a good fit here specifically, even though the counting loop around it is still hand-written.

Since every character must be inspected once to know which bucket it belongs in, and there's no way to determine vowel/consonant/other membership without looking at the character itself, a single linear pass is already the best this problem can do — there's no algorithmic shortcut past "look at each character."

## Brute Force Solution — Linear Scan (this is already optimal; every character must be classified individually, so a single linear pass can't be improved on)

```python
class Solution:
    def count_vowels_and_consonants_linear_scan(self, s):
        vowels = 0
        consonants = 0
        vowel_set = "aeiou"
        for char in s:
            lowered = char.lower()
            if not lowered.isalpha():
                continue
            if lowered in vowel_set:
                vowels += 1
            else:
                consonants += 1
        return [vowels, consonants]
```

## Additional Solution — Built-in `sum()` with Generator Expressions

**⚠️ Known bug:** as implemented, this method has a typo that crashes with an `AttributeError` on any input that reaches the `consonants` line's generator body — see the "Known bug" note directly under the code for the confirmed, traced behavior.

```python
    def count_vowels_and_consonants_builtin(self, s):
        lowered = s.lower()
        vowels = sum(1 for char in lowered if char in "aeiou")
        consonants = sum(1 for char in lowered if char.isaplha() and char not in "aeiou")
        return [vowels, consonants]
```

> **⚠️ Known bug — misspelled `.isalpha()`:** the `consonants` line calls `char.isaplha()` (two letters transposed) instead of `char.isalpha()`. `str` has no `isaplha` attribute, so this raises `AttributeError: 'str' object has no attribute 'isaplha'` the moment the generator actually evaluates that condition for a character. Confirmed trace for `s = "hello"`: `vowels` computes fine (`sum()` over the first generator never touches the typo), but the `consonants` line's generator starts iterating `"hello"`, and as soon as it reaches the first character, evaluating `char.isaplha()` raises the `AttributeError` immediately — the method never returns. Because Python generator expressions are lazy, the *only* input that avoids the crash is one where the `consonants` generator has nothing to iterate over at all: an empty string. Any string with at least one character reaches the typo and crashes, regardless of whether that character is a vowel, a consonant, a digit, or punctuation — even `"123"` crashes, since the generator still visits `'1'` and calls `.isaplha()` on it before the `and` can short-circuit. This is reported here, not silently fixed — see `test_sol.py` below for the tests that confirm this behavior against the real code (1 pass, 7 errors out of 8 tests).
>
> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().count_vowels_and_consonants_linear_scan(s)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a rephrasing:** rather than classifying each character once per pass and routing it to one of two counters inline, this version expresses each count as its own declarative query — "how many lowercase characters are vowels" and "how many lowercase characters are letters that aren't vowels" — using `sum()` over a generator expression for each. The tradeoff is that it scans the (already-lowercased) string twice, once per `sum()` call, instead of the single pass the hand-written loop makes, so it does strictly more character visits for the same O(n) asymptotic work — in exchange for two short, self-contained expressions that each read like the definition of what they're counting, rather than a loop body juggling two counters and an `if`/`else` at once. (This intended tradeoff is unaffected by the typo bug above — the bug is a plain misspelling, not a flaw in the approach itself.)

### Algorithm — Linear Scan
1. Initialize `vowels` to `0` and `consonants` to `0`.
2. Walk through the string one character at a time.
3. Lowercase the current character.
4. If the lowercased character isn't alphabetic, skip it.
5. If it's one of `a`, `e`, `i`, `o`, `u`, increment `vowels`; otherwise increment `consonants`.
6. After the scan, return `[vowels, consonants]`.

### Algorithm — Built-in `sum()` with Generator Expressions
1. Lowercase the whole string once, up front.
2. Count characters that are in the vowel set with one `sum()` over a generator expression.
3. Count characters that are alphabetic but not in the vowel set with a second `sum()` over a generator expression.
4. Return `[vowels, consonants]`.

## Dry Run

### Linear Scan — `s = "hello"`

| Character | Lowercased | Is a letter? | Vowel? | `vowels` after | `consonants` after |
|---|---|---|---|---|---|
| h | h | Yes | No | 0 | 1 |
| e | e | Yes | Yes | 1 | 1 |
| l | l | Yes | No | 1 | 2 |
| l | l | Yes | No | 1 | 3 |
| o | o | Yes | Yes | 2 | 3 |

Return `[2, 3]`. ✅ matches expected output.

### Linear Scan — `s = "abc123 xy"`

| Character | Lowercased | Is a letter? | Vowel? | `vowels` after | `consonants` after |
|---|---|---|---|---|---|
| a | a | Yes | Yes | 1 | 0 |
| b | b | Yes | No | 1 | 1 |
| c | c | Yes | No | 1 | 2 |
| 1 | 1 | No | — | 1 | 2 (skipped) |
| 2 | 2 | No | — | 1 | 2 (skipped) |
| 3 | 3 | No | — | 1 | 2 (skipped) |
| (space) | (space) | No | — | 1 | 2 (skipped) |
| x | x | Yes | No | 1 | 3 |
| y | y | Yes | No | 1 | 4 |

Return `[1, 4]`. ✅ matches expected output.

### Built-in `sum()` (intended) — `s = "Programming"`

Lowercased once: `"programming"`. First `sum()`: characters in `"aeiou"` are `o`, `a`, `i` → `vowels = 3`. Second `sum()`: alphabetic characters not in `"aeiou"` are `p`, `r`, `g`, `r`, `m`, `m`, `n`, `g` → `consonants = 8`. Intended return: `[3, 8]` — matches the worked example given on the problem's own hints page. This is what the *intended* code (with `.isalpha()` spelled correctly) produces.

### Built-in `sum()` (as implemented) — `s = "hello"`

| Step | What happens |
|---|---|
| `lowered = "hello"` | No issue — `.lower()` is spelled correctly. |
| `vowels = sum(...)` | No issue — this generator never calls `.isaplha()`. Evaluates to `2` (`e`, `o`). |
| `consonants = sum(...)` | The generator starts iterating `"hello"`. At the first character `h`, it evaluates `char.isaplha()` → **raises `AttributeError: 'str' object has no attribute 'isaplha'`.** The method never reaches `return`. |

Actual result: crashes with `AttributeError` instead of returning `[2, 3]`. ❌ does not match the expected output — confirmed via direct execution (see the "Known bug" callout above and the `test_sol.py` results below).

## Complexity

| Approach | Time Complexity (intended) | Space Complexity (intended) | Notes |
|---|---|---|---|
| Linear Scan | O(n) | O(1) | Single pass; each character is classified once and routed to one of two counters. Already optimal — every character must be inspected to know which bucket it belongs in. Matches actual implementation — no bugs found. |
| Built-in `sum()` with Generator Expressions | O(n) | O(n) for the lowercased copy | **As implemented: crashes with `AttributeError` on any non-empty string**, due to the `.isaplha()` typo — see the "Known bug" callout above. Intended: same asymptotic time as Linear Scan, but scans the string twice (once per `sum()`) instead of once, and `s.lower()` allocates a new lowercased string rather than lowercasing in place per character. |

## Real-World Use Case

Classifying each character of text into categories and tallying the results is a foundational step in text analysis and validation pipelines:

- **Readability and linguistic analysis tools** — vowel/consonant ratios, syllable estimation, and similar heuristics used by readability scorers and language-detection tools are built directly on top of per-character classification and counting like this.
- **Input validation for text fields** — checking that a password, username, or product code contains a required mix of letter types (or rejecting fields that are entirely non-alphabetic) reuses this same classify-then-count structure.
- **Text-based games and puzzles** — word games (Scrabble-style scoring, anagram solvers, word puzzles that count letter types) commonly need per-character classification as a building block.
- **Preprocessing for search and NLP** — tokenizers and text-cleaning pipelines often need to distinguish letters from digits/punctuation as an early filtering step before further processing, which is exactly the "is this even a letter" check this problem requires.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports exactly which method fails or errors.

| Test | Input | Expected | Result |
|---|---|---|---|
| `test_example_1` | `"hello"` | `[2, 3]` | Linear Scan ✅, Builtin ❌ (`AttributeError`) |
| `test_example_2_with_digits_and_space` | `"abc123 xy"` | `[1, 4]` | Linear Scan ✅, Builtin ❌ (`AttributeError`) |
| `test_empty_string` | `""` | `[0, 0]` | Both ✅ (the buggy generator has nothing to iterate over, so it never reaches the typo) |
| `test_mixed_case_vowels` | `"AEIOUbcd"` | `[5, 3]` | Linear Scan ✅, Builtin ❌ (`AttributeError`) |
| `test_no_vowels` | `"bcdfg"` | `[0, 5]` | Linear Scan ✅, Builtin ❌ (`AttributeError`) |
| `test_no_consonants` | `"aeiou"` | `[5, 0]` | Linear Scan ✅, Builtin ❌ (`AttributeError`) |
| `test_no_letters_at_all` | `"123 !@#"` | `[0, 0]` | Linear Scan ✅, Builtin ❌ (`AttributeError`, even though the digits/symbols aren't letters — the generator still evaluates `.isaplha()` on each one before it can fail the `and`) |
| `test_long_string_near_length_constraint` | `"bcdfg" * 2000` (10,000 chars) | `[0, 10000]` | Linear Scan ✅, Builtin ❌ (`AttributeError`) |

**8 tests, 16 sub-assertions.** `count_vowels_and_consonants_linear_scan` passes every case — no bugs found. `count_vowels_and_consonants_builtin` fails on 7 of 8 (`FAILED (errors=7)`), confirmed identically in the cloud container and re-run directly on-device as ground truth. See the "⚠️ Known bug" callout above the Additional Solution code block for the root cause and traced behavior — this was reported, not silently patched, and the tests above use the mathematically correct expected values throughout rather than being adjusted to match the buggy output.

Run with:
```bash
cd Strings/count_vowels_and_consonants
python3 -m unittest -v
```
