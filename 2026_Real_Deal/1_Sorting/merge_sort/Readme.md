# Merge Sort

## Problem
Given an array `nums`, sort it in ascending order using **merge sort** (divide in halves, sort each, merge).

| Input | Output |
|---|---|
| `[13, 46, 24, 52, 20, 9]` | `[9, 13, 20, 24, 46, 52]` |

## Approaches

| | Brute force (slicing) | Optimized (index ranges) |
|---|---|---|
| Idea | Split with `nums[:mid]` / `nums[mid:]`, sort each copy, merge into a new list | Recurse on `(low, high)` of the same array, merge range, copy back |
| Time | O(n log n) | O(n log n) |
| Space | O(n log n) total copies made, O(n) alive at once plus stack | O(n) temp per merge + O(log n) stack |
| Extra | Returns a new list | Sorts in place |
| Code | `mergeSortBruteForce` | `mergeSortOptimized` |

## Dry run (`[13, 46, 24, 52, 20, 9]`)

| Step | Range (low..high) | Action | Result |
|---|---|---|---|
| 1 | 0..2 → 0..1 → 0..0, 1..1 | merge 13, 46 | 13 46 |
| 2 | 0..2 | merge [13 46] + [24] | 13 24 46 |
| 3 | 3..5 → 3..4 → 3..3, 4..4 | merge 52, 20 | 20 52 |
| 4 | 3..5 | merge [20 52] + [9] | 9 20 52 |
| 5 | 0..5 | merge [13 24 46] + [9 20 52] | 9 13 20 24 46 52 |

Result: `[9, 13, 20, 24, 46, 52]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best / Average / Worst | O(n log n) | O(n) | log n levels, each merges n items total |

Stable (`<=` takes left on ties). Not adaptive: always n log n.

## Bug review of `my_sol.py`

The `merge` step is correct (copy-back included, `<=` keeps it stable). The only bug is indentation:

| Line | Bug | Fix |
|---|---|---|
| `def mergeSortHelper` | Indented inside `merge`, so it is a nested function that is defined and never called; `self.mergeSortHelper` doesn't exist | Dedent to class level (same level as `merge`) |
| `def mergeSort` | Also nested inside `merge`, so `Solution().mergeSort(nums)` raises `AttributeError` | Dedent to class level |
| `self.mergeSortHelper(nums, 0 , n - 1)` | Fine once dedented; just spacing (`0 ,`) | Style only |
