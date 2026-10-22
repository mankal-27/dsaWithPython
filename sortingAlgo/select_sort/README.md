# Selection Sort

**Topic:** Sorting Algorithms
**Difficulty:** Easy (concept chapter)
**Link:** https://algomaster.io/learn/dsa/selection-sort
**Files:** `ch1.py` (implementation)

> This is a concept chapter on algomaster.io, not a problem with a fixed input/output statement, so there is no "Problem Statement" with examples and constraints. The task is: **implement selection sort** so it sorts an array in ascending order, in place.

## What Is Selection Sort?

Selection sort splits the array into two regions: a **sorted region** on the left (elements already in their final positions) and an **unsorted region** on the right. On each pass it scans the unsorted region to find the smallest element, then swaps it with the first element of the unsorted region. That grows the sorted region by one and shrinks the unsorted region by one. After n-1 passes the array is sorted (the last element is automatically in place).

## How It Works

1. Start with index 0 as the current position `i`.
2. Scan from `i` to the end to find the index of the minimum element.
3. Swap that minimum with the element at `i`.
4. Move `i` one step right (the sorted region grows by one).
5. Repeat until `i` reaches the second-to-last element.

The inner loop only *finds* the minimum's index - it never swaps. The single swap happens after the inner loop finishes, so there is at most one swap per pass.

## How to Solve It - Thought Process

Where bubble sort pushes the largest value right through many neighbour swaps, selection sort asks a different question: "which element belongs in position `i`?" The answer is simply the smallest value in the unsorted part. So instead of fixing order gradually with lots of swaps, find the winner first (just remember its index while scanning), then move it into place with one swap.

That gives the loop shape directly: an outer loop over target positions `i = 0 .. n-2`, and an inner loop `j = i+1 .. n-1` that updates `min_index` whenever it sees something smaller than `arr[min_index]`. The outer loop stops at `n-2` because once n-1 elements are placed, the last one has nowhere else to be. The inner loop starts at `i+1` because `min_index` is initialised to `i` (the element at `i` is the first candidate).

Two details worth noticing. The comparison is strict `<`, so on ties the *first* minimum found is kept. And the guard `if min_index != i` skips a pointless self-swap when the minimum is already in place - harmless to remove, but it saves a write.

The trade-off versus bubble sort: selection sort always makes the same n(n-1)/2 comparisons regardless of input (no early exit, not adaptive), but it makes at most n-1 swaps instead of up to O(n^2). It wins when writes are expensive and loses when the input is nearly sorted.

## Brute Force Solution

There is no meaningfully simpler variant; selection sort is already the straightforward approach. For reference, here is the same idea written the "naive" way that swaps every pass without the guard (works identically, one extra no-op write when the minimum is already in place):

```python
def selection_sort_basic(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

## Optimized Solution - Skip the Redundant Swap (your `ch1.py`)

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the minimum in unsorted position
        min_index = i

        for j in range(i + 1, n):
            if(arr[j] < arr[min_index]):
                min_index = j

        #swap minimumu with first unsorted element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
```

Verified: matches `sorted()` on 3,000 random arrays (lengths 0-15, negatives and duplicates), and handles `[]` and `[1]` (the outer `range(n-1)` is empty). No bugs found. (Only nit: a typo in a comment, "minimumu" - harmless.)

## Dry Run

### `arr = [64, 25, 12, 22, 11]`

Each row is one comparison in the inner loop. `min_index` starts at `i`.

**Pass 1** (`i=0`, `min_index=0` -> 64)

| j | Compare | Action | `min_index` |
|---|---|---|---|
| 1 | 25 < 64 | new min | 1 |
| 2 | 12 < 25 | new min | 2 |
| 3 | 22 < 12? no | - | 2 |
| 4 | 11 < 12 | new min | 4 |

Swap `arr[0]` and `arr[4]` -> `[11, 25, 12, 22, 64]`. Sorted region: `[11]`.

**Pass 2** (`i=1`, `min_index=1` -> 25)

