# Sum of Array Elements

## Problem Statement
Given an integer array `nums`, return the sum of all its elements using recursion.

| Input | Output | Explanation |
|-------|--------|-------------|
| [1, 2, 3, 4] | 10 | 1+2+3+4 |
| [5] | 5 | single element |
| [] | 0 | empty sum |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (loop) | Add each element in a loop | O(n) | O(1) |
| Recursive (your solution) | `sum(i) = nums[i] + sum(i+1)`, base case `i == len` → 0 | O(n) | O(n) call stack |
| Optimized (halving recursion) | `sum(low, high) = sum(low, mid) + sum(mid, high)` | O(n) | O(log n) call stack |

## Dry Run (nums = [1, 2, 3], recursive)

| Call | Returns | Computation |
|------|---------|-------------|
| helper(0) | 6 | 1 + helper(1) |
| helper(1) | 5 | 2 + helper(2) |
| helper(2) | 3 | 3 + helper(3) |
| helper(3) | 0 | base case (i == len) |

Unwinding: 0 → 3 → 5 → 6.

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Recursion depth = len(nums) | len > ~990 → `RecursionError` | Loop, or halving recursion (depth log n) |

Logic is otherwise correct (empty list returns 0). Fixed version with brute force + optimized: [solution.py](solution.py).
