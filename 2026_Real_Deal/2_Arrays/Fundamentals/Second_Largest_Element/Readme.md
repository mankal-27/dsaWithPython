# Second Largest Element in an Array

## Problem Statement

| Item | Detail |
|---|---|
| Input | An integer array `nums` |
| Output | The second largest **distinct** value (`-1` if it doesn't exist) |
| Example 1 | `nums = [3, 1, 4, 1, 5]` → `4` |
| Example 2 | `nums = [-5, -2, -9]` → `-5` |
| Example 3 | `nums = [5, 5, 5]` → `-1` (no distinct second value) |
| Constraints | Values may be negative or duplicated; array may have 0 or 1 elements |

## Approaches

| | Brute Force | Better | Optimized |
|---|---|---|---|
| Idea | Sort, walk back from the end to the first value != largest | Pass 1: find largest. Pass 2: max of values != largest | One pass tracking `largest` and `second_largest` |
| Time | O(n log n) | O(2n) = O(n) | O(n) |
| Space | O(n) sorted copy | O(1) | O(1) |
| Explanation | Duplicates of the max must be skipped, so you can't just take `[-2]` | Simple and safe, but reads the array twice | When a new max appears, the old max becomes second; otherwise update second only if value is strictly between |

## Dry Run (Optimized)

`nums = [3, 1, 4, 1, 5]`

| Step | value | Case | largest | second_largest |
|---|---|---|---|---|
| init | 3 | - | 3 | None |
| 1 | 1 | `< largest`, second is None → set | 3 | 1 |
| 2 | 4 | `> largest` → shift | 4 | 3 |
| 3 | 1 | `< largest`, not `> second` | 4 | 3 |
| 4 | 5 | `> largest` → shift | 5 | 4 |

Result: `4`

## Complexity

| | Best | Average | Worst |
|---|---|---|---|
| Brute force time | O(n log n) | O(n log n) | O(n log n) |
| Better time | O(n) | O(n) | O(n) |
| Optimized time | O(n) | O(n) | O(n) |
| Brute force space | O(n) | O(n) | O(n) |
| Better / Optimized space | O(1) | O(1) | O(1) |

## Bug Review of `my_sol.py`

| # | Bug | Why it's wrong | Fix |
|---|---|---|---|
| 1 | `second_largest = -1` sentinel (brute + better + optimized) | `-1` is a valid element: `[-5, -2, -9]` returns `-1` instead of `-5`; also can't tell "not found" from a real `-1` | Track with `None` internally, convert to `-1` only on return |
| 2 | `secondLargestElementOptimized` is unfinished | No loop and no return → always returns `None` | Single-pass top-two tracking |
| 3 | `len(nums) < 2` returns `-1` | Correct per spec (not a bug) | Fine as the final answer (spec says `-1`), but internal state must still use `None` |

Note: input `[1000, -1000]` must return `-1000`; a `-1` sentinel returns `-1`. Brute force and Better logic is otherwise correct for non-negative input.

Fixed version: [solution.py](solution.py)
