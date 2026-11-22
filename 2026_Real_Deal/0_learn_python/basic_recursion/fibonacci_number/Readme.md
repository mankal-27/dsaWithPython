# Fibonacci Number

## Problem Statement
Given an integer `n`, return the n-th Fibonacci number, where `F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`.

| Input | Output | Explanation |
|-------|--------|-------------|
| 0 | 0 | base case |
| 1 | 1 | base case |
| 5 | 5 | 0,1,1,2,3,**5** |
| 10 | 55 | 0,1,1,2,3,5,8,13,21,34,**55** |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (your solution) | `fib(n-1) + fib(n-2)`, base `n <= 1` | O(2^n) | O(n) call stack |
| Memoized recursion | Same recursion, cache results in a dict | O(n) | O(n) |
| Optimized | Iterate, keep only the last two values | O(n) | O(1) |

Why brute force is slow: the same subproblems (e.g. `fib(3)`) are recomputed many times, so the call tree doubles at each level.

## Dry Run (n = 4, recursive)

| Call | Returns | Computed from |
|------|---------|---------------|
| fib(4) | 3 | fib(3) + fib(2) |
| fib(3) | 2 | fib(2) + fib(1) |
| fib(2) | 1 | fib(1) + fib(0) |
| fib(1) | 1 | base case |
| fib(0) | 0 | base case |

`fib(2)` is computed twice here; for larger `n` the repeats explode.

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Exponential time O(2^n) | `n ≈ 40+` takes very long | Memoize or iterate |
| Negative `n` returns `n` itself (`n <= 1`) | `fib(-5)` → -5, which is not a valid Fibonacci value | Reject `n < 0` with `ValueError` |

Logic is otherwise correct for n ≥ 0. Fixed version: [solution.py](solution.py).
