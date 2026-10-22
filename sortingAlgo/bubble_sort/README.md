# Bubble Sort

**Topic:** Sorting Algorithms
**Difficulty:** Easy (concept chapter)
**Link:** https://algomaster.io/learn/dsa/bubble-sort
**Files:** `ch1.py` (implementation)

> This is a concept chapter on algomaster.io, not a problem with a fixed input/output statement, so there is no "Problem Statement" with examples and constraints. The task is: **implement bubble sort** so it sorts an array in ascending order, in place, with the early-termination optimization.

## What Is Bubble Sort?

Bubble sort is a comparison-based sorting algorithm. It repeatedly steps through the array, compares each pair of adjacent elements, and swaps them if they are in the wrong order. Each full pass moves the largest unsorted element to its final position at the end of the array, like a bubble rising to the surface. After pass 1 the largest element is last; after pass 2 the second largest is second from last; after n-1 passes the array is sorted.

## How It Works

1. Start at the beginning of the array.
2. Compare the current element with the next one.
3. If the current is greater than the next, swap them.
4. Move to the next pair and repeat steps 2-3.
5. After one full pass, the largest unsorted element sits at the end.
6. Repeat for the remaining unsorted portion (the inner loop shrinks by one each pass).
7. Stop early if a pass makes no swaps - the array is already sorted.

## How to Solve It - Thought Process

The core observation is that one pass of "compare neighbours and swap if out of order" is guaranteed to carry the largest value in the unsorted part all the way to its end, because a large value keeps winning every comparison and keeps being swapped forward. So a single pass permanently fixes one element's position. Repeating that n-1 times fixes n-1 elements, and the last one is then automatically in place. That gives the outer loop (`for i in range(n-1)`: counts passes).

Two refinements follow naturally. First, after `i` passes the last `i` elements are already final, so there is no reason to compare into them: the inner loop only needs to run `n - 1 - i` times. (This is also what keeps `arr[j+1]` in bounds.) Second, if a pass makes zero swaps, every adjacent pair is already in order, which means the whole array is sorted - so keep a `swapped` flag that is reset at the start of each pass and checked at the end. That single flag turns the best case (already sorted input) from O(n^2) into O(n).

The comparison uses strict `>`, not `>=`. Equal elements are never swapped, so their original relative order is preserved - that is what makes bubble sort **stable**.

## Brute Force Solution - No Early Exit

Always runs all n-1 passes, even if the array became sorted early:

```python
def bubble_sort_basic(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## Optimized Solution - With Early Termination (your `ch1.py`)

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(n - 1 - i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # Early exit if no swaps
        if not swapped:
            break

    return arr
```

Verified: matches `sorted()` on 2,000 random arrays (lengths 0-15, including negatives and duplicates), and handles `[]` and `[1]` (the outer `range(n-1)` is empty, so it just returns the input). No bugs found.

## Dry Run

### Optimized - `arr = [5, 3, 8, 4, 2]` (needs every pass)

Each row is one comparison of `arr[j]` and `arr[j+1]`; the array shown is the state *after* that step.

**Pass 1** (`i=0`, inner loop `j = 0..3`)

| j | Compare | Action | Array after |
|---|---|---|---|
| 0 | 5 > 3 | swap | `[3, 5, 8, 4, 2]` |
| 1 | 5 > 8? no | - | `[3, 5, 8, 4, 2]` |
| 2 | 8 > 4 | swap | `[3, 5, 4, 8, 2]` |
| 3 | 8 > 2 | swap | `[3, 5, 4, 2, 8]` |

`swapped = True` -> 8 is now fixed at the end.

**Pass 2** (`i=1`, `j = 0..2`)

| j | Compare | Action | Array after |
|---|---|---|---|
| 0 | 3 > 5? no | - | `[3, 5, 4, 2, 8]` |
| 1 | 5 > 4 | swap | `[3, 4, 5, 2, 8]` |
| 2 | 5 > 2 | swap | `[3, 4, 2, 5, 8]` |

`swapped = True` -> 5 is fixed.

**Pass 3** (`i=2`, `j = 0..1`)

| j | Compare | Action | Array after |
|---|---|---|---|
| 0 | 3 > 4? no | - | `[3, 4, 2, 5, 8]` |
| 1 | 4 > 2 | swap | `[3, 2, 4, 5, 8]` |

`swapped = True` -> 4 is fixed.

**Pass 4** (`i=3`, `j = 0`)

| j | Compare | Action | Array after |
|---|---|---|---|
| 0 | 3 > 2 | swap | `[2, 3, 4, 5, 8]` |

`swapped = True`; the outer loop ends (`range(4)` exhausted). Return `[2, 3, 4, 5, 8]`.

Totals: **10 comparisons, 7 swaps** (10 = 4+3+2+1 = n(n-1)/2).

### Optimized - early exit, `arr = [1, 2, 3, 4, 5]` (already sorted)

**Pass 1** (`i=0`, `j = 0..3`)

| j | Compare | Action | Array after |
|---|---|---|---|
| 0 | 1 > 2? no | - | `[1, 2, 3, 4, 5]` |
| 1 | 2 > 3? no | - | `[1, 2, 3, 4, 5]` |
| 2 | 3 > 4? no | - | `[1, 2, 3, 4, 5]` |
| 3 | 4 > 5? no | - | `[1, 2, 3, 4, 5]` |

`swapped` is still `False` -> `break`. Return immediately.

Totals: **4 comparisons, 0 swaps** - the basic version would have done 10 comparisons.

### Brute Force (no flag)

Produces the same swaps as the first trace above, but on `[1, 2, 3, 4, 5]` it would still run all 4 passes (4+3+2+1 = 10 comparisons) before returning.

## Complexity

| Case | Time | Space | Notes |
|---|---|---|---|
| Best (already sorted) | O(n) | O(1) | One pass, zero swaps, `swapped` stays False -> early exit. n-1 comparisons. (Basic version without the flag is still O(n^2).) |
| Average | O(n^2) | O(1) | Random order: about half the pairs swap, but the nested loops still give quadratic time. |
| Worst (reverse sorted) | O(n^2) | O(1) | Every comparison swaps: exactly n(n-1)/2 comparisons and swaps. |

- **In place:** only the swap and the `swapped` flag use extra memory.
- **Stable:** strict `>` never swaps equal elements.
- **Scale check (n = 10,000):** sorted input ~10,000 comparisons with the flag vs ~50,000,000 without it - about 5,000x less work.

## When to Use / Not Use

Good for: nearly sorted data (close to O(n) with the flag), very small arrays, quickly checking whether an array is already sorted (one pass, O(n), O(1) space), memory-constrained environments, and teaching. Poor for: large datasets, performance-critical code, and random or reverse-sorted data (insertion sort does fewer swaps; merge sort/quicksort are O(n log n)).

## Real-World Use Case

Bubble sort itself is rarely shipped, but its pattern is. The "one pass, no swaps means already sorted" check is a cheap sortedness test used before running heavier work. Small-n sorting inside hybrid algorithms (Timsort and introsort switch to a simple quadratic sort like insertion sort for tiny runs) follows the same reasoning that simple beats clever at small sizes. Stable adjacent-swap sorting also appears in embedded and firmware code where O(1) extra memory matters, and in teaching tools and sorting visualizers because every swap is easy to animate.

## Tests (planned)

To add when you want them (`test_ch1.py`): empty list, single element, two elements (sorted and swapped), already sorted, reverse sorted, all equal, duplicates, negatives, plus a comparison against `sorted()` on random arrays. Say "chkup" or "updated sol.py" and I'll write and verify them.
