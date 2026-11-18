# Most Frequent Element in an Array

## Problem Statement
Given an array `arr`, return the element that occurs the most times. Return `None` for an empty array. If several elements tie, return the **smallest** value.

| Input | Output | Why |
|---|---|---|
| `[1, 2, 2, 3, 3, 3]` | `3` | 3 appears 3 times |
| `[1, 2, 2, 1]` | `1` | tie, 1 is smaller |
| `[10000, 10000, 9999, 9999]` | `9999` | tie, 9999 is smaller |
| `[]` | `None` | empty |

## Approaches

| | Brute Force | Optimized (hash map) |
|---|---|---|
| Idea | For each element, scan the whole array and count it | One pass to build `value -> count`, then pick the max |
| Time | O(n²) | O(n) |
| Space | O(1) | O(k), k = distinct values |
| Method | `most_frequent_brute` | `most_frequent_optimized` |

## Dry Run (`[1, 2, 2, 3, 3, 3]`)

| Step | num | freq_map | best (value, count) |
|---|---|---|---|
| 1 | 1 | {1:1} | - |
| 2 | 2 | {1:1, 2:1} | - |
| 3 | 2 | {1:1, 2:2} | - |
| 4-6 | 3,3,3 | {1:1, 2:2, 3:3} | - |
| Pick | 1 | count 1 > 0 | (1, 1) |
| Pick | 2 | 2 > 1 | (2, 2) |
| Pick | 3 | 3 > 2 | (3, 3) -> **3** |

## Bug Review of `my_sol.py`

| # | Bug | Effect | Fix |
|---|---|---|---|
| 1 | `most_frequent_pythonic(arr)` has no `self` | `TypeError` when called on a `Solution()` instance | add `self` |
| 2 | On-the-fly update returns the value that *reaches* the max first | `[1,2,2,1]` gives `2`, but `Counter` gives `1`; inconsistent tie handling | count first, then pick max in insertion order (strict `>`) |

The core idea (hash map of counts) is correct.

## Complexity Summary

| Method | Time | Space |
|---|---|---|
| Brute | O(n²) | O(1) |
| Optimized | O(n) | O(k) |
| Counter | O(n) | O(k) |
