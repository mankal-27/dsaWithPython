# Reverse an Array

## Problem Statement
Given an array `nums`, return it reversed. Practice it with recursion (swap the two ends, then recurse inward).

| Input | Output | Explanation |
|-------|--------|-------------|
| [1,2,3,4,5] | [5,4,3,2,1] | opposite order |
| [1,2] | [2,1] | one swap |
| [7] | [7] | single element |
| [] | [] | empty array |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force | Read `nums` from last index to 0 into a new list | O(n) | O(n) |
| Recursive (your solution) | Swap `left`/`right`, recurse with `left+1, right-1`, stop when `left >= right` | O(n) | O(n/2) call stack (in place) |
| Optimized (two-pointer loop) | Same swaps in a `while left < right` loop | O(n) | O(1) |

## Dry Run (nums = [1,2,3,4], recursive)

| Call | left | right | Action | Array |
|------|------|-------|--------|-------|
| helper(0, 3) | 0 | 3 | swap 1<->4 | 4 2 3 1 |
| helper(1, 2) | 1 | 2 | swap 2<->3 | 4 3 2 1 |
| helper(2, 1) | 2 | 1 | left >= right, return | 4 3 2 1 |

Result: `[4,3,2,1]`.

## Complexity Notes

| Metric | Value | Why |
|--------|-------|-----|
| Time | O(n) | n/2 swaps |
| Space (loop) | O(1) | swaps happen in place |
| Stack (recursive) | O(n/2) | one frame per swap |

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Recursion depth = n/2 | len > ~2000 → `RecursionError` | Use the two-pointer loop (`reverse_optimized`) |
| Mutates input in place | Caller's list changes (fine only if intended) | Copy first (`list(nums)`) when the original must be kept |

Logic is otherwise correct (empty, one element, odd and even lengths all work). Fixed version: [solution.py](solution.py).
