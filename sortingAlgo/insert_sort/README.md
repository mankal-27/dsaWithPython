# Insertion Sort

**Topic:** Sorting Algorithms
**Difficulty:** Easy (concept chapter)
**Link:** https://algomaster.io/learn/dsa/insertion-sort
**Files:** `ch1.py` (implementation)

> This is a concept chapter on algomaster.io, not a problem with a fixed input/output statement, so there is no "Problem Statement" with examples and constraints. The task is: **implement insertion sort** so it sorts an array in ascending order, in place.

## What Is Insertion Sort?

Insertion sort builds a sorted prefix one element at a time, like sorting playing cards in your hand. The array is split into a **sorted region** on the left and an **unsorted region** on the right. Each step takes the first element of the unsorted region (the `key`) and inserts it into its correct position inside the sorted region, shifting larger elements one slot to the right to make room.

## How It Works

1. Start at index 1 (a single first element is already "sorted").
2. Save the current element as `key`.
3. Compare `key` with elements of the sorted region, moving right to left.
4. Shift every element greater than `key` one position to the right.
5. Drop `key` into the gap that opens up.
6. Move to the next unsorted element and repeat.

The standard version *shifts* rather than swaps: a shift is one assignment, while a swap is three (with a temp variable). The inner `while` loop stops at the first element that is less than or equal to `key`.

## How to Solve It - Thought Process

Think of the left part of the array as always being sorted. Adding one more element to a sorted list only requires finding where it belongs: walk left from the new element past everything bigger than it, then stop. That is the whole algorithm - the outer loop grows the sorted prefix (`i = 1 .. n-1`) and the inner loop finds the insertion point.

The efficient way to do the walk is to combine searching and making room in one motion. Save the element in `key` first (otherwise the first shift would overwrite it), then slide each larger element right by one. When the loop stops, `j` points at the last element that is not greater than `key` (or `-1` if `key` is the new minimum), so the gap is at `j + 1` - that is why the final assignment is `arr[j + 1] = key`.

Two properties fall out of the inner loop condition `arr[j] > key`. Because it is strict, equal elements are never shifted past each other, so the sort is **stable**. And because the loop exits immediately when the left neighbour is already smaller, an already-sorted array costs just one comparison per element, so the sort is **adaptive**: best case O(n). Condition order matters too: `j >= 0` is checked first so `arr[j]` is never read at index -1 (which in Python would silently wrap to the last element rather than raise an error).

## Brute Force Solution - Swap Version

Insert by repeatedly swapping adjacent elements backwards. Correct, but it does 3 assignments per step instead of 1:

```python
def insertion_sort_swap(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr
```

## Optimized Solution - Shift and Place (your `ch1.py`)

```python
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert Key ar the correct position
        arr[j+1] = key

    return arr
```

Verified: matches `sorted()` on 3,000 random arrays (lengths 0-15, negatives and duplicates), and handles `[]` and `[1]` (the outer `range(1, n)` is empty). No bugs found. (Only nit: a typo in a comment, "ar" for "at" - harmless.)

## Dry Run

### `arr = [5, 2, 4, 6, 1, 3]`

"Comparisons" below counts `arr[j] > key` checks; each shift is one assignment.

| i | key | Shifts (arr[j] > key) | Stops because | Placed at | Array after |
|---|---|---|---|---|---|
| 1 | 2 | 5 | `j` reached -1 | index 0 | `[2, 5, 4, 6, 1, 3]` |
| 2 | 4 | 5 | 2 > 4? no | index 1 | `[2, 4, 5, 6, 1, 3]` |
| 3 | 6 | none | 5 > 6? no | index 3 (stays) | `[2, 4, 5, 6, 1, 3]` |
| 4 | 1 | 6, 5, 4, 2 | `j` reached -1 | index 0 | `[1, 2, 4, 5, 6, 3]` |
| 5 | 3 | 6, 5, 4 | 2 > 3? no | index 2 | `[1, 2, 3, 4, 5, 6]` |

