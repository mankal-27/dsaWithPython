# Count Odd Digits

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged) |
| `bug_free_solution.py` | Restructured `count_odd_digits_brute_force` and `count_odd_digits_optimized` with tests |

## 1. Problem Statement

Given an integer `number`, return how many of its digits are odd. The sign is not a digit.

| Input | Output | Why |
|---|---|---|
| `12345` | `3` | 1, 3, 5 are odd |
| `2468` | `0` | all even |
| `0` | `0` | 0 is even |
| `-135` | `3` | ignore the minus sign |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `count_odd_digits_brute_force` | `count_odd_digits_optimized` |
| Idea | Convert to a string, check each character against `1 3 5 7 9` | Take `number % 10`, test the bit `& 1`, drop it with `// 10` |
| Why it works | Each character is one digit | `% 10` isolates the last digit, `// 10` removes it |
| Edge handling | `abs()` before `str()` | `abs()`; `0` skips the loop and returns 0 |

There is no sub-linear method: every digit must be inspected. "Optimized" here means O(1) extra space instead of building a string.

## 3. Bugs Found in the Original Solution

No correctness bugs. I checked `12345`, `0`, `-135`, `2468`, `9` and `10**20 + 1`, and all give the right answers. Style notes only:

| # | Line | Note | Fix |
|---|---|---|---|
| 1 | `if num == 0: return 0` | Redundant; the loop already returns 0 | Remove |
| 2 | `lastDigit`, `while(...)`, `if(...)` | camelCase and parentheses are not PEP 8 | `last_digit`, no parentheses |
| 3 | `count = count + 1` | Verbose | `odd_count += 1` |
| 4 | method name | Only one approach, no brute-force version | Added both variants |

## 4. Dry Run

**Optimized on `12345`:**

| Step | `number` | `last_digit` | Odd? | `odd_count` | `number` after `// 10` |
|---|---|---|---|---|---|
| 1 | 12345 | 5 | yes | 1 | 1234 |
| 2 | 1234 | 4 | no | 1 | 123 |
| 3 | 123 | 3 | yes | 2 | 12 |
| 4 | 12 | 2 | no | 2 | 1 |
| 5 | 1 | 1 | yes | 3 | 0 |

Loop stops at `number == 0`. Result: **3**.

**Brute force on `-135`:** `abs` gives `135`, `str` gives `"135"`, all three characters are in `13579`. Result: **3**.

## 5. Complexity

Let `d` be the number of digits, so `d ≈ log10(n)`.

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d) | O(d) | `str()` builds a d-character string, then one pass |
| Optimized | O(d) | O(1) | One loop pass per digit, two integer variables |

## 6. Real-World Use Case

Digit-parity checks appear in checksum schemes (Luhn and ISBN weigh digits by position or parity), in validating IDs, and as a building block for digit problems such as digit sums and Armstrong numbers.
