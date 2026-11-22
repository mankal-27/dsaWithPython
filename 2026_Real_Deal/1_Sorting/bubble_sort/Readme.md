# Bubble Sort

## Problem
Given an array `nums`, sort it in ascending order using **bubble sort**.

| Input | Output |
|---|---|
| `[13, 46, 24, 52, 20, 9]` | `[9, 13, 20, 24, 46, 52]` |

## Approaches

| | Brute force | Optimized (early exit) |
|---|---|---|
| Idea | Do n-1 full passes, swapping adjacent out-of-order pairs, no matter what | Same, but shrink each pass (last i items are already placed) and stop if a pass makes no swap |
| Time | O(n²) always | O(n²) worst/avg, **O(n)** best (already sorted) |
| Space | O(1) | O(1) |
| Code | `bubbleSortBruteForce` | `bubbleSortOptimized` |

## Dry run (`[13, 46, 24, 52, 20, 9]`)

| Pass | Compared range | Array after pass | Swapped? |
|---|---|---|---|
| 1 | indices 0..5 | 13 24 46 20 9 **52** | yes |
| 2 | indices 0..4 | 13 24 20 9 **46** 52 | yes |
| 3 | indices 0..3 | 13 20 9 **24** 46 52 | yes |
| 4 | indices 0..2 | 13 9 **20** 24 46 52 | yes |
| 5 | indices 0..1 | 9 **13** 20 24 46 52 | yes |
| 6 | indices 0..0 | no comparisons | no, stop |

Result: `[9, 13, 20, 24, 46, 52]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best (sorted) | O(n) | O(1) | one pass, no swaps, break |
| Average / Worst | O(n²) | O(1) | about n(n-1)/2 comparisons |

Stable (only swaps when `>`, never on equal).

## Bug review of `my_sol.py`

| Line | Bug | Fix |
|---|---|---|
| none | None found. Loop `range(n-1, -1, -1)` with inner `range(i)` is correct, `isSwapped` early exit is correct | n/a |

Note: the outer loop could be `range(n-1, 0, -1)` (i=0 does nothing), harmless as is.
