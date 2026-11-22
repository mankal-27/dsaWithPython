# Selection Sort

## Problem
Given an array `nums`, sort it in ascending order using **selection sort**.

| Input | Output |
|---|---|
| `[64, 25, 12, 22, 11]` | `[11, 12, 22, 25, 64]` |

## Approaches

| | Brute force | Optimized (in-place) |
|---|---|---|
| Idea | Repeatedly find the min of what's left, remove it, append to a new list | Find the min of the unsorted suffix and swap it into index `i` |
| Time | O(n²) | O(n²) (best case too; no early exit) |
| Space | O(n) extra | O(1) |
| Swaps | n pops (each O(n)) | at most n-1 |
| Code | `selectionSortBruteForce` | `selectionSortOptimized` |

## Dry run (`[64, 25, 12, 22, 11]`)

| i | Unsorted part scanned | min_index (value) | After swap |
|---|---|---|---|
| 0 | 64 25 12 22 11 | 4 (11) | 11 25 12 22 64 |
| 1 | 25 12 22 64 | 2 (12) | 11 12 25 22 64 |
| 2 | 25 22 64 | 3 (22) | 11 12 22 25 64 |
| 3 | 25 64 | 3 (25) | no swap |

Result: `[11, 12, 22, 25, 64]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best / Avg / Worst | O(n²) | O(1) | always n(n-1)/2 comparisons |

Not stable (swap can jump an element over an equal one).

## Bug review of `my_sol.py`

| Line | Bug | Fix |
|---|---|---|
| `nums(min_index)` | Calls the list like a function → `TypeError: 'list' object is not callable` | Use `nums[min_index]` |

Everything else (loop bounds, swap guard, return) is correct.
