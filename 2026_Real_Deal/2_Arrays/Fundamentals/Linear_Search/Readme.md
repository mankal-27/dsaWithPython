# Linear Search

## Problem Statement

| Item | Detail |
|---|---|
| Input | An integer array `nums` and an integer `target` |
| Output | Index of the first occurrence of `target` in `nums`, or `-1` if absent |
| Example 1 | `nums = [4, 2, 7, 1], target = 7` → `2` |
| Example 2 | `nums = [1, 2, 3], target = 9` → `-1` |
| Constraints | Array may be unsorted, empty, or contain duplicates |

## Approaches

| | Brute Force | Optimized |
|---|---|---|
| Idea | Loop over every index `0..n-1`, compare `nums[i]` with `target` | Same scan using `enumerate`, no repeated indexing |
| Code | `for i in range(len(nums))` | `for i, v in enumerate(nums)` |
| Time | O(n) | O(n) |
| Space | O(1) | O(1) |
| Explanation | Return as soon as a match is found; otherwise `-1` | Identical complexity; cleaner and more Pythonic. Unsorted data cannot be searched faster than O(n) (if sorted, use binary search, O(log n)) |

## Dry Run

`nums = [4, 2, 7, 1], target = 7`

| Step | i | nums[i] | nums[i] == 7? | Action |
|---|---|---|---|---|
| 1 | 0 | 4 | No | continue |
| 2 | 1 | 2 | No | continue |
| 3 | 2 | 7 | Yes | return 2 |

`nums = [1, 2, 3], target = 3` (the case the original code failed)

| Step | i | nums[i] | Match? | Action |
|---|---|---|---|---|
| 1 | 0 | 1 | No | continue |
| 2 | 1 | 2 | No | continue |
| 3 | 2 | 3 | Yes | return 2 |

## Complexity

| | Best | Average | Worst |
|---|---|---|---|
| Time | O(1) (target at index 0) | O(n) | O(n) (last or absent) |
| Space | O(1) | O(1) | O(1) |

## Bug Review of `my_sol.py`

| # | Bug | Why it's wrong | Fix |
|---|---|---|---|
| 1 | `range(len(nums)-1)` | Stops at index `n-2`, so the last element is never checked. `[1,2,3]`, target `3` returns `-1` instead of `2`. A single-element array `[5]` with target `5` also returns `-1` | Use `range(len(nums))` |

Fixed version: [solution.py](solution.py)
