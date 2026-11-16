# All Divisors of a Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (bugs marked in comments) |
| `bug_free_solution.py` | `divisors_brute_force` and `divisors_optimized` with tests |

## 1. Problem Statement

Given a positive integer `n`, return all its positive divisors in ascending order.

| Input | Output | Why |
|---|---|---|
| `12` | `[1, 2, 3, 4, 6, 12]` | each divides 12 exactly |
| `36` | `[1, 2, 3, 4, 6, 9, 12, 18, 36]` | 6 is a square root, listed once |
| `13` | `[1, 13]` | prime |
| `1` | `[1]` | only itself |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `divisors_brute_force` | `divisors_optimized` |
| Idea | Test every `i` from 1 to `n` | Loop `i` to `sqrt(n)`; each hit gives the pair `i` and `n // i` |
| Why it works | Direct definition | Divisors pair up around sqrt(n) |
| Care needed | Start at 1, include `n` | Don't add the root twice for perfect squares; use `//`; sort at the end |

## 3. Bugs in `my_sol.py`

| # | Bug | Fix |
|---|---|---|
| 1 | `range(number)` starts at 0, so `number % 0` raises `ZeroDivisionError` | `range(1, number + 1)` |
| 2 | Same range stops at `number - 1`, so `number` is missing | Include `number + 1` as the end |
| 3 | `number / i` is float division, giving `12.0` not `12` | `number // i` |
| 4 | Method name typo `divsorOfNumBruteForce` | Rename |

## 4. Dry Run

**Optimized, `n = 12`:** `isqrt(12) = 3`

| `i` | 12 % i | Added | List so far |
|---|---|---|---|
| 1 | 0 | 1, 12 | [1, 12] |
| 2 | 0 | 2, 6 | [1, 12, 2, 6] |
| 3 | 0 | 3, 4 | [1, 12, 2, 6, 3, 4] |

Sorted: `[1, 2, 3, 4, 6, 12]`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(1) extra (output aside) | One modulo per number up to `n` |
| Optimized | O(sqrt n + d log d) | O(d) | sqrt(n) loop, then sort `d` divisors (d is small) |
