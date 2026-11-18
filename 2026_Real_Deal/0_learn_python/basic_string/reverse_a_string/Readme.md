# Reverse a String

**Topic:** Basic String · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (bugs marked in comments) |
| `bug_free_solution.py` | `reverse_string_brute_force` and `reverse_string_optimized` with tests |

## 1. Problem Statement

Given a string, return it reversed.

| Input | Output | Why |
|---|---|---|
| `"hello"` | `"olleh"` | characters read back to front |
| `"ab"` | `"ba"` | even length, one swap |
| `"racecar"` | `"racecar"` | palindrome is unchanged |
| `"a"` / `""` | `"a"` / `""` | nothing to swap |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `reverse_string_brute_force` | `reverse_string_optimized` |
| Idea | Walk from the last index to 0, appending each char to a new list | Convert to a list, swap the two ends and move inward |
| Why it works | Reading back to front is the reverse | Each swap puts two characters in their final positions |
| Care needed | `range(len-1, -1, -1)` | `right = len - 1`; loop while `left < right` |

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | `right = len(str)` is out of range, so `str[right]` raises `IndexError` | Bug | `right = len(str) - 1` |
| 2 | Strings are immutable: `str[left] = ...` raises `TypeError` | Bug | `chars = list(text)` then swap |
| 3 | Returns the list, not a string | Bug | `"".join(chars)` |
| 4 | Parameter named `str` shadows the built-in | Style | rename to `text` |
| 5 | `while(...)`, `left , right` spacing, camelCase name | Style | `while ...:`, `left, right`, snake_case |

## 4. Dry Run

**Optimized, `"hello"` -> `['h','e','l','l','o']`:**

| Step | `left` | `right` | Swap | `chars` |
|---|---|---|---|---|
| 1 | 0 | 4 | h <-> o | o e l l h |
| 2 | 1 | 3 | e <-> l | o l l e h |
| 3 | 2 | 2 | stop (`left < right` false) | o l l e h |

Result: `"olleh"`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(n) | one pass, new list of n chars |
| Optimized | O(n) | O(n) | n/2 swaps; the list copy is needed because strings are immutable (O(1) extra if given a mutable list) |
