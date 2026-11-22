# Reverse a String

## Problem Statement
Given a string `s`, return it reversed. Practice it with recursion (swap the two ends, then recurse inward).

| Input | Output | Explanation |
|-------|--------|-------------|
| "hello" | "olleh" | characters in opposite order |
| "ab" | "ba" | one swap |
| "a" | "a" | single char |
| "" | "" | empty string |

## Approaches

| Approach | Idea | Time | Space |
|----------|------|------|-------|
| Brute force (loop build) | Walk `s` from the last index to 0, append each char to a list, join | O(n) | O(n) |
| Recursive (your solution) | Copy to list, swap `left`/`right`, recurse with `left+1, right-1`, stop when `left >= right` | O(n) | O(n) list + O(n/2) call stack |
| Optimized (two-pointer loop) | Same swap idea in a `while left < right` loop, no recursion | O(n) | O(n) list (strings are immutable), O(1) stack |

## Dry Run (s = "abcd", recursive)

| Call | left | right | Action | List state |
|------|------|-------|--------|------------|
| helper(0, 3) | 0 | 3 | swap a<->d | d b c a |
| helper(1, 2) | 1 | 2 | swap b<->c | d c b a |
| helper(2, 1) | 2 | 1 | left >= right, return | d c b a |

Result: `"dcba"`.

## Complexity Notes

| Metric | Value | Why |
|--------|-------|-----|
| Time | O(n) | n/2 swaps + one join |
| Space | O(n) | Python strings are immutable, so a list copy is required |
| Stack (recursive) | O(n/2) | one frame per swap |

## Bug Review of `my_sol.py`

| Issue | Impact | Fix |
|-------|--------|-----|
| Recursion depth = n/2 | len(s) > ~2000 → `RecursionError` | Use the two-pointer loop (`reverse_optimized`) |

Logic is otherwise correct (empty string, one char, odd and even lengths all work). Fixed version with brute force + optimized: [solution.py](solution.py).
