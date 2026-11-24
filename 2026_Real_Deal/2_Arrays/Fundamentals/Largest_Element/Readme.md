# Largest Element in an Array

## Problem Statement

| Item | Detail |
|---|---|
| Input | An integer array `nums` |
| Output | The largest value in `nums` (`None` if the array is empty) |
| Example 1 | `nums = [3, 1, 4, 1, 5]` → `5` |
| Example 2 | `nums = [-5, -2, -9]` → `-2` |
| Constraints | Values may be negative or duplicated; array may have one element or be empty |

## Approaches

| | Brute Force | Optimized |
|---|---|---|
| Idea | Sort the array, the last element is the largest | Scan once, keep a running maximum |
| Code | `sorted(nums)[-1]` | `if nums[i] > largest: largest = nums[i]` |
| Time | O(n log n) | O(n) |
| Space | O(n) for the sorted copy (O(1) if sorted in place) | O(1) |
| Explanation | Simple but does far more work than needed: ordering everything just to read one value | Every element is looked at exactly once; start `largest` at `nums[0]` (not 0, which breaks for all-negative arrays) |

## Dry Run

`nums = [3, 1, 4, 1, 5]`

| Step | i | nums[i] | nums[i] > largest? | largest after |
|---|---|---|---|---|
| init | - | - | - | 3 |
| 1 | 1 | 1 | No | 3 |
| 2 | 2 | 4 | Yes | 4 |
| 3 | 3 | 1 | No | 4 |
| 4 | 4 | 5 | Yes | 5 |

Result: `5`

## Complexity

| | Best | Average | Worst |
|---|---|---|---|
| Brute force time | O(n log n) | O(n log n) | O(n log n) |
| Optimized time | O(n) | O(n) | O(n) |
| Brute force space | O(n) | O(n) | O(n) |
| Optimized space | O(1) | O(1) | O(1) |

O(n) is optimal: every element must be inspected at least once.

## Bug Review of `my_sol.py`

| # | Bug | Why it's wrong | Fix |
|---|---|---|---|
| 1 | `nums.sort()` in brute force | Mutates the caller's list (side effect) | Use `sorted(nums)` (a copy) |
| 2 | No empty-array guard (both methods) | `nums[-1]` / `nums[0]` raise `IndexError` on `[]` | `if not nums: return None` |
| 3 | `range(len(nums))` in optimized (minor) | Compares `nums[0]` with itself, one wasted step; not incorrect | `range(1, len(nums))` |

The core logic of both methods is correct for non-empty input.

Fixed version: [solution.py](solution.py)
