# Check Palindrome in a String

## Problem Statement
Given a string `s`, return `True` if it reads the same forwards and backwards, else `False`. Practice it with recursion (compare the two ends, then recurse inward).

| Input | Output | Explanation |
|-------|--------|-------------|
| "racecar" | True | mirror image |
| "abba" | True | even length |
| "hello" | False | 'h' != 'o' |
| "a" | True | single char |
| "" | True | empty string |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (reverse + compare) | Build the reversed string, check `s == reversed` | O(n) | O(n) |
| Recursive (your solution) | `helper(left, right)`: return True if `left >= right`, False on mismatch, else recurse `left+1, right-1` | O(n) | O(n/2) call stack |
| Optimized (two-pointer loop) | Same comparisons in `while left < right`, no recursion | O(n) | O(1) |

## Dry Run (s = "abca", recursive)

| Call | left | right | s[left] vs s[right] | Action |
|------|------|-------|---------------------|--------|
| helper(0, 3) | 0 | 3 | a == a | recurse |
| helper(1, 2) | 1 | 2 | b != c | return False |

Result: `False`. For `"abba"`: helper(0,3) ok, helper(1,2) ok, helper(2,1) → `left >= right` → `True`.

## Complexity Notes

| Metric | Value | Why |
|--------|-------|-----|
| Time | O(n) | at most n/2 comparisons |
| Space (brute force) | O(n) | reversed copy |
| Space (recursive) | O(n/2) | one frame per comparison |
| Space (optimized) | O(1) | two indices only |

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Recursion depth = n/2 | len(s) > ~2000 → `RecursionError` | Use the two-pointer loop (`check_optimized`) |

Logic is otherwise correct (empty string, one char, odd and even lengths all work). Case and non-alphanumeric characters are not ignored; the problem doesn't ask for that. Fixed version with brute force + optimized: [solution.py](solution.py).
