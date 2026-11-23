# Insertion Sort

## Problem
Given an array `nums`, sort it in ascending order using **insertion sort**.

| Input | Output |
|---|---|
| `[13, 46, 24, 52, 20, 9]` | `[9, 13, 20, 24, 46, 52]` |

## Approaches

| | Brute force (adjacent swaps) | Optimized (shift + insert) |
|---|---|---|
| Idea | Take item i, swap it left with its neighbour while the neighbour is bigger | Hold item i as `key`, shift bigger items right, write `key` once into the gap |
| Time | O(n²) worst/avg, O(n) best | O(n²) worst/avg, **O(n)** best (sorted) |
| Space | O(1) | O(1) |
| Writes per step | 2 per swap (3 assignments) | 1 per shift |
| Code | `insertionSortBruteForce` | `insertionSortOptimized` |

## Dry run (`[13, 46, 24, 52, 20, 9]`)

| i | key | Shifts | Array after (sorted prefix = left of `|`) |
|---|---|---|---|
| 1 | 46 | none | 13 46 \| 24 52 20 9 |
| 2 | 24 | 46 moves right | 13 24 46 \| 52 20 9 |
| 3 | 52 | none | 13 24 46 52 \| 20 9 |
| 4 | 20 | 52, 46, 24 move right | 13 20 24 46 52 \| 9 |
| 5 | 9 | 52, 46, 24, 20, 13 move right | 9 13 20 24 46 52 |

Result: `[9, 13, 20, 24, 46, 52]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best (sorted) | O(n) | O(1) | inner while never runs |
| Average / Worst (reversed) | O(n²) | O(1) | about n(n-1)/2 shifts |

Stable (shifts only when `>`, never on equal). Adaptive: fast on nearly sorted input.

## Bug review of `my_sol.py`

| Line | Bug | Fix |
|---|---|---|
| none | None found. `range(1, n)`, `j >= 0` guard before `nums[j]`, strict `>` (keeps stability) and `nums[j+1] = key` are all correct. Empty/1-element arrays are fine | n/a |
