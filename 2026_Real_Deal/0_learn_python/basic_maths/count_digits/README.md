# Count Digits

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `cnt.py` | Your original solution, line-by-line comments, bugs marked |
| `bug_free_solution.py` | Restructured, bug-free `count_digits_brute_force` and `count_digits_optimized` |
| `updt.py` | Earlier fixes plus an extra string-based approach |

## 1. Problem Statement

Given an integer `number`, return how many digits it has. The sign is not a digit.

| Input | Output | Why |
|---|---|---|
| `12345` | `5` | five digits |
| `7` | `1` | single digit |
| `0` | `1` | zero is written with one digit |
| `-123` | `3` | ignore the minus sign |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `count_digits_brute_force` | `count_digits_optimized` |
| Idea | Drop the last digit with `// 10` until the number is 0, counting each drop | `digits = floor(log10(n)) + 1`, then verify with an exact integer check |
| Why it works | Each `// 10` removes exactly one digit | Any n in `[10^(k-1), 10^k)` has k digits, and `log10(n)` lies in `[k-1, k)` |
| Edge handling | `abs()` for negatives; `0` returns 1 | Same, plus the integer check, because `log10` is a float and can round up |

```python
# Brute force
number = abs(number)
if number == 0: return 1
digit_count = 0
while number > 0:
    number //= 10
    digit_count += 1
return digit_count

# Optimized
number = abs(number)
if number == 0: return 1
digit_count = int(math.log10(number)) + 1
if 10 ** (digit_count - 1) > number:   # float rounded up -> correct it
    digit_count -= 1
return digit_count
```

## 3. Bugs Found in the Original Solution

| # | Method | Input | Got | Expected | Cause | Fix |
|---|---|---|---|---|---|---|
| 1 | `count` | `-123` | `0` | `3` | `while num > 0` is false for negatives, so the loop never runs | `abs(number)` first |
| 2 | `countOptimized` | `999999999999999` | `16` | `15` | `log10` returns 14.999... as a float that rounds up to 15.0, so `+1` gives 16 | Check `10 ** (digit_count - 1) > number` and subtract 1 |
| 3 | `countOptimized` | `10**30 - 1` | `31` | `30` | Same float rounding, worse for large values | Same fix as #2 |

## 4. Dry Run

**Brute force on `12345`:**

| Step | `number` before | `number` after `// 10` | `digit_count` |
|---|---|---|---|
| 1 | 12345 | 1234 | 1 |
| 2 | 1234 | 123 | 2 |
| 3 | 123 | 12 | 3 |
| 4 | 12 | 1 | 4 |
| 5 | 1 | 0 | 5 |

The loop stops because `number == 0`. Result: **5**.

**Optimized on `12345`:**

| Step | Expression | Value |
|---|---|---|
| 1 | `log10(12345)` | ≈ 4.09 |
| 2 | `int(...) + 1` | 5 |
| 3 | check `10**4 > 12345`? | False, so keep 5 |

Result: **5**.

**Optimized on `999999999999999` (the bug case):**

| Step | Expression | Value |
|---|---|---|
| 1 | `log10(999999999999999)` | 15.0 (float rounded up from 14.999...) |
| 2 | `int(...) + 1` | 16 |
| 3 | check `10**15 > 999999999999999`? | True, so subtract 1 |

Result: **15**. The original code returned 16.

## 5. Complexity

Let `d` be the number of digits, so `d ≈ log10(n)`.

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d), i.e. O(log n) | O(1) | One loop pass per digit, using only two integer variables |
| Optimized | O(1) | O(1) | One `log10`, one power and one comparison, whatever the size of n. For huge Python ints the arithmetic itself grows with d |
| String (`updt.py`) | O(d) | O(d) | `str()` builds a d-character string |

## 6. Real-World Use Case

Digit counting is used to pad IDs to a fixed width (invoice and order numbers), to validate lengths (phone and card numbers, OTPs), and to size columns in reports and terminal output. It is also a building block for digit problems such as palindrome numbers, Armstrong numbers and digit sums. Number-to-string code uses the same idea to decide how big a buffer it needs.
