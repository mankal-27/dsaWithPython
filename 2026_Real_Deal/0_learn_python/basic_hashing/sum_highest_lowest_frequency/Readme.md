# Sum of Highest and Lowest Frequency

## Problem Statement
Given an array `nums`, count how many times each distinct value appears. Return the **highest frequency + the lowest frequency**. Return `0` for an empty array. If there is only one distinct value, highest and lowest are the same count (answer is `2 * count`).

| Input | Output | Why |
|---|---|---|
| `[1, 2, 2, 3, 3, 3]` | `4` | counts 1→1, 2→2, 3→3; 3 + 1 |
| `[1, 1, 2, 3]` | `3` | counts 1→2, 2→1, 3→1; 2 + 1 |
| `[1, 1, 2, 2]` | `4` | all counts 2; 2 + 2 |
| `[5]` | `2` | single value, 1 + 1 |
| `[4, 4, 4, 4, 1, 2, 2]` | `5` | counts 4→4, 1→1, 2→2; 4 + 1 |
| `[]` | `0` | empty |

## Approaches

| | Brute Force | Optimized (hash map + one pass) |
|---|---|---|
| Idea | Count each value by scanning the whole array, then take max and min of the counts | Build `value -> count` once with `Counter`, then one pass tracking `max_freq` and `min_freq` |
| Time | O(n²) | O(n) |
| Space | O(k) | O(k), k = distinct values |
| Method | `sum_highest_lowest_frequency_brute` | `sum_highest_lowest_frequency_optimized` |

## Dry Run (`[1, 2, 2, 3, 3, 3]`, map = {1:1, 2:2, 3:3})

| Step | count | max_freq | min_freq | Branch |
|---|---|---|---|---|
| start | - | 0 | 6 (`len(nums)`) | - |
| 1 | 1 | 1 | 1 | new max and new min |
| 2 | 2 | 2 | 1 | new max |
| 3 | 3 | 3 | 1 | new max |
| Result | | | | **3 + 1 = 4** |

## Bug Review of `my_sol.py`

| # | Bug | Effect | Fix |
|---|---|---|---|
| 1 | `for count in freq_map.items()` | `.items()` yields `(value, count)` tuples, so `count > max_freq` compares a tuple to an int and raises `TypeError` on any non-empty input | `for count in freq_map.values()` |
| 2 | `min_freq = len(nums)` | Not a bug: a count can never exceed `len(nums)`, so it is a safe starting "infinity" | keep |
| 3 | `if not nums: return 0` | Not a bug: handles the empty case | keep |

The idea (Counter plus tracking max and min) is correct once bug 1 is fixed.

## Complexity Summary

| Method | Time | Space |
|---|---|---|
| Brute | O(n²) | O(k) |
| Optimized | O(n) | O(k) |
