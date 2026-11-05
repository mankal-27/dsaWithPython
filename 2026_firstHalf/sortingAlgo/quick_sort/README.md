# Quick Sort

**Topic:** Sorting Algorithms
**Difficulty:** Medium (concept chapter)
**Link:** https://algomaster.io/learn/dsa/quick-sort
**Files:** `ch1.py` (implementation - **in progress**)

> This is a concept chapter on algomaster.io, not a problem with a fixed input/output statement, so there is no "Problem Statement" with examples and constraints. The task is: **implement quick sort** (Lomuto partition) so it sorts an array in ascending order, in place.

> ℹ️ **Status of `ch1.py`: unfinished.** The file currently contains only the setup of an iterative version (an explicit stack, popping a range, choosing `pivot = arr[high]`, and `i = low - 1`). There is no partition loop, no pivot placement, no pushing of sub-ranges, and no `return`. Calling `quick_sort([3, 1, 2])` returns `None` and leaves the list unchanged. This is not a bug in finished code, just work in progress, so the README below describes the intended algorithm and the dry run uses a reference version, not your file. Tell me when it's done ("chkup") and I'll verify it and update this README.

## What Is Quick Sort?

Quick sort is a divide-and-conquer algorithm built around **partitioning**:

1. Pick a **pivot** element.
2. Rearrange the array so everything smaller than (or equal to) the pivot is on its left and everything larger is on its right. The pivot lands in its final sorted position.
3. Repeat the process on the left part and the right part.

Merge sort does its work when combining; quick sort does its work when splitting. By the time recursion reaches size 0 or 1, the array is already sorted and nothing needs combining.

## How It Works - Lomuto Partition

