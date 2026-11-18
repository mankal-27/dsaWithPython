# Largest Odd Number in String

**Topic:** Basic String · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (review notes in comments) |
| `bug_free_solution.py` | `largest_odd_number_brute_force` and `largest_odd_number_optimized` with tests |

## 1. Problem Statement

Given a string `num` representing a large integer, return the largest-valued odd integer (as a string) that is a **substring** of `num`, or `""` if none exists. The result must not have leading zeros, but the input may.

| Input | Output | Why |
|---|---|---|
| `"52"` | `"5"` | `"5"` is the only odd substring that ends in an odd digit; `"52"` is even |
| `"4206"` | `""` | no odd digit |
| `"35427"` | `"35427"` | whole string ends in 7 |
| `"1230"` | `"123"` | trailing `0` is dropped |
| `"0035"` | `"35"` | leading zeros stripped |

Key fact: a number is odd iff its last digit is odd. The longest prefix ending at an odd digit is the largest, once its leading zeros are removed.

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `largest_odd_number_brute_force` | `largest_odd_number_optimized` |
| Idea | Try prefixes from longest to shortest, return the first whose last digit is odd, with leading zeros stripped | Walk from the right to the last odd digit, skip leading zeros, return that slice |
| Why it works | Longest odd prefix is the largest odd substring | Same, but without building every prefix |
| Care needed | `range(len, 0, -1)`; return `""` at the end | Slice end is `last_odd + 1`; `lstrip("0")` / skip loop for leading zeros |

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | Leading-zero skip is correct and required (`"0035"` gives `"35"`) | None | keep it |
| 2 | Parameter named `str` shadows the built-in | Style | rename to `num` |
| 3 | `if(...)` parentheses, `int(...) % 2` per char, no trailing newline | Style | `if ...:`, `in "13579"` |

The core idea (find the last odd digit) is correct, and the no-odd case returns `""` properly.

## 4. Dry Run

**Optimized, `"35427"`:** index 4 holds `7`, odd, return `num[:5]` = `"35427"`.

**Optimized, `"1230"`:**

| Step | `index` | Digit | Odd? | Result |
|---|---|---|---|---|
| 1 | 3 | 0 | no | continue |
| 2 | 2 | 3 | yes | return `num[:3]` = `"123"` |

**Optimized, `"0035"`:** last odd digit is `5` at index 3; skip `0`s at indexes 0 and 1, return `num[2:4]` = `"35"`.

**Optimized, `"4206"`:** no digit is odd, loop ends, return `""`.

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n^2) | O(n) | up to n prefixes, each slice copies up to n chars |
| Optimized | O(n) | O(1) | one right-to-left scan, one final slice for the result |
