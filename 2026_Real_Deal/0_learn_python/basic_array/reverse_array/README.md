# Reverse Array

**Topic:** Basic Array · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (bugs marked in comments) |
| `bug_free_solution.py` | `reverse_brute_force` and `reverse_optimized` with tests |

## 1. Problem Statement

Given an array of integers, return it with the elements in reverse order.

| Input | Output | Why |
|---|---|---|
| `[1, 2, 3]` | `[3, 2, 1]` | first becomes last |
| `[1, 2, 3, 4]` | `[4, 3, 2, 1]` | even length, no middle element |
| `[5]` | `[5]` | single element |
| `[]` | `[]` | nothing to reverse |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `reverse_brute_force` | `reverse_optimized` |
| Idea | Build a new array, reading the old one from the back | Two pointers swap mirrored elements in place |
| Why it works | Element at `i` belongs at `n - 1 - i` | Each swap fixes two positions at once, stop when pointers meet |
| Care needed | Index `n - i - 1` for the target | Loop while `left < right` (middle element stays) |

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | No logic bugs: `self`, `n`, and the mirrored index `n - i - 1` are all correct | OK | none |
| 2 | Returns `None` (bare `return`), array is reversed in place via the copy-back loop | OK for in-place judges | Return the array too if the caller uses the result |
| 3 | Uses an O(n) temp array plus a second loop, so it is the brute force | Efficiency | Two-pointer swap gives O(1) space |
| 4 | `arr [i]` / `temp [i]` spacing and trailing spaces | Style | `temp[i]` |

The idea (fill a new array from the back, copy it back) is correct: it is the brute force approach.

## 4. Dry Run

**Optimized, `[1, 2, 3, 4]`:**

| Step | `left` | `right` | Array after swap |
|---|---|---|---|
| start | 0 | 3 | `[1, 2, 3, 4]` |
| 1 | 0 | 3 | `[4, 2, 3, 1]` |
| 2 | 1 | 2 | `[4, 3, 2, 1]` |
| stop | 2 | 1 | `left >= right` |

Result: `[4, 3, 2, 1]`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(n) | One copy per element, plus a new array |
| Optimized | O(n/2) = O(n) | O(1) | n/2 swaps, no extra array |
