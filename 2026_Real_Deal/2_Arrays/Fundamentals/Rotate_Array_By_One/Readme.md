# Rotate Array By One

## Problem Statement

| Item | Detail |
|---|---|
| Input | An array `nums` of `n` elements |
| Output | Nothing; `nums` is modified **in place** so every element moves one step left and the first element goes to the end |
| Example 1 | `[1, 2, 3, 4, 5]` → `[2, 3, 4, 5, 1]` |
| Example 2 | `[7]` → `[7]` |
| Example 3 | `[]` → `[]` |
| Constraints | Array may be empty or have a single element |

## Approaches

| | Brute Force | Optimized |
|---|---|---|
| Idea | Build a new list `nums[1:] + [nums[0]]`, then copy it back into `nums` | Save `nums[0]`, shift every element one step left, put the saved value at the end |
| Time | O(n) | O(n) |
| Space | O(n) extra list | O(1) (one temp variable) |
| Explanation | Simple, but allocates a second array of size n | Works directly on the input, only one temp value is stored |

## Dry Run (Optimized)

`nums = [1, 2, 3, 4, 5]`, `temp = 1`

| Step | i | Action | nums after step |
|---|---|---|---|
| 1 | 1 | `nums[0] = nums[1]` | `[2, 2, 3, 4, 5]` |
| 2 | 2 | `nums[1] = nums[2]` | `[2, 3, 3, 4, 5]` |
| 3 | 3 | `nums[2] = nums[3]` | `[2, 3, 4, 4, 5]` |
| 4 | 4 | `nums[3] = nums[4]` | `[2, 3, 4, 5, 5]` |
| end | | `nums[-1] = temp` | `[2, 3, 4, 5, 1]` |

## Complexity

| | Best | Average | Worst |
|---|---|---|---|
| Brute force time | O(n) | O(n) | O(n) |
| Optimized time | O(n) | O(n) | O(n) |
| Brute force space | O(n) | O(n) | O(n) |
| Optimized space | O(1) | O(1) | O(1) |

## Bug Review of `my_sol.py`

| # | Finding | Detail |
|---|---|---|
| 1 | No bugs | Logic is correct and already optimal: O(n) time, O(1) space |
| 2 | Edge cases | `[]` returns early; `[x]` is saved then rewritten to itself: both correct |
| 3 | Return value | Returns `None` (in place); fine if the judge checks `nums`, add `return nums` if it expects a result |

Restructured version with brute force + optimized: [solution.py](solution.py)
