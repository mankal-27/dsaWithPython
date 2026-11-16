# Check Prime Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `is_prime_brute_force` and `is_prime_optimized` with tests |

## 1. Problem Statement

A prime number is an integer greater than 1 whose only divisors are 1 and itself. Return `True`/`False`.

| Input | Output | Why |
|---|---|---|
| `7` | `True` | only 1 and 7 divide it |
| `2` | `True` | smallest prime |
| `9` | `False` | 3 divides it |
| `1` | `False` | 1 is not prime |
| `0` | `False` | not greater than 1 |
| `-7` | `False` | negatives are not prime |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `is_prime_brute_force` | `is_prime_optimized` |
| Idea | Test every `i` from 2 to `n-1` | Test `i` only from 2 to `sqrt(n)` |
| Why it works | Directly applies the definition | If `n = a * b`, one of `a`, `b` is ≤ sqrt(n), so a factor must show up by then |
| Care needed | Guard `n <= 1` | Use `math.isqrt` and `+ 1` so sqrt(n) itself is tested (e.g. 25 = 5 * 5) |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `def isPrimeBrute(number)` / `isPrimeOptimized` | Missing `self`; calling on `Solution()` raises `TypeError` | Add `self` |
| 2 | `if number == 1` | `0` and negatives skip the loop and return `True` | Use `number <= 1` |
| 3 | `range(2, number)` | O(n) is slow for large `n` | That is the brute force; optimized uses sqrt |
| 4 | `range(2, math.sqrt(number))` | `math.sqrt` returns a float; `range` raises `TypeError` | `math.isqrt(number)` |
| 5 | Same line | `range` end is exclusive, so sqrt(n) is never tested: 4, 9, 25 would be called prime | `range(2, limit + 1)` |
| 6 | Style | `if(...)` parentheses, no trailing newline | Clean formatting |

## 4. Dry Run

**Optimized on `25`:** `limit = isqrt(25) = 5`

| `divisor` | `25 % divisor` | Result |
|---|---|---|
| 2 | 1 | continue |
| 3 | 1 | continue |
| 4 | 1 | continue |
| 5 | 0 | return **False** (this is the case bug 5 missed) |

**Optimized on `7`:** `limit = 2`; `7 % 2 = 1`, loop ends -> **True**.

**Brute force on `9`:** 2 -> 1, 3 -> 0 -> **False**.

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(1) | One modulo check per `i` below `n` |
| Optimized | O(√n) | O(1) | Checks only up to `isqrt(n)` |
