# Merge Sort

**Topic:** Sorting Algorithms
**Difficulty:** Medium (concept chapter)
**Link:** https://algomaster.io/learn/dsa/merge-sort
**Files:** `ch1.py` (implementation)

> This is a concept chapter on algomaster.io, not a problem with a fixed input/output statement, so there is no "Problem Statement" with examples and constraints. The task is: **implement merge sort** so it sorts an array in ascending order (in place, using temporary arrays during the merge).

## What Is Merge Sort?

Merge sort is a divide-and-conquer algorithm:

1. **Divide** the array into two halves.
2. **Conquer** each half by sorting it recursively.
3. **Combine** the two sorted halves by merging them into one sorted range.

The recursion bottoms out at subarrays of 0 or 1 elements, which are already sorted. All the real work happens in the merge step.

## How It Works

**Recursive driver** - `merge_sort(arr, left, right)`:

1. If `left >= right`, return (base case).
2. `mid = left + (right - left) // 2`.
3. Sort the left half `[left, mid]`, then the right half `[mid+1, right]`.
4. `merge(arr, left, mid, right)`.

**Merge** - combine two sorted ranges with two pointers:

1. Copy the left half and the right half into temporary arrays.
2. Keep a pointer `i` in the left copy, `j` in the right copy, and `k` as the write position in `arr`.
3. Repeatedly copy the smaller front element into `arr[k]` and advance that pointer and `k`.
4. When one side runs out, copy whatever remains of the other side.

## How to Solve It - Thought Process

Sorting a whole array is hard, but merging two already-sorted arrays is easy: you only ever look at the front of each, take the smaller, and move on. That is a single left-to-right sweep, O(n). So the trick is to arrange for the merge to always have sorted inputs, and recursion does exactly that: split until pieces are size 1 (trivially sorted), then merge upward.

Why O(n log n) every time: halving always takes about log2(n) levels, and every level merges every element exactly once (O(n) per level). Input order never changes the shape of the recursion, so best, average and worst are all the same.

The details that matter in code:

- **Midpoint:** `left + (right - left) // 2` avoids integer overflow in languages with fixed-size ints (harmless in Python, but the idiom matches the chapter's Java).
- **Temporary copies:** the merge overwrites `arr[left..right]`, so the two halves must be copied out first. That is where the O(n) extra space comes from.
- **`<=` not `<`:** when the two front elements are equal, take the LEFT one first. The left half came earlier in the input, so this preserves original order of equals - that is what makes merge sort **stable**.
- **Draining the leftovers:** after the main loop one side may still have elements. They are already sorted and all >= everything written so far, so they are copied straight over. Each drain loop must advance BOTH its own read pointer and the write position `k`.

## Brute Force Solution

There is no simpler comparison-sort variant of the same idea to show here (bubble/selection/insertion sort from earlier chapters are the simple O(n^2) baseline). A compact "return a new list" version of merge sort, for comparison, looks like this:

```python
def merge_sort_simple(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_simple(arr[:mid])
    right = merge_sort_simple(arr[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

## Optimized Solution - In-Place Index-Based Version (your `ch1.py`)

```python
def merge_sort(arr, left, right):
    if(left >= right):
        return

    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1: right + 1]

    i = 0
    j = 0
    k = left

    while i <len(left_arr) and j < len(right_arr):
        if(left_arr[i]) <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        j += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
```

Call it as `merge_sort(arr, 0, len(arr) - 1)`. It sorts `arr` in place and returns `None` (same as the chapter's Java `void`).

> ⚠️ **Known bug (in the left-leftover loop of `merge`):** the third loop
>
> ```python
> while i < len(left_arr):
>     arr[k] = left_arr[i]
>     i += 1
>     j += 1      # <-- should be k += 1
> ```
>
> advances `j` (the right-half pointer, which is no longer used at this point) instead of `k` (the write position in `arr`). So when TWO OR MORE elements remain in the left half after the right half is exhausted, every one of them is written to the same slot `arr[k]`, each overwriting the last, and the later slots keep stale values. With exactly one leftover element it happens to write to the correct final slot, which is why small cases and the chapter's example look fine.
>
> **Confirmed by running the code:**
>
> | Input | Your result | Expected |
> |---|---|---|
> | `[38, 27, 43, 3, 9, 82, 10]` | `[3, 9, 10, 27, 38, 43, 82]` | same (passes - at most one left-over each time) |
> | `[2, 1]` | `[1, 2]` | same (passes) |
> | `[3, 2, 1]` | `[1, 3, 1]` | `[1, 2, 3]` - **wrong** |
> | `[5, 4, 3, 2, 1]` | `[1, 2, 3, 1, 2]` | `[1, 2, 3, 4, 5]` - **wrong** |
>
> Across 500 random arrays (length 0-12, values 0-9) it returned the wrong answer on **207**. Not just a crash risk: it silently returns wrong data, and elements are lost and duplicated (the output for `[3, 2, 1]` contains two 1s and no 2).
>
> Trace of `[3, 2, 1]`: `merge [3,2] -> [2,3]` is fine. Then `merge([2,3] , [1])`: the right side's `1` is smaller than `2`, so it is taken first (`arr[0] = 1`, `k = 1`), and the right half is now exhausted. The left-leftover loop then writes `2` to `arr[1]`, and since `k` doesn't advance, writes `3` to `arr[1]` as well. `arr[2]` is never written and keeps its old value `1`: result `[1, 3, 1]`.
>
> The right-leftover loop below it is correct (it does `k += 1`) - compare the two loops. This README documents the bug rather than fixing it; the one-line change is `j += 1` -> `k += 1`, say the word if you want it applied.

## Dry Run

### Divide and merge on `[38, 27, 43, 3, 9, 82, 10]` (your code, correct on this input)

Divide (right-inclusive, `mid = left + (right - left) // 2`, so size 7 splits 4 + 3):