Detail of the longest step, `i = 4`, `key = 1` (array starts `[2, 4, 5, 6, 1, 3]`):

| j | Check | Action | Array |
|---|---|---|---|
| 3 | 6 > 1 | shift | `[2, 4, 5, 6, 6, 3]` |
| 2 | 5 > 1 | shift | `[2, 4, 5, 5, 6, 3]` |
| 1 | 4 > 1 | shift | `[2, 4, 4, 5, 6, 3]` |
| 0 | 2 > 1 | shift | `[2, 2, 4, 5, 6, 3]` |
| -1 | `j >= 0` fails | place `key` at `arr[0]` | `[1, 2, 4, 5, 6, 3]` |

Result `[1, 2, 3, 4, 5, 6]`. Totals: **12 element comparisons, 9 shifts** (9 = the number of inversions in the input).

### Already sorted: `arr = [1, 2, 3, 4, 5]`

Each `key` is compared once with its left neighbour, the check fails immediately, and `key` is written back to its own slot: **4 comparisons, 0 shifts** - this is the O(n) best case. Selection sort needs 10 comparisons on the same input.

### Reverse sorted: `arr = [5, 4, 3, 2, 1]`

Every key travels to the front: 1 + 2 + 3 + 4 = **10 comparisons and 10 shifts** - the O(n^2) worst case, n(n-1)/2.

### Stability check: `[(3,'a'), (1,'x'), (3,'b'), (2,'y')]` sorted by number

Result `[(1,'x'), (2,'y'), (3,'a'), (3,'b')]` (confirmed by running the code): `3a` stays ahead of `3b`, because `3a > 3b` is false so it is never shifted past.

## Complexity

| Case | Time | Space | Notes |
|---|---|---|---|
| Best (already sorted) | O(n) | O(1) | Inner loop exits immediately every time; n-1 comparisons. |
| Average | O(n^2) | O(1) | Each element moves past about half the sorted region. |
| Worst (reverse sorted) | O(n^2) | O(1) | Every element travels to the front: n(n-1)/2 shifts. |

| Property | Value |
|---|---|
| In place | Yes |
| Stable | Yes (strict `>`) |
| Adaptive | Yes - running time is about n + (number of inversions) |
| Online | Yes - can sort as elements arrive |

**Comparison with the other two O(n^2) sorts:**

| | Bubble | Selection | Insertion |
|---|---|---|---|
| Best case | O(n) with flag | O(n^2) | O(n) |
| Swaps / writes | up to O(n^2) | at most n-1 | up to O(n^2) shifts (1 write each) |
| Stable | Yes | No | Yes |
| Adaptive | Yes | No | Yes |

## When to Use / Not Use

Good for: nearly sorted data (about n comparisons with few inversions), small arrays (under roughly 10-20 elements), online sorting where items arrive one at a time and the collection must stay sorted, and as the small-run subroutine inside hybrid sorts. Poor for: large random data (n = 1,000,000 needs about 250 billion comparisons on average vs about 20 million for merge sort) and any performance-critical path where input is not guaranteed small or nearly sorted.

## Real-World Use Case

Insertion sort is the workhorse hiding inside production sorting libraries. Python's built-in `sorted()`/`list.sort()` (Timsort) and Java's object sort use insertion sort (in Timsort's case, a binary-insertion variant) to sort short runs, typically fewer than 64 elements, before merging them. C++'s `std::sort` (introsort) falls back to insertion sort once partitions shrink below about 16 elements. Shell sort is built from it with varying gaps. It is also the right tool for keeping a small live list sorted as items arrive, such as maintaining a leaderboard or a priority list where each new score is inserted into place.

## Tests (planned)

To add when you want them (`test_ch1.py`): empty list, single element, two elements (sorted and swapped), already sorted, reverse sorted, all equal, duplicates, negatives, the stability example above, a "new minimum last" case (exercises `j` reaching -1), plus a comparison against `sorted()` on random arrays. Say "chkup" and I'll write and verify them.
