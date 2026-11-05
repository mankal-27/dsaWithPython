# Shell Sort

**Topic:** Sorting Algorithms
**Difficulty:** Easy-Medium (concept chapter)
**Link:** https://algomaster.io/learn/dsa/shell-sort
**Files:** `ch1.py` (implementation)

> This is a concept chapter on algomaster.io, not a problem with a fixed input/output statement, so there is no "Problem Statement" with examples and constraints. The task is: **implement shell sort** so it sorts an array in ascending order, in place, using Shell's original gap sequence (n/2, n/4, ..., 1).

## What Is Shell Sort?

Shell sort is a generalization of insertion sort that lets elements move across large distances early. Instead of comparing adjacent elements, it compares elements `gap` positions apart and runs an insertion sort over each group of elements spaced `gap` apart. The gap shrinks each round until it reaches 1, at which point it is an ordinary insertion sort, but on an array that is already nearly sorted, so that last pass is close to O(n).

## How It Works

1. Start with `gap = n // 2`.
2. For each `i` from `gap` to `n - 1`: save `key = arr[i]`, set `j = i`.
3. While `j >= gap` and `arr[j - gap] > key`: shift `arr[j - gap]` into `arr[j]` and **step `j` back by `gap`**.
4. Put `key` at `arr[j]`.
5. Halve the gap and repeat until the gap reaches 0 (the last round used gap 1).

It is exactly insertion sort with `1` replaced by `gap`.

## How to Solve It - Thought Process

Insertion sort is slow because each comparison/shift moves an element only one slot, so an element that is far from home takes many steps. Shell sort's idea: first fix gross disorder cheaply by sorting elements that are far apart (large gap), where each shift covers a long distance. Each smaller gap then has less left to fix, and by gap 1 almost nothing needs to move.

Start by writing insertion sort, then generalize: every `1` in "look at the neighbour" becomes `gap`. The start of the loop moves from index 1 to index `gap` (the first element that has a gap-distant predecessor), the loop condition becomes `j >= gap` (so `arr[j - gap]` exists), the comparison is `arr[j - gap] > key`, and the walk-back is `j -= gap`. Wrap that in an outer loop that halves `gap`.

Gap sequence matters: Shell's original (n/2, n/4, ..., 1) is simplest but has an O(n^2) worst case because with powers of two, even-position and odd-position elements are never compared together until the last gap-1 pass. Hibbard (2^k - 1), Knuth ((3^k - 1) / 2) and Sedgewick sequences give O(n^(3/2)) or better. Like insertion sort, shifts use `>` so the result is **not** stable overall (equal elements in different gap-groups can cross).

## Brute Force Solution - Plain Insertion Sort

The gap-1 special case and the baseline shell sort improves on:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

## Optimized Solution - Gapped Insertion Sort (your `ch1.py`)

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0 :
        for i in range(gap, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]

            arr[j] = key

        gap //= 2
    return arr