| j | Compare | Action | `min_index` |
|---|---|---|---|
| 2 | 12 < 25 | new min | 2 |
| 3 | 22 < 12? no | - | 2 |
| 4 | 64 < 12? no | - | 2 |

Swap `arr[1]` and `arr[2]` -> `[11, 12, 25, 22, 64]`. Sorted region: `[11, 12]`.

**Pass 3** (`i=2`, `min_index=2` -> 25)

| j | Compare | Action | `min_index` |
|---|---|---|---|
| 3 | 22 < 25 | new min | 3 |
| 4 | 64 < 22? no | - | 3 |

Swap `arr[2]` and `arr[3]` -> `[11, 12, 22, 25, 64]`. Sorted region: `[11, 12, 22]`.

**Pass 4** (`i=3`, `min_index=3` -> 25)

| j | Compare | Action | `min_index` |
|---|---|---|---|
| 4 | 64 < 25? no | - | 3 |

`min_index == i`, so the guard skips the swap. Result: `[11, 12, 22, 25, 64]`.

Totals: **10 comparisons, 3 swaps** (10 = 4+3+2+1 = n(n-1)/2). Bubble sort on the same input would make 8 swaps.

### Already sorted: `arr = [1, 2, 3, 4, 5]`

Every pass finds that `arr[i]` is already the minimum (no `<` comparison succeeds), so `min_index == i` and the swap is skipped each time. Result unchanged, but still **10 comparisons, 0 swaps** - there is no early exit, which is why selection sort is O(n^2) even in the best case.

### Why it is not stable: `[5a, 3, 5b, 1]`

Pass 1 finds the minimum `1` at index 3 and swaps it with index 0, giving `[1, 3, 5b, 5a]`. The two 5s have swapped relative order (5a was first, now 5b is). Confirmed by running the code on `[(5,'a'), (3,'x'), (5,'b'), (1,'y')]` keyed on the number: result `[(1,'y'), (3,'x'), (5,'b'), (5,'a')]`.

## Complexity

| Case | Time | Space | Notes |
|---|---|---|---|
| Best (already sorted) | O(n^2) | O(1) | Still scans the whole unsorted region every pass; no early termination. |
| Average | O(n^2) | O(1) | Always exactly n(n-1)/2 comparisons. |
| Worst | O(n^2) | O(1) | Same comparisons; only the swap count changes. |

| Property | Value |
|---|---|
| Swaps | At most n-1 (one per pass) - O(n) |
| In place | Yes |
| Stable | No (long-distance swap can leap an element over an equal one) |
| Adaptive | No (does not benefit from partially sorted input) |

**Bubble vs Selection:** bubble sort can do up to n-1 swaps *per pass* (O(n^2) total) but can finish early on sorted input and is stable; selection sort does exactly one swap per pass (O(n) total) but always does the full comparison count and is not stable.

## When to Use / Not Use

Good for: situations where swaps (writes) are expensive, tight memory (O(1) extra space), tiny arrays (n < ~20), and when predictable running time matters. Poor for: large datasets (10,000 elements is about 50 million comparisons), when stability is required (use insertion or merge sort), nearly sorted data (insertion sort is near O(n) there), and generally on random data where insertion sort does fewer comparisons.

## Real-World Use Case

Selection sort's low write count matters on storage with costly or limited writes, such as flash memory and EEPROM in embedded devices, where each write wears the medium; minimising writes while sorting a small table in place is exactly its strength. It also shows up in firmware with a few dozen entries (sorting a handful of sensor readings or a small priority table) where code size and O(1) memory beat raw speed. Its "find the minimum, then place it" idea is also the core of heap sort, where a heap replaces the linear scan.

## Tests (planned)

To add when you want them (`test_ch1.py`): empty list, single element, two elements (sorted and swapped), already sorted, reverse sorted, all equal, duplicates, negatives, a swap-count check (at most n-1 swaps), the stability counter-example above, plus a comparison against `sorted()` on random arrays. Say "chkup" and I'll write and verify them.
