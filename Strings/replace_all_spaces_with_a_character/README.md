# Replace All Spaces with a Character

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/replace-all-spaces-with-a-character
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s and a single character ch, return a new string where every space in s is replaced by ch. Every non-space character keeps its original value and position. Only the spaces change.

If the input has no spaces, the output matches the input. If the input is empty, the output is empty too. Since each space turns into exactly one character, the length of the string never changes.

**Example 1**
```
Input:  s = "a b c", ch = '_'
Output: "a_b_c"
```

**Example 2**
```
Input:  s = "hello world", ch = '-'
Output: "hello-world"
```

**Constraints**
```
0 <= s.length <= 1000
s consists of printable ASCII characters.
ch is a single character.
```

## How to Solve It — Thought Process

The first thing worth noticing is that this problem is a one-for-one swap, not an insertion or a deletion — every space becomes exactly one `ch`, and nothing else shifts position or changes length. That immediately rules out anything more complicated than a straightforward per-character decision: look at each character in turn, and if it's a space, use `ch` instead; if it isn't, keep it exactly as it is. There's no dependency between positions — deciding what happens at index `i` never requires knowing what happened at `i - 1` or `i + 1` — so a single pass through the string, left to right, is naturally enough.

The one detail worth being deliberate about is *how* the result gets built, not what decision gets made at each character. In Python, strings are immutable — every time you do `result = result + something`, you're not appending onto the existing string, you're building a brand-new string that's a copy of the old one plus the new piece. Doing that inside a loop, once per character, would mean the *total* amount of copying work across the whole loop grows quadratically with the string's length (each step re-copies everything built so far), even though there are only `n` characters to process. The fix is to accumulate the pieces somewhere mutable — a list — and defer the actual string construction to a single `"".join(...)` call at the very end. Appending to a list is a cheap, amortized-constant-time operation per character, and building the final string once, from all the pieces at once, avoids the repeated re-copying that direct string concatenation in a loop would cause.

The empty-string and no-spaces cases don't need special handling; they fall out of the same loop naturally. An empty string means there are zero characters to iterate over, so the loop body never runs and the result list stays empty, giving back an empty string. A string with no spaces means the "is this a space" check is always false, so every character gets copied through unchanged, and the output ends up identical to the input — exactly as the problem statement describes.

Since building the output requires producing a full copy of the string (with spaces swapped out), and every character has to be looked at to decide what goes in its place, this is already as efficient as the problem allows: O(n) time to visit each character once, and O(n) space because the result is itself a new string of the same length as the input — there's no way to avoid materializing the output, since Python strings can't be modified in place.

## Brute Force Solution — Linear Scan and Build (this is already optimal; producing a transformed copy requires visiting every character once and building an output of the same length)

```python
class Solution:
    def replace_spaces_linear_scan(self, s, ch):
        result = []
        for char in s:
            if char == " ":
                result.append(ch)
            else:
                result.append(char)
        return "".join(result)
```

## Additional Solution — Built-in `str.replace()`

```python
    def replace_spaces_builtin_replace(self, s, ch):
        return s.replace(' ', ch)
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().replace_spaces_linear_scan(s, ch)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a shorter version of the same loop:** `str.replace()` performs the exact same one-for-one substitution that the hand-written loop does, scanning the string once and swapping every space for `ch`, but the scan and the buffer-building both happen inside CPython's C implementation of the `str` type rather than as a Python-level loop with list appends and a final `join()`. Same algorithmic idea, same O(n) time and O(n) space, but with the per-character work happening at C speed rather than through the Python interpreter — the same tradeoff seen with `sum()`/`len()`/`str.count()` in earlier problems in this repo.

### Algorithm — Linear Scan and Build
1. Create an empty list to hold the result pieces.
2. Loop over every character in the input string.
3. If the current character is a space, append `ch` to the list.
4. Otherwise, append the current character unchanged.
5. After the loop, join the list into a single string and return it.

### Algorithm — Built-in `str.replace()`
1. Call `s.replace(' ', ch)`, which scans the string and substitutes every space with `ch` internally.
2. Return the result directly.

## Dry Run

### Linear Scan and Build — `s = "a b c"`, `ch = '_'`

| Character | Is a space? | Appended | `result` after |
|---|---|---|---|
| a | No | a | `['a']` |
| (space) | Yes | _ | `['a', '_']` |
| b | No | b | `['a', '_', 'b']` |
| (space) | Yes | _ | `['a', '_', 'b', '_']` |
| c | No | c | `['a', '_', 'b', '_', 'c']` |

`"".join(['a', '_', 'b', '_', 'c'])` → `"a_b_c"`. Return `"a_b_c"`. ✅ matches expected output.

### Linear Scan and Build — `s = "hello world"`, `ch = '-'`

The loop copies `h`, `e`, `l`, `l`, `o` unchanged, replaces the single space with `-`, then copies `w`, `o`, `r`, `l`, `d` unchanged. `result` joins to `"hello-world"`. Return `"hello-world"`. ✅ matches expected output.

### Built-in `str.replace()` — `s = ""`, `ch = '*'`

`"".replace(' ', '*')` has no characters to scan and no spaces to replace, so it returns the empty string unchanged. Return `""`, matching the stated rule that an empty input produces an empty output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Linear Scan and Build | O(n) | O(n) | Single pass; each character is inspected once and appended to a list, then joined once at the end. Already optimal — producing a transformed copy requires visiting every character and building an output of the same length; using a list plus one `join()` avoids the quadratic cost that repeated string concatenation in a loop would cause. |
| Built-in `str.replace()` | O(n) | O(n) | Same asymptotic complexity as Linear Scan and Build; the scan-and-substitute happens in CPython's C implementation instead of an interpreted loop with list appends, which is typically faster in practice for the same work. |

## Real-World Use Case

Swapping one character for another throughout a string, position by position, is a small building block that shows up in a range of text-transformation tasks:

- **URL slug generation** — converting a title or sentence into a URL-friendly slug commonly involves replacing spaces (and other characters) with a hyphen or underscore, which is exactly this transformation.
- **CSV and delimited-format escaping** — replacing a problematic character (a space, a comma, a newline) with a safe placeholder before writing a value into a delimited file is a direct application of this same find-and-substitute pattern.
- **Whitespace normalization** — converting between whitespace conventions (spaces to tabs, spaces to a visible placeholder for debugging/logging, or collapsing varied whitespace to a single canonical character) builds on this same character-by-character substitution.
- **Templating and filename sanitization** — generating a safe filename from user input (where spaces and other characters often need to become underscores or hyphens) is another everyday instance of this same one-for-one character replacement.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"a b c"`, `'_'` | `"a_b_c"` |
| `test_example_2` | `"hello world"`, `'-'` | `"hello-world"` |
| `test_empty_string` | `""`, `'*'` | `""` |
| `test_no_spaces` | `"nospaces"`, `'_'` | `"nospaces"` |
| `test_all_spaces` | `"   "`, `'#'` | `"###"` |
| `test_multiple_consecutive_spaces` | `"a  b"`, `'_'` | `"a__b"` |
| `test_leading_space` | `" lead"`, `'_'` | `"_lead"` |
| `test_trailing_space` | `"trail "`, `'_'` | `"trail_"` |
| `test_long_string_near_length_constraint` | `"a " * 500` (1,000 characters), `'X'` | `"aX" * 500` |

All 9 tests (18 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

Run with:
```bash
cd Strings/replace_all_spaces_with_a_character
python3 -m unittest -v
```
