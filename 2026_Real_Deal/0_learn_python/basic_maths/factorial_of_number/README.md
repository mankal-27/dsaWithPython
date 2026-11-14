# Factorial of a Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `factorial_brute_force` and `factorial_optimized` with tests |

## 1. Problem Statement

Given a non-negative integer `number`, return `number!` (the product of all integers from 1 to `number`). `0! = 1`.

| Input | Output | Why |
|---|---|---|
| `0` | `1` | by definition |
| `1` | `1` | just 1 |
| `5` | `120` | 1·2·3·4·5 |
| `10` | `3628800` | product of 1..10 |
| `-3` | `ValueError` | undefined for negatives |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `factorial_brute_force` | `factorial_optimized` |
| Idea | Recursion: `n! = n * (n-1)!` | Loop multiplying 2..n into a running result |
| Why it works | Definition of factorial, base case `n <= 1` returns 1 | Product is accumulated once per number |
| Extra | Deep `n` risks recursion limit | No stack use; skips multiplying by 1 |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `range(num)` | Starts at `0`, so `result * 0` makes every answer `0` (`5` gives `0`, not `120`) | `range(1, num + 1)` |
| 2 | Input check | Negative numbers are not rejected | Raise `ValueError` |
| 3 | Style | `if num == 0 :` stray space, no trailing newline | Clean formatting |

The `num == 0` special case is correct.

## 4. Dry Run

**Optimized on `5`:**

| Step | `multiplier` | `result` before | `result` after |
|---|---|---|---|
| start | - | 1 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 3 | 2 | 6 |
| 3 | 4 | 6 | 24 |
| 4 | 5 | 24 | 120 |

Result **120**.

**Brute force on `3`:** `3 * f(2)` -> `3 * (2 * f(1))` -> `3 * (2 * 1)` = **6**.

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(n) | n recursive calls stacked on the call stack |
| Optimized | O(n) | O(1) | One loop, one running variable |

(Multiplications on big integers cost more than O(1) each, but the count of multiplications is n.)
