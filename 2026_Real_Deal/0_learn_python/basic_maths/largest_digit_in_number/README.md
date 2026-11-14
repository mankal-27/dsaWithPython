# Largest Digit in a Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `largest_digit_brute_force` and `largest_digit_optimized` with tests |

## 1. Problem Statement

Given an integer `number`, return its largest digit. Negative numbers use their absolute value.

| Input | Output | Why |
|---|---|---|
| `472` | `7` | digits 4, 7, 2 |
| `1000` | `1` | zeros never beat 1 |
| `0` | `0` | single digit |
| `99` | `9` | repeated max |
| `-472` | `7` | sign ignored |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `largest_digit_brute_force` | `largest_digit_optimized` |
| Idea | `max(str(abs(n)))` then `int` | Loop: `% 10` gets last digit, keep running max, `// 10` drops it |
| Why it works | Characters '0'-'9' compare in the same order as digits | Every digit is visited once |
| Extra | None | Early exit once the max is 9 |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `while(num > 0)` | Negative input skips the loop and returns `0` (`-472` gives `0`, not `7`) | `number = abs(number)` first |
| 2 | Style | camelCase `lastDigit`, parentheses on `while`/`if`, no trailing newline | `snake_case`, no parentheses |

The core logic is correct for `num >= 0`, including `0`.

## 4. Dry Run

**Optimized on `472`:**

| Step | `number` | `last_digit` | `largest_digit` | `number` after `// 10` |
|---|---|---|---|---|
| 1 | 472 | 2 | 2 | 47 |
| 2 | 47 | 7 | 7 | 4 |
| 3 | 4 | 4 | 7 (4 < 7) | 0 |

Loop ends, result **7**.

**Brute force on `472`:** `"472"` -> `max` is `'7'` -> `7`.

## 5. Complexity

Let `d` be the number of digits, so `d ≈ log10(n)`.

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d) | O(d) | Builds a d-character string |
| Optimized | O(d) | O(1) | One pass, two integer variables |

## 6. Real-World Use Case

Digit-level scans appear in number-base conversion (smallest base needed), checksum validation and digit-DP style problems.
