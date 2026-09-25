# Toggle Case of Every Character

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/toggle-case-of-every-character
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s, return a new string where the case of every letter is flipped. Each uppercase letter becomes lowercase, and each lowercase letter becomes uppercase. Any character that is not a letter, such as a digit or a space, stays exactly as it is.

For example, "Hello" becomes "hELLO", and "123abc" becomes "123ABC".

**Example 1**
```
Input:  s = "Hello World"
Output: "hELLO wORLD"
```

**Example 2**
```
Input:  s = "ABCabc"
Output: "abcABC"
```

**Constraints**
```
0 <= s.length <= 1000
The string may contain letters, digits, spaces, and other printable characters.
```

## How to Solve It — Thought Process

At first glance, "flip the case of a letter" sounds like it might need a lookup table — a rule pairing `A` with `a`, `B` with `b`, and so on through all 52 letters. Writing that out by hand would be tedious and error-prone, so it's worth asking whether there's a pattern that makes 52 individual rules unnecessary. There is: characters aren't just symbols, they're numbers under the hood (Python's `ord()` gives a character's underlying code point, and `chr()` goes the other way), and the uppercase and lowercase letters sit in two parallel, evenly-spaced ranges — uppercase `A` through `Z` in one contiguous block, lowercase `a` through `z` in another, with lowercase sitting exactly `32` codes above its uppercase counterpart at every position (`'A'` is `65`, `'a'` is `97`; `'B'` is `66`, `'b'` is `98`, and so on all the way to `'Z'`/`'z'`). Because that gap is constant across the entire alphabet, one arithmetic rule replaces all 52 individual pairings: shift an uppercase letter's code up by `32` to get its lowercase twin, and shift a lowercase letter's code down by `32` to get its uppercase twin.

That leaves two things to get right per character: first, deciding *which* direction to shift (or whether to shift at all), and second, actually doing the shift through `ord()`/`chr()` rather than trying to do arithmetic directly on a string character. The direction check itself is straightforward range membership — is this character's code within the uppercase block, within the lowercase block, or in neither? Anything outside both ranges (a digit, a space, punctuation) isn't a letter at all, so it has no case to flip and gets copied through untouched. That "leave it as is" behavior isn't a separate special case to code for — it's just the natural fallback when neither range condition is true.

Since Python strings are immutable, the result has to be built up as a new string rather than edited in place, the same consideration that came up when replacing spaces earlier in this topic: accumulate the transformed characters into a list, and join them into the final string once at the end, rather than repeatedly concatenating onto a string inside the loop.

The empty-string case resolves itself the same way it always does with a scanning approach: no characters means the loop body never runs, so the result list stays empty and joins to an empty string.

Since every character has to be inspected once to determine whether it's uppercase, lowercase, or neither, a single linear pass is already the best this problem can do — there's no way to flip case without looking at each character to classify it first.

## Brute Force Solution — ASCII Arithmetic (this is already optimal; every character must be classified and possibly shifted once, so a single linear pass can't be improved on)

```python
class Solution:
    def toggle_case_ascii_arithmetic(self, s):
        result = []
        for char in s:
            code = ord(char)
            if ord('A') <= code <= ord('Z'):
                result.append(chr(code + 32))
            elif ord('a') <= code <= ord('z'):
                result.append(chr(code - 32))
            else:
                result.append(char)
        return "".join(result)
```

## Additional Solution — Built-in `str.swapcase()`