(The scheme used in the chapter; Hoare's scheme uses two converging pointers and about 3x fewer swaps, but is trickier to get right.)

1. If the range has fewer than 2 elements, stop.
2. Pivot = last element of the range (`arr[high]`).
3. `i = low - 1` marks the end of the "<= pivot" region.
4. For `j` from `low` to `high - 1`: if `arr[j] <= pivot`, do `i += 1` and swap `arr[i]` with `arr[j]`.
5. Swap the pivot (at `high`) with `arr[i + 1]`. The pivot is now at index `i + 1`, its final position.
6. Sort the range left of the pivot and the range right of it.

## How to Solve It - Thought Process

The whole algorithm rests on one guarantee: after partitioning, the pivot is exactly where it will end up in the sorted array, and nothing will ever cross it again. So the two sides can be sorted completely independently, and each recursive call fixes at least one more element permanently.

Lomuto's trick for partitioning in one left-to-right scan is to maintain two regions inside the range: a "small" region `[low..i]` of elements <= pivot, and a "large" region `[i+1..j-1]` of elements > pivot, with the unexamined part `[j..high-1]` beyond. Each new element either extends the large region (just advance `j`) or belongs in the small region (grow the small region by one with `i += 1` and swap the element into that slot, which pushes one large element along). At the end the pivot, parked at `high` the whole time, is swapped into slot `i + 1`, right between the two regions.

Your design choice: using an explicit **stack of `(low, high)` pairs** instead of recursion. Pop a range, partition it, push the left and right sub-ranges, repeat until the stack is empty. This sidesteps Python's recursion limit and makes the worst-case stack growth visible. A common refinement is to push the larger sub-range first so the smaller one is processed next, keeping the stack at O(log n) even in the worst case.

Pivot choice drives performance. Always taking the last element is O(n^2) on already sorted (or reverse sorted) input, because every partition peels off just one element. Random pivots or median-of-three make that unlikely.

## Brute Force Solution

Simple but not in place - build new lists around the pivot:

```python
def quick_sort_simple(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = [x for x in arr[:-1] if x <= pivot]
    larger = [x for x in arr[:-1] if x > pivot]
    return quick_sort_simple(smaller) + [pivot] + quick_sort_simple(larger)
```

## Optimized Solution - In-Place Lomuto with Explicit Stack (your `ch1.py`, unfinished)

What you have so far:

```python
def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while(stack):
        low, high = stack.pop()

        if low < high:
            pivot = arr[high]
            i = low - 1
```

Remaining to write: the scan loop (step 4), the pivot swap (step 5), pushing the two sub-ranges `(low, p - 1)` and `(p + 1, high)`, and `return arr`.

## Dry Run

Reference trace of the algorithm above (not your file) on the chapter's example `[10, 7, 8, 9, 1, 5]`:

**Range `[0, 5]`**, pivot = 5, `i = -1`

| j | arr[j] | arr[j] <= 5? | Action | Array |
|---|---|---|---|---|
| 0 | 10 | no | skip | `[10, 7, 8, 9, 1, 5]` |
| 1 | 7 | no | skip | same |
| 2 | 8 | no | skip | same |
| 3 | 9 | no | skip | same |
| 4 | 1 | yes | `i = 0`, swap `arr[0]` and `arr[4]` | `[1, 7, 8, 9, 10, 5]` |

Place pivot: swap `arr[i+1] = arr[1]` with `arr[5]` -> `[1, 5, 8, 9, 10, 7]`. Pivot 5 is final at index 1. Push `(0, 0)` and `(2, 5)`.

**Range `[2, 5]`**, pivot = 7: elements 8, 9, 10 are all > 7, so `i` stays 1. Place pivot at index 2 -> `[1, 5, 7, 9, 10, 8]`.

**Range `[3, 5]`**, pivot = 8: 9, 10 both > 8. Pivot to index 3 -> `[1, 5, 7, 8, 10, 9]`.

**Range `[4, 5]`**, pivot = 9: 10 > 9. Pivot to index 4 -> `[1, 5, 7, 8, 9, 10]`.

Remaining ranges have fewer than 2 elements. Result `[1, 5, 7, 8, 9, 10]`. (This input is close to the bad case: with a last-element pivot most partitions are lopsided, which is the O(n^2) behaviour in miniature.)

### Stability check: `[3a, 1, 3b, 2]`

Pivot 2: `1 <= 2` moves 1 to the front, then the pivot swaps into index 1, giving `[1, 2, 3b, 3a]`. The 3s swapped order, so quick sort is **not stable**.

## Complexity

| Case | Time | Space (stack) | Notes |
|---|---|---|---|
| Best | O(n log n) | O(log n) | Pivot splits the range in half each time. |
| Average | O(n log n) | O(log n) | Random-ish input. |
| Worst | O(n^2) | O(n) | Pivot is always the min or max, e.g. last-element pivot on sorted input. (With the larger-side-first stack trick the stack stays O(log n).) |

| Property | Value |
|---|---|
| In place | Yes |
| Stable | No (long-distance swaps) |
| Adaptive | No (last-element pivot is actually worst on sorted input) |
| Cache behaviour | Excellent - sequential scans over contiguous memory |

**Pivot strategies:** first/last element (trivial, bad on sorted data), random pivot (easy, makes the worst case very unlikely), median-of-three (used by standard libraries such as C++ `std::sort`).

## When to Use / Not Use

Good for: general-purpose sorting of arrays, memory-constrained settings (O(log n) stack, no extra arrays), cache-friendly workloads, and cases where average performance matters more than the worst case. Not ideal for: worst-case-sensitive or adversarial input (use merge or heap sort), when stability is required, linked lists (merge sort fits better), and tiny subarrays (optimized versions switch to insertion sort below roughly 10-20 elements).

## Real-World Use Case

Quick sort and its descendants are the default array sorters in much of the standard-library world: C's `qsort` has historically been quick-sort based, C++ `std::sort` is introsort (quick sort with median-of-three pivots, falling back to heap sort when recursion gets too deep and to insertion sort for tiny ranges), and many language runtimes use similar hybrids for primitive arrays. Databases use quick-sort-style partitioning for in-memory sorting steps, and the same partition routine powers **quickselect**, used to find medians and top-k elements without a full sort.

## Tests (planned)

To add once `ch1.py` is finished (`test_ch1.py`): empty list, single element, two elements, already sorted, reverse sorted (the worst case for last-element pivot), all equal, duplicates, negatives, the chapter example `[10, 7, 8, 9, 1, 5]`, a large sorted list to confirm the stack handles depth, plus a comparison against `sorted()` on random arrays. Say "chkup" when it's ready.
