# Linear Search for a Target

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/linear-search
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer array nums and an integer target, return the index of the first occurrence of target in nums, or -1 if target is not present.

The array is not assumed to be sorted, and it may contain duplicate values. When the target appears more than once, return the smallest index where it occurs.

**Example 1**
```
Input:  nums = [5, 3, 8, 1], target = 8
Output: 2
```

**Example 2**
```
Input:  nums = [4, 2, 7, 9], target = 6
Output: -1
```

**Constraints**
```
0 <= nums.length <= 10^4
-10^9 <= nums[i], target <= 10^9
The array may be empty, unsorted, and may contain duplicates.
```

## How to Solve It — Thought Process

The first thing worth noticing is what's *not* given here: no guarantee that `nums` is sorted. That single fact rules out any approach that tries to be clever about where to look next — techniques like binary search rely entirely on ordering to decide whether the target is more likely to the left or right of some midpoint, and none of that reasoning is available on an array whose elements could be in any arrangement. Without an ordering guarantee, the only sound strategy is to treat every position as a candidate until it's actually been checked, which means the search has to examine elements one at a time, in some order, until it finds a match or runs out of places to look.

Given that a full scan is unavoidable, the natural order to scan in is left to right, and that choice isn't arbitrary — it's what makes "return the first occurrence" fall out for free. If the target appears at multiple indices, scanning from the start and stopping at the very first match is guaranteed to land on the smallest matching index, simply because smaller indices are visited before larger ones. There's no need for any special bookkeeping to track "is this the earliest match so far" — returning immediately upon the first match *is* that logic, expressed as early termination rather than as an explicit comparison.

The other detail worth being deliberate about is the choice of `-1` as the "not found" signal. Since valid indices only ever range from `0` up to `len(nums) - 1`, any negative number is automatically distinguishable from a real index — `-1` specifically is the conventional choice (mirroring what many languages' built-in search functions return), but the important property is just that it can never collide with a legitimate result. That signal is only safe to return after the entire array has been scanned without a match; returning it early, before every position has had a chance to match, would incorrectly report "not found" for a target that does exist further along.

Since finding a target in an unordered collection requires checking candidates until one matches (or all have been ruled out), and each check is a single constant-time comparison, this single left-to-right pass is already the best possible approach in the worst case — there's no way to guarantee finding (or ruling out) a target in unsorted data without the possibility of examining every element. What's worth knowing beyond the hand-written loop is that Python offers a built-in way to express the same "find the first matching position" idea: `list.index()` performs the same linear search internally, raising a `ValueError` if the target isn't found rather than returning a sentinel — so using it here means catching that exception and translating it into `-1` to match this problem's expected return convention.

## Solution — Linear Scan (this is already optimal for unsorted data; there's no way to guarantee finding or ruling out a target without potentially examining every element)

```python
class Solution:
    def linear_search_scan(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

## Additional Solution — Built-in `list.index()`

```python
    def linear_search_builtin_index(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            return -1
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().linear_search_builtin_index(nums, target)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a one-liner restatement:** both perform the same O(n) left-to-right scan for the first match, but `list.index()` runs that scan inside CPython's C implementation rather than as interpreted Python bytecode, which is typically measurably faster in practice for the same asymptotic work. The tradeoff is the error-handling style: `list.index()` communicates "not found" via a raised exception rather than a sentinel value, so this approach needs a `try`/`except` to translate that into the `-1` this problem expects — a different idiom (exception-based signaling wrapped to match a sentinel-based contract) worth being comfortable with, not just a different way of writing the same comparison loop.

### Algorithm — Linear Scan
1. Loop `i` from `0` to the last index of `nums`.
2. If `nums[i] == target`, return `i` immediately.
3. If the loop completes without a match, return `-1`.

### Algorithm — Built-in `list.index()`
1. Call `nums.index(target)`, which performs the same left-to-right search internally and returns the first matching index.
2. If `target` isn't present, `list.index()` raises `ValueError`; catch it and return `-1` instead.

## Dry Run

### Linear Scan — `nums = [5, 3, 8, 1], target = 8`

| `i` | `nums[i]` | `nums[i] == target`? |
|---|---|---|
| 0 | 5 | No |
| 1 | 3 | No |
| 2 | 8 | Yes → return `2` immediately |

Return `2`. ✅ matches expected output. Note that index `3` (`nums[3] = 1`) is never examined, since the scan already found its answer.

### Built-in `list.index()` — `nums = [4, 2, 7, 9], target = 6`

`[4, 2, 7, 9].index(6)` scans the whole list, finds no match, and raises `ValueError`. The `except` clause catches it and returns `-1`. ✅ matches expected output.

**Duplicate-target case — `nums = [3, 7, 3, 7], target = 7`:** Linear Scan checks `i=0` (`3 != 7`), then `i=1` (`7 == 7`) → returns `1` immediately, without ever reaching the second `7` at index `3`. `[3, 7, 3, 7].index(7)` also returns `1` — both correctly report the *first* occurrence, not any later duplicate.

**Empty array case — `nums = [], target = 5`:** Linear Scan's `range(len([]))` is empty, so the loop body never runs and it falls through to `return -1`. `[].index(5)` raises `ValueError` immediately (nothing to scan), which the `except` clause converts to `-1`. Both correctly return `-1`.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Linear Scan | O(n) worst case | O(1) | Stops at the first match, so best case is O(1); worst case (target absent or at the end) examines every element. Already optimal for unsorted data. |
| Built-in `list.index()` | O(n) worst case | O(1) | Same asymptotic complexity as Linear Scan; the scan runs in CPython's C implementation instead of interpreted Python, which is typically faster in practice for the same work. |

## Real-World Use Case

Finding the position of a value in an unordered collection is one of the most fundamental operations in software, and the "no ordering guarantee, so scan until found" pattern shows up constantly:

- **Searching unindexed or unsorted data** — looking up a record in a list of log entries, a small in-memory list of recent items, or any collection that hasn't been sorted or indexed specifically for fast lookup.
- **Finding the first match under a custom condition** — this exact "scan left to right, return on first match" pattern generalizes directly to `find()`/`indexOf()`-style utility functions in virtually every standard library, and to filtering the first item matching a predicate.
- **Small-scale lookups where sorting isn't worth it** — for small or one-off searches, a linear scan is often simpler and just as fast in practice as building and maintaining a sorted structure or hash index purely to speed up a single lookup.
- **A building block for more complex algorithms** — many string-matching and pattern-search algorithms (naive substring search, for instance) are direct extensions of this same "check each position in order" idea.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | [5, 3, 8, 1], target=8 | 2 |
| `test_example_2_not_found` | [4, 2, 7, 9], target=6 | -1 |
| `test_empty_array` | [], target=5 | -1 |
| `test_duplicate_target_returns_first_occurrence` | [3, 7, 3, 7], target=7 | 1 |
| `test_target_at_first_index` | [9, 1, 2], target=9 | 0 |
| `test_target_at_last_index` | [1, 2, 3, 4, 5], target=5 | 4 |
| `test_large_array_near_length_constraint` | list(range(10000)), target=9999 | 9999 |

All 7 tests (14 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation.

Run with:
```bash
cd Arrays/linear_search
python3 -m unittest -v
```
