# Check if Array Is Sorted

**Topic:** Basic Array · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (review in comments) |
| `bug_free_solution.py` | `is_sorted_brute_force` and `is_sorted_optimized` with tests |

## 1. Problem Statement

Given an array of integers, return `True` if it is sorted in non-decreasing (ascending) order, else `False`.

| Input | Output | Why |
|---|---|---|
| `[1, 2, 3]` | `True` | each element >= previous |
| `[1, 1, 2]` | `True` | equal neighbours are allowed |
| `[1, 3, 2, 4]` | `False` | 2 comes after 3 |
| `[5]` / `[]` | `True` | nothing can be out of order |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `is_sorted_brute_force` | `is_sorted_optimized` |
| Idea | Compare every element with every later element | Compare each element only with its previous neighbour |
| Why it works | Sorted means no pair is out of order | Order between neighbours implies order for all pairs (transitivity) |
| Care needed | Inner loop starts at `i + 1` | Loop starts at index 1; use `<` so equal values pass |

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | No logic bugs: pair check, `<` for equal values, and empty/single arrays are all correct | OK | none |
| 2 | Nested loops compare all pairs, O(n^2) | Efficiency | Adjacent-only check gives O(n) |
| 3 | `if(...)`, `i+1` spacing, camelCase method name | Style | `if ...:`, `i + 1`, `is_sorted` |

## 4. Dry Run

**Optimized, `[1, 3, 2, 4]`:**

| Step | `index` | `numbers[index-1]` | `numbers[index]` | Result |
|---|---|---|---|---|
| 1 | 1 | 1 | 3 | ok, 3 >= 1 |
| 2 | 2 | 3 | 2 | 2 < 3, return `False` |

Result: `False`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n^2) | O(1) | n(n-1)/2 pair comparisons |
| Optimized | O(n) | O(1) | n-1 adjacent comparisons, early exit |
