# Sum of Array Elements

**Topic:** Basic Array · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (review notes in comments) |
| `bug_free_solution.py` | `sum_brute_force` and `sum_optimized` with tests |

## 1. Problem Statement

Given an array of integers, return the sum of all its elements.

| Input | Output | Why |
|---|---|---|
| `[1, 2, 3]` | `6` | 1 + 2 + 3 |
| `[-1, -2, 3]` | `0` | negatives are added too |
| `[5]` | `5` | single element |
| `[]` | `0` | nothing to add |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `sum_brute_force` | `sum_optimized` |
| Idea | Loop over the array, keep a running `total` | Call built-in `sum()` |
| Why it works | Every element is visited once and added | Same single pass, but implemented in C |
| Care needed | Start `total` at 0 (handles empty array) | None |

Both are O(n): every element must be read at least once, so no approach can beat linear time.

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | None: logic is correct for empty, negative and normal arrays | - | - |
| 2 | `range(len(arr))` with `arr[i]` is unneeded indexing | Style | `for value in arr` |
| 3 | Test code runs at import time | Style | Wrap in `if __name__ == "__main__":` |

## 4. Dry Run

**Brute force, `[1, 2, 3]`:**

| Step | `value` | `total` after |
|---|---|---|
| start | - | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |

Result: `6`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(1) | One addition per element, one variable |
| Optimized | O(n) | O(1) | `sum()` is still one pass, only a faster constant |
