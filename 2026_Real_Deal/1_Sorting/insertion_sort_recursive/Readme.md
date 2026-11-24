# Insertion Sort (Recursive)

## Problem
Sort `nums` in non-decreasing order using **insertion sort with recursion only**: no `for`/`while` loops, no built-in sort.

| Input | Output |
|---|---|
| `[13, 46, 24, 52, 20, 9]` | `[9, 13, 20, 24, 46, 52]` |

## Approaches

| | Brute force (swap down) | Optimized (shift) |
|---|---|---|
| Idea | Recursively sort first `size-1` items, then recursively swap `nums[size-1]` left while the left neighbour is bigger | Same recursion, but save `key`, shift bigger items right one slot, write `key` once into the gap |
| Time | O(n²) worst/avg, O(n) best | O(n²) worst/avg, O(n) best |
| Space | O(n) recursion stack | O(n) recursion stack |
| Writes per insert | 2 per step (swap) | 1 per step + 1 final |
| Code | `insertionSortBruteForce` | `insertionSortOptimized` |

## Dry run (`[13, 46, 24, 52, 20, 9]`)

| Call (size) | Inserted | Array after insert |
|---|---|---|
| 1 | base case | 13 46 24 52 20 9 |
| 2 | 46 | **13 46** 24 52 20 9 |
| 3 | 24 | **13 24 46** 52 20 9 |
| 4 | 52 | **13 24 46 52** 20 9 |
| 5 | 20 | **13 20 24 46 52** 9 |
| 6 | 9 | **9 13 20 24 46 52** |

Result: `[9, 13, 20, 24, 46, 52]`

## Complexity

| Case | Time | Space | Why |
|---|---|---|---|
| Best (sorted) | O(n) | O(n) | each insert stops after 1 compare; n stack frames |
| Average / Worst (reversed) | O(n²) | O(n) | ~n(n-1)/2 compares/moves |

Stable (stops on `<=` / shifts only on `>`), in place apart from the stack.

## Bug review of `my_sol.py`

| Line | Bug | Fix |
|---|---|---|
| `helper` | Function has no body, so it's a syntax error and the file can't run | Add base case `if size <= 1: return`, recurse on `size - 1`, then insert `nums[size-1]` |
| (missing) | No insertion step at all (needs its own recursive helper, since loops are banned) | `_swapDown` / `_shiftInsert` |
