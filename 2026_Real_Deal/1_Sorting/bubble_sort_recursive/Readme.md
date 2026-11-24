# Bubble Sort (Recursive)

## Problem
Sort an array `nums` in ascending order using **bubble sort**, implemented **recursively** (each call does one pass, then recurses on a smaller range).

| Input | Output |
|---|---|
| `[13, 46, 24, 52, 20, 9]` | `[9, 13, 20, 24, 46, 52]` |

## Approaches

| | Brute force | Optimized (early exit) |
|---|---|---|
| Idea | One pass over `size` items, then recurse with `size-1`, until `size <= 1` | Same, but if a pass makes no swap the array is sorted, so stop recursing |
| Time | O(n²) always | O(n²) worst/avg, **O(n)** best (sorted) |
| Space | O(n) recursion stack | O(n) worst, O(1) extra best |
| Code | `bubbleSortBruteForce` | `bubbleSortOptimized` |

## Dry run (`[13, 46, 24, 52, 20, 9]`)

| Call (size) | Pass compares | Array after pass | Swapped? |
|---|---|---|---|
| 6 | idx 0..5 | 13 24 46 20 9 **52** | yes |
| 5 | idx 0..4 | 13 24 20 9 **46** 52 | yes |
| 4 | idx 0..3 | 13 20 9 **24** 46 52 | yes |
| 3 | idx 0..2 | 13 9 **20** 24 46 52 | yes |
| 2 | idx 0..1 | 9 **13** 20 24 46 52 | yes |
| 1 | base case | unchanged | stop |

Result: `[9, 13, 20, 24, 46, 52]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best (sorted, optimized) | O(n) | O(1) | one pass, no swap, return |
| Average / Worst | O(n²) | O(n) | ~n(n-1)/2 comparisons, n stack frames |

Stable (swaps only on `>`).

## Bug review of `my_sol.py`

| Line | Bug | Fix |
|---|---|---|
| swap line | RHS uses `nums[1]` instead of `nums[i]`, so the swap copies the wrong element and corrupts the array | `nums[i], nums[i+1] = nums[i+1], nums[i]` |
| base case | `if n == 1` misses `n == 0`; empty list recurses with n = -1, -2, ... forever (RecursionError) | `if n <= 1` |

Missing (not a bug): no early exit, so best case is O(n²); see the optimized version.