```
Level 0:  [38, 27, 43, 3, 9, 82, 10]
                /                  \
Level 1:  [38, 27, 43, 3]      [9, 82, 10]
           /         \           /       \
Level 2:  [38, 27]  [43, 3]   [9, 82]   [10]
           /    \    /    \    /    \
Level 3: [38] [27] [43] [3] [9]  [82]
```

Merges, in the order your code performs them (traced by running it):

| Merge range (`left, mid, right`) | Before | After |
|---|---|---|
| `0, 0, 1` | `[38, 27]` | `[27, 38]` |
| `2, 2, 3` | `[43, 3]` | `[3, 43]` |
| `0, 1, 3` | `[27, 38, 3, 43]` | `[3, 27, 38, 43]` |
| `4, 4, 5` | `[9, 82]` | `[9, 82]` |
| `4, 5, 6` | `[9, 82, 10]` | `[9, 10, 82]` |
| `0, 3, 6` | `[3, 27, 38, 43, 9, 10, 82]` | `[3, 9, 10, 27, 38, 43, 82]` |

Final merge in detail (`left_arr = [3, 27, 38, 43]`, `right_arr = [9, 10, 82]`):

| i | j | k | Compare | Take |
|---|---|---|---|---|
| 0 | 0 | 0 | 3 <= 9 | 3 (left) |
| 1 | 0 | 1 | 27 <= 9? no | 9 (right) |
| 1 | 1 | 2 | 27 <= 10? no | 10 (right) |
| 1 | 2 | 3 | 27 <= 82 | 27 (left) |
| 2 | 2 | 4 | 38 <= 82 | 38 (left) |
| 3 | 2 | 5 | 43 <= 82 | 43 (left) |
| 4 | 2 | 6 | left exhausted | drain right: 82 |

Result `[3, 9, 10, 27, 38, 43, 82]`. Here the left side finished first, so the (buggy) left-drain loop never ran with 2+ elements.

### Where the bug bites: `[3, 2, 1]`

| Step | Range | Before | After |
|---|---|---|---|
| merge `0, 0, 1` | `[3, 2]` | `[3, 2, 1]` | `[2, 3, 1]` |
| merge `0, 1, 2` | `left_arr=[2,3]`, `right_arr=[1]` | `[2, 3, 1]` | `[1, 3, 1]` - wrong |

In the second merge: `1 < 2` so `arr[0] = 1`, `j` becomes 1 (right exhausted), `k = 1`. Left-drain loop: `arr[1] = 2` (`j` -> 2, `k` stays 1), then `arr[1] = 3` (`k` still 1). `arr[2]` is untouched.

## Complexity

| Case | Time | Space | Notes |
|---|---|---|---|
| Best | O(n log n) | O(n) | Split/merge structure is input-independent. |
| Average | O(n log n) | O(n) | Same. |
| Worst | O(n log n) | O(n) | Same - no degradation on adversarial input (unlike quick sort). |

| Property | Value |
|---|---|
| Space | O(n) for the temporary arrays (+ O(log n) call stack) |
| Stable | Yes (`<=` takes the left element first on ties) |
| In place | No (needs the temp copies) |
| Adaptive | No (same work on sorted input) |

**Comparison:** merge sort guarantees O(n log n) and is stable but uses O(n) memory; quick sort is O(1)-ish extra space and cache-friendlier but O(n^2) worst case and not stable; heap sort is O(n log n) and in place but not stable and cache-unfriendly.

## When to Use / Not Use

Good for: guaranteed O(n log n) (real-time systems, untrusted input), sorting linked lists (merge can re-link nodes in O(1) extra space), external sorting of data larger than memory, cases needing stability, and parallel sorting (the two halves are independent). Not ideal for: memory-tight environments, small arrays (insertion sort wins below roughly 20-30 elements, which is why optimized versions switch to it), and nearly sorted data (Timsort/insertion sort exploit existing order; merge sort doesn't).

## Real-World Use Case

Merge sort is the backbone of external sorting in databases and big-data systems: sort chunks that fit in RAM, write them out, then do a multi-way merge, which is how terabyte-scale sorts and `ORDER BY` on huge tables work. Python's `list.sort()` and `sorted()` (Timsort) and Java's object sort are merge-sort hybrids chosen specifically for stability and the O(n log n) guarantee. The same merge-two-sorted-sequences primitive underlies merging sorted runs in log-structured storage and MapReduce-style shuffle/sort phases.

## Tests (planned)

To add once the bug above is settled (`test_ch1.py`): empty list, single element, two elements, already sorted, reverse sorted (`[3, 2, 1]` and `[5, 4, 3, 2, 1]` expose the bug), all equal, duplicates, negatives, odd and even lengths, a stability check using (key, tag) records, plus a comparison against `sorted()` on random arrays. Tests will be written with the correct expected values, so they fail until the bug is fixed. Say "chkup" when ready.
