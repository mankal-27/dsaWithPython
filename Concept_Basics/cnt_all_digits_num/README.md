# Count All Digits of a Number

**Step:** Concept Basics → Basic Maths
**Difficulty:** Easy
**Link:** https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number?category=beginner-problem&subcategory=basic-maths
**Files:** `ex1.py` (solution), `test_ex1.py` (unit tests)

## Problem Statement

You are given an integer `n`. Return the number of digits in the number.

The number will have no leading zeroes, except when the number is `0` itself.

**Example 1**
```
Input:  n = 4
Output: 1
Explanation: There is only 1 digit in 4.
```

**Example 2**
```
Input:  n = 14
Output: 2
Explanation: There are 2 digits in 14.
```

**Example 3**
```
Input:  n = 234
Output: 3
```

**Constraints**
```
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
```

## Solution

```python
import math

class Solution:
    def countDigit(self, n):
        count = 0
        if n == 0:
            return 1
        while(n > 0):
            count = count + 1
            n = math.floor(n / 10)
        return count
```

**Approach:** Handle `n = 0` as a special case up front (it has 1 digit, but the loop below would never execute for it). Otherwise, repeatedly strip the last digit by dividing `n` by 10 (using `math.floor` since `/` in Python always returns a float), incrementing `count` once per strip, until `n` reaches `0`.

## Complexity

- **Time Complexity:** O(d), where `d` is the number of digits in `n`. Equivalently O(log₁₀ n), since the value of `n` shrinks by a factor of 10 each iteration — the loop runs exactly once per digit.
- **Space Complexity:** O(1) — only the `count` variable and the shrinking copy of `n` are used; no extra data structures that grow with input size.

## Dry Run

`n = 234`

| Iteration | n (start of loop) | n > 0? | count (after ++) | n = math.floor(n/10) |
|---|---|---|---|---|
| 1 | 234 | yes | 1 | 23 |
| 2 | 23 | yes | 2 | 2 |
| 3 | 2 | yes | 3 | 0 |
| 4 | 0 | no → loop exits | — | — |

Return `count = 3`. ✅ matches expected output.

**Edge case dry run — `n = 0`:** the `if n == 0: return 1` guard fires immediately, so the `while` loop (which would never run since `0 > 0` is `False`) is never reached. Returns `1` directly.

## Real-World Use Case

Counting digits is a small building block that shows up inside larger systems rather than as a standalone feature:

- **Input validation:** checking that a PIN, OTP, account number, or pincode has the expected number of digits before accepting it.
- **UI/formatting:** deciding how many placeholder boxes to render for an OTP input, or how much to pad a number with leading zeros (e.g. invoice numbers like `INV-00042`).
- **Digit DP / competitive programming:** many "digit DP" problems (count numbers with a given digit sum, count numbers without repeated digits, etc.) first need to know how many digits the number has to size the DP table.
- **Number formatting libraries:** functions that decide whether to display a number in full, abbreviate it (1.2K, 3.4M), or choose a column width in a table/report use digit count internally.

## Tests

`test_ex1.py` covers the three given examples plus edge/boundary cases:

| Test | Input | Expected |
|---|---|---|
| `test_example_1_single_digit` | 4 | 1 |
| `test_example_2_two_digits` | 14 | 2 |
| `test_example_3_three_digits` | 234 | 3 |
| `test_zero_edge_case` | 0 | 1 |
| `test_single_digit_boundary_low` | 1 | 1 |
| `test_single_digit_boundary_high` | 9 | 1 |
| `test_two_digit_boundary` | 10 | 2 |
| `test_four_digit_number` | 1000 | 4 |
| `test_max_constraint_value` | 5000 (upper bound) | 4 |
| `test_power_of_ten` | 100 | 3 |

Run with:
```bash
cd Concept_Basics/cnt_all_digits_num
python3 -m unittest -v
```

All 10 tests pass against the current `ex1.py` implementation.
