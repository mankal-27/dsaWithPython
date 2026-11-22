# Check if Array is Sorted

## Problem Statement
Given an array `nums`, return `True` if it is sorted in non-decreasing order, else `False`. Practice it with recursion (compare neighbours, recurse right).

| Input | Output | Explanation |
|-------|--------|-------------|
| [1, 2, 3, 4] | True | strictly increasing |
| [1, 2, 2, 3] | True | equal neighbours allowed |
| [1, 3, 2, 4] | False | 3 > 2 |
| [5] | True | single element |
| [] | True | empty array |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (sort + compare) | `nums == sorted(nums)` | O(n log n) | O(n) |
| Recursive (your solution) | `helper(i)`: True at last index, False if `nums[i] > nums[i+1]`, else `helper(i+1)` | O(n) | O(n) call stack |
| Optimized (loop) | One pass, return False on first descent | O(n) | O(1) |

## Dry Run (nums = [1, 3, 2, 4], recursive)

| Call | i | nums[i] vs nums[i+1] | Action |
|------|---|----------------------|--------|
| helper(0) | 0 | 1 <= 3 | recurse |
| helper(1) | 1 | 3 > 2 | return False |

Result: `False`. For `[1, 2, 3]`: helper(0), helper(1) ok, helper(2) → last index → `True`.

## Complexity Notes

| Metric | Value | Why |
|--------|-------|-----|
| Time (brute force) | O(n log n) | sorting dominates |
| Time (recursive / optimized) | O(n) | at most n-1 comparisons |
| Space (recursive) | O(n) | one frame per element |
| Space (optimized) | O(1) | only an index |

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Recursion depth = n-1 | len(nums) > ~1000 → `RecursionError` | Use the loop (`check_optimized`) |

Logic is otherwise correct (empty, single element, duplicates all work; the `len <= 1` guard is needed there so `helper(0)` isn't indexed on an empty list). Fixed version with brute force + optimized: [solution.py](solution.py).