```python
    def toggle_case_builtin_swapcase(self, s):
        return s.swapcase()
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().toggle_case_ascii_arithmetic(s)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a shorter version of the same loop:** Python's `str` type has a method, `swapcase()`, that exists specifically to do exactly what this problem asks — flip every letter's case and leave everything else alone. Unlike the ASCII Arithmetic solution, which reimplements the classification-and-shift logic explicitly with `ord()`/`chr()` range checks, `swapcase()` performs the same case-toggling internally, in CPython's C implementation, using the language's full Unicode case-folding rules rather than a hardcoded `+32`/`-32` offset (which technically only covers the ASCII letter ranges). Same O(n) time and O(n) space, but with the per-character classification and shifting happening at C speed instead of through an interpreted Python loop — the same tradeoff seen with `str.replace()`/`str.count()` in earlier problems in this repo.

### Algorithm — ASCII Arithmetic
1. Create an empty list to hold the result pieces.
2. Loop over every character in the input string.
3. If the character's code falls within the uppercase range (`'A'` to `'Z'`), append the character `32` codes higher (its lowercase twin).
4. Else if the character's code falls within the lowercase range (`'a'` to `'z'`), append the character `32` codes lower (its uppercase twin).
5. Otherwise, append the character unchanged.
6. After the loop, join the list into a single string and return it.

### Algorithm — Built-in `str.swapcase()`
1. Call `s.swapcase()`, which flips the case of every letter internally and leaves everything else unchanged.
2. Return the result directly.

## Dry Run

### ASCII Arithmetic — `s = "Hi 9!"`

| Character | `ord()` | Range | Shift | Result char | `result` after |
|---|---|---|---|---|---|
| H | 72 | Uppercase (`65`–`90`) | `+32` → `104` | h | `['h']` |
| i | 105 | Lowercase (`97`–`122`) | `-32` → `73` | I | `['h', 'I']` |
| (space) | 32 | Neither | none | (space) | `['h', 'I', ' ']` |
| 9 | 57 | Neither | none | 9 | `['h', 'I', ' ', '9']` |
| ! | 33 | Neither | none | ! | `['h', 'I', ' ', '9', '!']` |

`"".join(...)` → `"hI 9!"`. This matches the worked example on the problem's own hints page.

### ASCII Arithmetic — `s = "Hello World"`

`H`→`h`, `e`→`E`, `l`→`L`, `l`→`L`, `o`→`O` (space unchanged), `W`→`w`, `o`→`O`, `r`→`R`, `l`→`L`, `d`→`D`. Joined: `"hELLO wORLD"`. ✅ matches expected output.

### Built-in `str.swapcase()` — `s = "ABCabc"`

`"ABCabc".swapcase()` flips each of the six letters: `A`→`a`, `B`→`b`, `C`→`c`, `a`→`A`, `b`→`B`, `c`→`C`. Return `"abcABC"`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| ASCII Arithmetic | O(n) | O(n) | Single pass; each character is classified with two range checks and shifted (or copied) once, then appended to a list, joined once at the end. Already optimal — flipping case requires classifying every character. |
| Built-in `str.swapcase()` | O(n) | O(n) | Same asymptotic complexity as ASCII Arithmetic; the classification and case-flip happen in CPython's C implementation instead of an interpreted loop with manual `ord()`/`chr()` arithmetic, which is typically faster in practice for the same work. |

## Real-World Use Case

Flipping or otherwise transforming the case of text on a per-character basis is a small operation that shows up in several everyday text-processing contexts:

- **Case-insensitive comparison and normalization** — while this problem specifically flips case rather than normalizing it, the same character-by-character classification (is this letter upper, lower, or neither) is the building block behind case-insensitive search, sorting, and comparison utilities.
- **Text obfuscation and stylistic formatting** — "sPoNgEbOb case" and similar alternating-case text effects, sometimes used in casual text styling or as a simple obfuscation technique, are a direct, repeated application of a per-character case toggle.
- **Data validation and format checking** — verifying that an identifier or code follows a specific case convention (checking which characters are upper/lower, or converting between conventions like camelCase and snake_case) relies on the same per-character classification this problem exercises.
- **Legacy encoding and protocol handling** — some older text protocols and encodings that predate Unicode rely on exactly this kind of fixed-offset ASCII arithmetic (the same `+32`/`-32` relationship between upper and lowercase letters) for case manipulation, which is why understanding the underlying ASCII structure — not just calling a built-in — is a useful skill on its own.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"Hello World"` | `"hELLO wORLD"` |
| `test_example_2` | `"ABCabc"` | `"abcABC"` |
| `test_empty_string` | `""` | `""` |
| `test_no_letters` | `"123 !@#"` | `"123 !@#"` |
| `test_all_uppercase` | `"ABCDE"` | `"abcde"` |
| `test_all_lowercase` | `"abcde"` | `"ABCDE"` |
| `test_mixed_letters_digits_punctuation` | `"Hi 9!"` | `"hI 9!"` |
| `test_long_string_near_length_constraint` | `"a"*500 + "B"*500` (1,000 characters) | `"A"*500 + "b"*500` |

All 8 tests (16 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

Run with:
```bash
cd Strings/toggle_case_of_every_character
python3 -m unittest -v
```
