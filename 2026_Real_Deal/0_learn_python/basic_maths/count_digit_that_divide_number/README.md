# Count the Digits That Divide a Number

**Topic:** Basic Maths · **Difficulty:** Easy · **LeetCode:** 2520

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (only a bug comment added) |
| `bug_free_solution.py` | `count_digits_brute_force` and `count_digits_optimized` with tests |

## 1. Problem Statement

Given an integer `num`, return the number of digits in `num` that divide `num`. A digit `val` divides `num` if `num % val == 0`. Constraints: `1 <= num <= 10^9`, and `num` has no `0` digit. A digit that repeats is counted each time.

| Input | Output | Why |
|---|---|---|
| `7` | `1` | 7 divides 7 |
| `121` | `2` | 1 divides 121 (twice), 2 does not |
| `1248` | `4` | 1, 2, 4, 8 all divide 1248 |
| `15` | `2` | 1 and 5 both divide 15 |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `count_digits_brute_force` | `count_digits_optimized` |
| Idea | Convert to a string, test `num % int(char)` for each character | Peel digits with `% 10` and `// 10`, test against a saved copy of the original |
| Why it works | Each character is one digit | `% 10` isolates the last digit, `// 10` removes it |
| Key detail | Nothing to preserve, `num` never changes | Must keep `original`, because `num` shrinks |

There is no sub-linear method, since every digit must be inspected. "Optimized" means O(1) extra space instead of building a string.

## 3. Bugs Found in the Original Solution

| # | Line | Bug | Fix |
|---|---|---|---|
| 1 | `if(num % lastDigit == 0)` | `num` is shrinking (`num //= 10`), so each digit is tested against the leftover prefix, not the original number. `121` gives `3` (checks `121%1`, `12%2`, `1%1`) but the answer is `2`. It passes some inputs by luck | Save `original = num` first and test `original % last_digit` |
| 2 | `lastDigit` as both digit variable and instance name | The instance at the bottom is also named `lastDigit`, which is confusing | Name it `solution` |
| 3 | camelCase, `while(...)`, `if(...)` | Not PEP 8 | `last_digit`, no parentheses |

A `0` digit would cause `ZeroDivisionError`, but the constraints rule it out.

## 4. Dry Run

**Optimized on `121`** (`original = 121`):

| Step | `num` | `last_digit` | `original % last_digit` | Divides? | `divisor_count` | `num` after `// 10` |
|---|---|---|---|---|---|---|
| 1 | 121 | 1 | 0 | yes | 1 | 12 |
| 2 | 12 | 2 | 1 | no | 1 | 1 |
| 3 | 1 | 1 | 0 | yes | 2 | 0 |

Loop stops at `num == 0`. Result: **2**.

**Original buggy code on `121`:** step 2 computes `12 % 2 == 0` (should be `121 % 2 == 1`), so it counts 3.

**Brute force on `1248`:** characters `1, 2, 4, 8`; `1248` is divisible by each, so the result is **4**.

## 5. Complexity

Let `d` be the number of digits, so `d ≈ log10(num)` (at most 10 here).

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d) | O(d) | `str()` builds a d-character string, then one pass |
| Optimized | O(d) | O(1) | One loop pass per digit, three integer variables |

## 6. Real-World Use Case

Digit-by-digit divisibility tests are the basis of "self-dividing number" checks and show up in checksum and number-property validation, where you need the original value to stay fixed while you consume its digits.
