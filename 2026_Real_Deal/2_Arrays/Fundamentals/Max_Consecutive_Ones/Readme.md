# Max Consecutive Ones

## Problem Statement

| Item | Detail |
|---|---|
| Input | A binary array `nums` (each element is `0` or `1`) |
| Output | The length of the longest run of consecutive `1`s |
| Example 1 | `nums = [1, 1, 0, 1, 1, 1]` → `3` |
| Example 2 | `nums = [1, 0, 1, 1, 0, 1]` → `2` |
| Example 3 | `nums = [0, 0, 0]` → `0` |
| Constraints | Array may be empty or contain only 0s / only 1s |

## Approaches

| | Brute Force | Optimized |
|---|---|---|
| Idea | From every index, walk right while the value is `1` and record the run length | One pass: `1` → extend current run and update best; `0` → reset current run |
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |
| Explanation | Re-counts the same 1s many times (e.g. all-ones array) | Each element is looked at once; the run counter only needs the current streak |

## Dry Run (Optimized)

`nums = [1, 1, 0, 1, 1, 1]`

| Step | value | Action | current_run | longest_run |
|---|---|---|---|---|
| 0 | 1 | extend | 1 | 1 |
| 1 | 1 | extend | 2 | 2 |
| 2 | 0 | reset | 0 | 2 |
| 3 | 1 | extend | 1 | 2 |
| 4 | 1 | extend | 2 | 2 |
| 5 | 1 | extend | 3 | 3 |

Result: `3`

## Complexity

| | Best | Average | Worst |
|---|---|---|---|
| Brute force time | O(n) (all zeros) | O(n²) | O(n²) (all ones) |
| Optimized time | O(n) | O(n) | O(n) |
| Space (both) | O(1) | O(1) | O(1) |

## Bug Review of `my_sol.py`

| # | Finding | Detail |
|---|---|---|
| 1 | No bugs | Logic is correct and already optimal: O(n) time, O(1) space |
| 2 | Edge cases | `[]` → `0`, all zeros → `0`, all ones → `n`: all correct |
| 3 | Minor style | `max(...)` runs on every `1`; fine, it just needs to be updated at least once per run |

Restructured version with brute force + optimized: [solution.py](solution.py)