```

> ⚠️ **Known bug (infinite loop):** the inner `while` loop shifts `arr[j - gap]` into `arr[j]` but never moves `j`. There is no `j -= gap` after the shift, so if the condition `j >= gap and arr[j - gap] > key` is true even once, it stays true forever (`j` and `arr[j - gap]` don't change; `key` doesn't change) and the program hangs.
>
> **Confirmed by running the code** (with a 5-second timeout):
>
> | Input | Result |
> |---|---|
> | `[]` | returns `[]` |
> | `[1]` | returns `[1]` |
> | `[1, 2]` | returns `[1, 2]` |
> | `[1, 2, 3, 4, 5]` | returns `[1, 2, 3, 4, 5]` |
> | `[2, 1]` | **hangs** (timed out) |
>
> It only terminates on inputs where no gapped comparison ever finds a larger element earlier, i.e. already-sorted arrays. Any array that actually needs sorting hangs. Trace of `[2, 1]`: `n = 2`, `gap = 1`, `i = 1`, `key = 1`, `j = 1`. Check: `j >= 1` yes, `arr[0] = 2 > 1` yes -> `arr[1] = 2` (array is now `[2, 2]`), `j` stays 1. Check again: `arr[0] = 2 > 1` still yes -> infinite loop.
>
> This README documents the bug rather than fixing it; the one-line change is to add `j -= gap` as the last line of the inner `while` body, i.e. right after `arr[j] = arr[j - gap]`. With that line added, a copy of the function sorted 2,000 random arrays (length 0-15, negatives and duplicates) correctly. Say the word if you want it applied.

## Dry Run

Intended algorithm (a copy with `j -= gap` added, since your file hangs) on the chapter's input `[23, 12, 42, 4, 9, 30, 5, 17]`, `n = 8`, gaps 4, 2, 1:

**Gap 4** (compare elements 4 apart: pairs (0,4), (1,5), (2,6), (3,7))

| i | key | Moves | Placed at | Array after |
|---|---|---|---|---|
| 4 | 9 | 23 > 9, shift | 0 | `[9, 12, 42, 4, 23, 30, 5, 17]` |
| 5 | 30 | 12 > 30? no | 5 | same |
| 6 | 5 | 42 > 5, shift | 2 | `[9, 12, 5, 4, 23, 30, 42, 17]` |
| 7 | 17 | 4 > 17? no | 7 | same |

**Gap 2**

| i | key | Moves | Placed at | Array after |
|---|---|---|---|---|
| 2 | 5 | 9 > 5, shift | 0 | `[5, 12, 9, 4, 23, 30, 42, 17]` |
| 3 | 4 | 12 > 4, shift | 1 | `[5, 4, 9, 12, 23, 30, 42, 17]` |
| 4 | 23 | 9 > 23? no | 4 | same |
| 5 | 30 | 12 > 30? no | 5 | same |
| 6 | 42 | 23 > 42? no | 6 | same |
| 7 | 17 | 30 > 17, shift | 5 | `[5, 4, 9, 12, 23, 17, 42, 30]` |

**Gap 1** (ordinary insertion sort on a nearly sorted array)

| i | key | Moves | Placed at | Array after |
|---|---|---|---|---|
| 1 | 4 | 5 > 4, shift | 0 | `[4, 5, 9, 12, 23, 17, 42, 30]` |
| 2-4 | 9, 12, 23 | none | unchanged | same |
| 5 | 17 | 23 > 17, shift; 12 > 17? no | 4 | `[4, 5, 9, 12, 17, 23, 42, 30]` |
| 6 | 42 | none | 6 | same |
| 7 | 30 | 42 > 30, shift; 23 > 30? no | 6 | `[4, 5, 9, 12, 17, 23, 30, 42]` |

Result `[4, 5, 9, 12, 17, 23, 30, 42]`. Notice how little the gap-1 pass had to do: only 3 small shifts.

### What your current code does on `[2, 1]`

`gap = 1`, `i = 1`, `key = 1`, `j = 1`: shift makes the array `[2, 2]`, `j` does not change, the condition is still true, and the loop never ends (see the bug note above).

## Complexity

| Gap sequence | Worst case | Average case | Best case |
|---|---|---|---|
| Shell's (n/2) - what the code uses | Θ(n^2) | about n^(3/2) empirically | O(n log n) |
| Hibbard (2^k - 1) | Θ(n^(3/2)) | about n^(5/4) | O(n log n) |
| Knuth ((3^k - 1) / 2) | O(n^(3/2)) | about n^(7/6) empirically | O(n log n) |
| Sedgewick | O(n^(4/3)) | about n^(7/6) empirically | O(n log n) |

| Property | Value |
|---|---|
| Space | O(1) |
| In place | Yes |
| Stable | No |
| Adaptive | Yes, mostly (sorted input: one compare per element per gap, O(n log n) total) |
| Recursive | No |

**Comparison:** insertion sort O(n^2) / stable / best O(n); shell sort better than O(n^2) with a good gap sequence / not stable; merge sort O(n log n) / stable / O(n) space; quick sort O(n log n) average / not stable / O(log n) stack.

## When to Use / Not Use

Good for: medium-sized arrays (hundreds to low thousands), embedded and constrained systems (no recursion, O(1) memory), nearly sorted data, and when insertion sort is too slow but merge/quick sort feels like overkill. Historically used in places like the uClibc `qsort`. Not ideal for: very large datasets, when stability is required, when a hard worst-case bound is needed, and linked lists (needs random access to elements `gap` apart).

## Real-World Use Case

Shell sort's niche is small, memory-starved systems: embedded firmware and microcontrollers where recursion risks stack overflow and extra memory is unavailable, and older C libraries such as uClibc, whose `qsort` used it because memory was scarce and simplicity mattered. It is also the standard stepping stone for understanding why insertion sort's weakness (long-distance moves) can be fixed, an idea that reappears in comb sort and in tuning hybrid sorts.

## Tests (planned)

To add once the bug above is settled (`test_ch1.py`): empty list, single element, two elements (sorted and swapped), already sorted, reverse sorted, all equal, duplicates, negatives, the chapter example `[23, 12, 42, 4, 9, 30, 5, 17]`, odd and even lengths, plus a comparison against `sorted()` on random arrays. Tests that hang will be run with a timeout. Written with correct expected values, so they fail (time out) until the bug is fixed. Say "chkup" when ready.
