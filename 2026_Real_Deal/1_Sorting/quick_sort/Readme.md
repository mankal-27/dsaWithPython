# Quick Sort

## Problem
Given an array `nums`, sort it in ascending order using **quick sort** (pick a pivot, partition around it, sort each side).

| Input | Output |
|---|---|
| `[13, 46, 24, 52, 20, 9]` | `[9, 13, 20, 24, 46, 52]` |

## Approaches

| | Brute force (new lists) | Optimized (in-place partition) |
|---|---|---|
| Idea | Pick middle pivot, build `smaller` / `equal` / `larger` lists, recurse, concatenate | Random pivot, Lomuto partition on `(low, high)` of the same array, recurse on both sides |
| Time | O(n log n) avg, O(n²) worst | O(n log n) avg, O(n²) worst (very unlikely with random pivot) |
| Space | O(n) extra lists per level | O(log n) stack (recurse on smaller side, loop on larger) |
| Extra | Returns a new list; handles duplicates via `equal` | Sorts in place; not stable |
| Code | `quickSortBruteForce` | `quickSortOptimized` |

## Dry run (`[13, 46, 24, 52, 20, 9]`, pivot = last element)

| Step | Range | Pivot | Partition result | Pivot index |
|---|---|---|---|---|
| 1 | 0..5 | 9 | nothing < 9, swap pivot to front: `9 46 24 52 20 13` | 0 |
| 2 | 1..5 | 13 | nothing < 13: `9 13 24 52 20 46` | 1 |
| 3 | 2..5 | 46 | 24, 20 < 46: `9 13 24 20 46 52` | 4 |
| 4 | 2..3 | 20 | nothing < 20: `9 13 20 24 46 52` | 2 |
| 5 | 3..3, 5..5 | — | single elements, done | — |

Result: `[9, 13, 20, 24, 46, 52]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best / Average | O(n log n) | O(log n) | Pivot splits roughly evenly: log n levels, n work each |
| Worst | O(n²) | O(log n) | Pivot is always min/max (sorted input with a fixed pivot); random pivot makes this unlikely |

Not stable (swaps jump over equal elements). Not adaptive.

## Bug review of `my_sol.py`

`my_sol.py` was empty when checked, so there is nothing to review yet. Save your attempt and run `upcode` again to get a bug review.

Common quick sort bugs to check in yours:

| Bug | Effect |
|---|---|
| Forgetting to swap the pivot into its final position after the scan | Pivot ends up misplaced, wrong result |
| Recursing on `(low, pivot)` instead of `(low, pivot - 1)` | Infinite recursion |
| Using `<=` on both sides with a fixed pivot | O(n²) on many duplicates |
| Fixed first/last pivot | O(n²) on sorted input |
