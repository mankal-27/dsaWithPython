# Add Digits Until Single Digit

## Problem Statement
Given a non-negative integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

| Input | Output | Explanation |
|-------|--------|-------------|
| 38 | 2 | 3+8=11 → 1+1=2 |
| 0 | 0 | already single digit |
| 9875 | 2 | 9+8+7+5=29 → 2+9=11 → 1+1=2 |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (loops) | While num ≥ 10, sum digits with `%10` and `//10` | O(log n) per round | O(1) |
| Recursive (your solution) | If num < 10 return it; else recurse on digit sum | O(log n) per round | O(log n) stack |
| Optimized (digital root) | `0 if num == 0 else 1 + (num-1) % 9` (a number ≡ its digit sum mod 9) | O(1) | O(1) |

## Dry Run (num = 38, recursive)

| Call | num | Digit sum | Action |
|------|-----|-----------|--------|
| addDigits(38) | 38 | 3+8 = 11 | recurse on 11 |
| addDigits(11) | 11 | 1+1 = 2 | recurse on 2 |
| addDigits(2) | 2 | – | base case, return 2 |

Optimized: 1 + (38-1) % 9 = 1 + 37 % 9 = 1 + 1 = 2.

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| `while num > 0` for negative input | Returns 0 silently (wrong) | Use `abs(num)` or reject negatives (not required by constraints) |
| Digit sum done with loop, repeat with recursion | Not a bug, just mixed style | Make digit sum recursive too for a pure recursion exercise |

Logic is correct for `num >= 0`. Fixed version with brute force + optimized: [solution.py](solution.py).
