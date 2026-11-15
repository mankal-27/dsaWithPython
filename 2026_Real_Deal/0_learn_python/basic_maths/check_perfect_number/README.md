# Check Perfect Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `perfect_brute_force` and `perfect_optimized` with tests |

## 1. Problem Statement

A positive integer is a perfect number if it equals the sum of its proper divisors (all divisors except itself). Return `True`/`False`.

| Input | Output | Why |
|---|---|---|
| `6` | `True` | 1 + 2 + 3 = 6 |
| `28` | `True` | 1 + 2 + 4 + 7 + 14 = 28 |
| `12` | `False` | 1 + 2 + 3 + 4 + 6 = 16 |
| `1` | `False` | no proper divisors, sum is 0 |
| `0` | `False` | not positive |
| `-6` | `False` | negatives are not perfect |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `perfect_brute_force` | `perfect_optimized` |
| Idea | Test every `i` from 1 to `n-1`, add the divisors | Divisors pair up as `(i, n/i)`; loop `i` only to `sqrt(n)` and add both |
| Why it works | Directly applies the definition | If `i` divides `n`, so does `n/i`; one of the pair is always ≤ sqrt(n) |
| Care needed | Guard `n <= 1` | Skip the partner when `i == n/i` (perfect squares); start sum at 1 |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `sum = 0` | Shadows the built-in `sum()` | Rename to `divisor_sum` |
| 2 | `range(1, num)` | O(n) is slow for large `n` | Loop to `sqrt(n)` with divisor pairs |
| 3 | `return sum == num` | `num = 0` gives an empty loop, sum 0, so `0 == 0` returns `True` (0 is not perfect) | Return `False` when `num <= 1` |
| 4 | Style | `if(...)` parentheses, no trailing newline | Clean formatting |

Negatives and `1` return `False` by accident (sum is 0), which is correct but should be explicit.

## 4. Dry Run

**Optimized on `28`:** start `divisor_sum = 1`

| `divisor` | `divisor²` ≤ 28? | divides 28? | partner | `divisor_sum` |
|---|---|---|---|---|
| 2 | 4 yes | yes | 14 | 1 + 2 + 14 = 17 |
| 3 | 9 yes | no | - | 17 |
| 4 | 16 yes | yes | 7 | 17 + 4 + 7 = 28 |
| 5 | 25 yes | no | - | 28 |
| 6 | 36 no, stop | - | - | 28 == 28 -> **True** |

**Brute force on `12`:** 1 + 2 + 3 + 4 + 6 = 16 ≠ 12 -> **False**.

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(1) | One modulo check per `i` below `n` |
| Optimized | O(√n) | O(1) | Each divisor found also yields its partner |
