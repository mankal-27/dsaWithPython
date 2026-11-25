# Rotate Array K Left

## Problem Statement

| Item | Detail |
|---|---|
| Input | An array `nums` of `n` elements and an integer `k >= 0` |
| Output | `nums` rotated **left** by `k` positions, in place |
| Example 1 | `[1, 2, 3, 4, 5], k=2` → `[3, 4, 5, 1, 2]` |
| Example 2 | `[1, 2, 3], k=3` → `[1, 2, 3]` |
| Example 3 | `[1, 2], k=5` → `[2, 1]` (k mod n = 1) |
| Constraints | Array may be empty; `k` may exceed `n` |

## Approaches

| | Brute Force | Optimized |
|---|---|---|
| Idea | Rotate left by one, repeated `k % n` times | Save first `k` elements, shift the rest left by `k`, write saved ones at the end |
| Time | O(n * k) | O(n) |
| Space | O(1) | O(k) |
| Explanation | Simple but slow for large k | One pass to shift plus one to restore |

## Dry Run (Optimized)

`nums = [1, 2, 3, 4, 5]`, `k = 2`, `saved = [1, 2]`

| Step | Action | nums after step |
|---|---|---|
| 1 | `nums[0] = nums[2]` | `[3, 2, 3, 4, 5]` |
| 2 | `nums[1] = nums[3]` | `[3, 4, 3, 4, 5]` |
| 3 | `nums[2] = nums[4]` | `[3, 4, 5, 4, 5]` |
| 4 | `nums[3] = saved[0]` | `[3, 4, 5, 1, 5]` |
| 5 | `nums[4] = saved[1]` | `[3, 4, 5, 1, 2]` |

## Complexity

| | Best | Average | Worst |
|---|---|---|---|
| Brute force time | O(n) (k % n = 0) | O(n * k) | O(n * k) |
| Optimized time | O(n) | O(n) | O(n) |
| Brute force space | O(1) | O(1) | O(1) |
| Optimized space | O(1) (k % n = 0) | O(k) | O(n) |

## Bug Review of `my_sol.py`

| # | Finding | Detail |
|---|---|---|
| 1 | Empty array crashes | `k % n` with `n == 0` raises `ZeroDivisionError`; add a guard |
| 2 | Wrong write index | `nums[n-k+1] = temp[i]` never changes with `i`, so only one slot is overwritten; should be `nums[n-k+i]` |
| 3 | No return | Returns `None`; add `return nums` if the judge expects a result |
| 4 | Approach | Shift logic (middle loop) is correct |

Fixed version with brute force + optimized: [solution.py](solution.py)
