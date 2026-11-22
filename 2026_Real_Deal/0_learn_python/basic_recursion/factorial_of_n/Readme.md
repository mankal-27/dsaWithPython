# Factorial of N

## Problem Statement
Given an integer `n`, return `n!` = n × (n-1) × ... × 1 using recursion. By definition `0! = 1`.

| Input | Output | Explanation |
|-------|--------|-------------|
| n = 5 | 120 | 5×4×3×2×1 |
| n = 1 | 1 | only 1 |
| n = 0 | 1 | empty product by definition |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (loop) | Multiply every number from 2 to n in a loop | O(n) | O(1) |
| Recursive (your solution) | `fact(n) = n * fact(n-1)`, base case `fact(0) = fact(1) = 1` | O(n) | O(n) call stack |
| Optimized (`math.factorial`) | C-implemented, no Python recursion limit | O(n) multiplications | O(1) stack |

There is no closed-form O(1) formula for exact factorials, so "optimized" here means removing the call stack (and the recursion limit).

## Dry Run (n = 4, recursive)

| Call | Returns | Computation |
|------|---------|-------------|
| fact(4) | 24 | 4 * fact(3) |
| fact(3) | 6 | 3 * fact(2) |
| fact(2) | 2 | 2 * fact(1) |
| fact(1) | 1 | base case |

Unwinding: 1 → 2 → 6 → 24.

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| No guard for negative `n` | Never reaches base case → infinite recursion → `RecursionError` | Raise `ValueError` for `n < 0` (and use `n <= 1` as base case) |
| Recursion depth = n | n > ~990 hits Python's recursion limit | Use loop or `math.factorial` |

Logic is otherwise correct. Fixed version with brute force + optimized: [solution.py](solution.py).
