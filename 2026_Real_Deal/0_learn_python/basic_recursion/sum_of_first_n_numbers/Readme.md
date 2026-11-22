# Sum of First N Numbers

## Problem Statement
Given an integer `N`, return the sum of the first `N` natural numbers (1 + 2 + ... + N) using recursion.

| Input | Output | Explanation |
|-------|--------|-------------|
| N = 4 | 10 | 1+2+3+4 |
| N = 1 | 1 | only 1 |
| N = 0 | 0 | empty sum |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (loop) | Add every number from 1 to N in a loop | O(N) | O(1) |
| Recursive (your solution) | `sum(N) = N + sum(N-1)`, base case `sum(0) = 0` | O(N) | O(N) call stack |
| Optimized (Gauss formula) | `N * (N + 1) / 2` | O(1) | O(1) |

## Dry Run (N = 4, recursive)

| Call | Returns | Computation |
|------|---------|-------------|
| sum(4) | 10 | 4 + sum(3) |
| sum(3) | 6 | 3 + sum(2) |
| sum(2) | 3 | 2 + sum(1) |
| sum(1) | 1 | 1 + sum(0) |
| sum(0) | 0 | base case |

Unwinding: 0 → 1 → 3 → 6 → 10.

Formula check: 4 * 5 / 2 = 10.

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Base case is `N == 0` only | Negative N recurses forever → `RecursionError` | Use `N <= 0` |
| Recursion depth = N | N > ~990 hits Python's recursion limit | Use loop or formula |

Logic is otherwise correct. Fixed version with brute force + optimized: [solution.py](solution.py).
