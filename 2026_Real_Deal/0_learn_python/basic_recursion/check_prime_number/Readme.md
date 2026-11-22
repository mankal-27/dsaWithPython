# Check Prime Number

## Problem Statement
Given an integer `num`, return `True` if it is prime, else `False`. (Recursion practice.)

| Input | Output | Explanation |
|-------|--------|-------------|
| 7 | True | only divisors 1 and 7 |
| 12 | False | divisible by 2 |
| 1 | False | 1 is not prime |
| 2 | True | smallest prime |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force | Test every divisor 2..n-1 | O(n) | O(1) |
| Recursive (your solution) | `helper(i)`: stop True if `i*i > n`, False if `n % i == 0`, else `helper(i+1)` | O(√n) | O(√n) call stack |
| Optimized | Iterative, skip even numbers, test odd divisors up to √n | O(√n) | O(1) |

Why √n: if `n = a*b` then one of `a, b` is ≤ √n, so checking up to √n is enough.

## Dry Run (num = 11, recursive)

| Call | i*i > 11? | 11 % i | Result |
|------|-----------|--------|--------|
| helper(2) | 4 > 11 no | 1 | helper(3) |
| helper(3) | 9 > 11 no | 2 | helper(4) |
| helper(4) | 16 > 11 yes | - | True |

Result: 11 is prime.

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Recursion depth ≈ √n | Prime n > ~1,000,000 → `RecursionError` | Iterative loop (O(1) space) |

Logic is otherwise correct (n ≤ 1 False; 2, 3 True; composites caught). Fixed version with brute force + optimized: [solution.py](solution.py).
