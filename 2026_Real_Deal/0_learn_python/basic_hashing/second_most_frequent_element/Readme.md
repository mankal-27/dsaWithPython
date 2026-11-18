# Second Most Frequent Element in an Array

## Problem Statement
Given an array `arr`, return the element with the **second-highest frequency**. If several elements share that frequency, return the **smallest** value. Return `-1` if the array is empty or there is no second frequency tier (e.g. all elements have the same count).

| Input | Output | Why |
|---|---|---|
| `[1, 2, 2, 3, 3, 3]` | `2` | counts 3→3, 2→2, 1→1; second tier is 2 |
| `[1, 1, 2, 2, 3, 3, 3]` | `1` | second tier (count 2) has 1 and 2; smaller is 1 |
| `[4, 4, 4, 1, 2, 2, 3, 3, 3]` | `2` | 4 and 3 tie for max; second tier is 2 |
| `[1, 1, 2, 2]` | `-1` | only one frequency tier |
| `[3,5,4,2,2,5,1,2,3,5,4,3,2,4,1]` | `3` | 2 has count 4; 3, 4, 5 tie at 3, smallest is 3 |
| `[]` | `-1` | empty |

## Approaches

| | Brute Force | Optimized (hash map + top-2 tracking) |
|---|---|---|
| Idea | Count each value by scanning the array, then find max count, then the largest smaller count | Build `value -> count` once, then one pass keeping `max_freq` and `sec_freq` |
| Time | O(n²) | O(n) |
| Space | O(k) | O(k), k = distinct values |
| Method | `second_most_frequent_brute` | `second_most_frequent_optimized` |

## Dry Run (`[1, 2, 2, 3, 3, 3]`, map = {1:1, 2:2, 3:3})

| Step | ele, count | max_freq / max_ele | sec_freq / sec_ele | Branch |
|---|---|---|---|---|
| start | - | 0 / -1 | 0 / -1 | - |
| 1 | 1, 1 | 1 / 1 | 0 / -1 | `count > max_freq`: demote old (0, None) |
| 2 | 2, 2 | 2 / 2 | 1 / 1 | `count > max_freq`: old max (1, 1) becomes second |
| 3 | Not a bug, but note: `max_ele = min(max_ele, ele)` on a tie for max is **required** | Without it, the demoted value is the first tied value, not the smallest. `[5,5,3,3,2,2,2]` would give `5` instead of `3` | keep it (your code had it right) |
| Result | | | | **2** |

## Bug Review of `my_sol.py`

| # | Bug | Effect | Fix |
|---|---|---|---|
| 1 | `sec_max_ele = max_freq` on the demotion line (typo, should be `sec_max_freq = max_freq`) | `sec_max_freq` never updated on demotion, so it stays stale and the second tier is wrong. `[1,2,2,3,3,3]` returns `1` instead of `2` | `sec_max_freq, sec_max_ele = max_freq, max_ele` |
| 2 | `-1` sentinel for "no answer" | Matches the expected output (`-1` when there is no second tier), so this is fine | keep `-1` |
| 3 | `max_ele = min(max_ele, ele)` on tie for max | Harmless for the answer, but when two values tie for max, the loser is dropped instead of being irrelevant; just skip (`continue`) since only the second tier matters | no update needed on tie |

The core idea (hash map plus tracking top two frequencies) is correct once bug 1 is fixed.

## Complexity Summary

| Method | Time | Space |
|---|---|---|
| Brute | O(n²) | O(k) |
| Optimized | O(n) | O(k) |
