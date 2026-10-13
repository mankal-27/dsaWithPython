# Largest Element in an Array

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/largest-element-in-array
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a non-empty integer array nums, return the largest element in the array.

The array can contain negative numbers, and the maximum value may appear more than once. In either case, return that maximum value.

**Example 1**
```
Input:  nums = [3, 9, 5]
Output: 9
```

**Example 2**
```
Input:  nums = [-5, -2, -9]
Output: -2
```

**Constraints**
```
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
The array is non-empty, and the maximum value may appear more than once.
```

## How to Solve It — Thought Process

Finding the largest value in a collection has the same unavoidable-work property as summing one: there's no way to be certain some unseen element isn't bigger than whatever's currently believed to be the maximum without actually looking at it, so every element has to be examined at least once. The mechanics of "keep a running best-so-far and update it when something beats it" are about as simple as an algorithm gets — the interesting part of this problem isn't the comparison logic, it's getting the *starting point* of that comparison right.

The tempting shortcut is to seed the running maximum at `0` and then scan for anything bigger. That works fine as long as the array actually contains a positive number, but it silently breaks the moment every element is negative: for `[-5, -2, -9]`, a running maximum that starts at `0` would never find anything in the array bigger than `0`, and the function would incorrectly report `0` as the answer — a value that isn't even present in the input. The fix is to never assume anything about the sign of the data; instead, seed the running maximum with an actual element of the array, most naturally `nums[0]`, the first one. Because the array is guaranteed non-empty by the constraints, `nums[0]` always exists, so this is safe without any extra empty-check. Seeding with the first element also means the scan itself only needs to walk from index `1` onward — index `0` has already been accounted for as the starting value, so re-comparing it against itself would be redundant.

The other detail worth being deliberate about is the comparison operator used to update the running maximum: strictly greater-than (`>`), not greater-than-or-equal (`>=`). Since the maximum value is allowed to repeat, using `>` means that when a later element ties the current maximum, the running maximum simply stays as it is — which is correct, since the value is identical either way. Using `>=` would also produce a correct final answer here (a tie just gets replaced with an equal value), but `>` more directly expresses the intent of "only update when something is strictly better," and avoids doing pointless reassignment work on ties.

Since every element must be inspected at least once and each inspection is a single constant-time comparison, this single pass is already the best possible approach — there's no way to find the maximum of `n` numbers without looking at all `n` of them, so there's no further algorithmic optimization to make. What's still worth knowing is that Python offers a built-in way to express the exact same idea: `max()` performs the identical linear scan internally, but inside CPython's C implementation rather than as an interpreted Python loop, which is typically faster in practice for the same O(n) work — the same tradeoff seen with `sum()` on the array-sum problem.

## Solution — Linear Scan (this is already optimal; there's no faster approach, since every element must be inspected at least once)

```python
class Solution:
    def largest_element_linear_scan(self, nums):
        largest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest
```

## Additional Solution — Built-in `max()`

```python
    def largest_element_builtin_max(self, nums):
        return max(nums)
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().largest_element_builtin_max(nums)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a one-liner restatement:** both perform the same O(n) scan-and-compare, but `max()` runs its loop inside CPython's C implementation rather than as interpreted Python bytecode, which is typically measurably faster in practice for the same asymptotic work — the same reason a built-in reduction is generally preferred over a hand-written loop in idiomatic Python when no custom per-element logic is needed.

### Algorithm — Linear Scan
1. Set `largest = nums[0]` (safe because the array is guaranteed non-empty).
2. Loop `i` from `1` to the end of the array.
3. For each `nums[i]`, if `nums[i] > largest`, update `largest = nums[i]`.
4. Return `largest`.

### Algorithm — Built-in `max()`
1. Call Python's built-in `max(nums)`, which performs the same scan-and-compare internally.
2. Return its result directly.

## Dry Run

### Linear Scan — `nums = [-5, -2, -9]`

| `i` | `nums[i]` | `nums[i] > largest`? | `largest` after |
|---|---|---|---|
| — | — | — | -5 (seeded from `nums[0]`) |
| 1 | -2 | Yes (-2 > -5) | -2 |
| 2 | -9 | No (-9 < -2) | -2 |

Return `-2`. ✅ matches expected output. Note how seeding with `nums[0] = -5` instead of `0` is what makes an all-negative array return a value that's actually in the array.

### Built-in `max()` — `nums = [3, 9, 5]`

`max([3, 9, 5])` performs the equivalent scan internally (starts from `3`, sees `9 > 3` → updates to `9`, sees `5 < 9` → no change) and returns `9` directly. ✅ matches expected output.

**Duplicate-maximum case — `nums = [4, 7, 7, 2]`:** Linear Scan seeds `largest = 4`, sees `7 > 4` → updates to `7`, sees the second `7`: `7 > 7` is `False`, so `largest` stays `7` (correctly, since the value is identical either way). `max([4, 7, 7, 2])` also returns `7`. Both handle the repeated maximum correctly.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Linear Scan | O(n) | O(1) | Visits every element exactly once; only the running maximum is stored. Already optimal — no algorithm can find the max of n numbers without examining all n. |
| Built-in `max()` | O(n) | O(1) | Same asymptotic complexity as Linear Scan; the scan runs in CPython's C implementation instead of interpreted Python, which is typically faster in practice for the same work. |

## Real-World Use Case

Finding the largest value in a collection is a building block that shows up constantly, often as a step inside something larger:

- **Leaderboards and rankings** — finding the top score, highest bid, or best result in a dataset is directly this problem, often repeated as data streams in.
- **Resource allocation and limits** — identifying the peak memory usage, maximum request latency, or highest load in a monitoring window drives alerting thresholds and capacity planning decisions.
- **A building block for other array algorithms** — finding the range (max − min), detecting outliers, or normalizing data (scaling values relative to the maximum) all start from being able to correctly and efficiently find the largest element.
- **UI and data visualization** — determining the upper bound of a chart's axis, or the tallest bar in a bar chart, typically requires scanning the underlying dataset for its maximum value first.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | [3, 9, 5] | 9 |
| `test_example_2_all_negative` | [-5, -2, -9] | -2 (exercises seeding with `nums[0]`, not `0`) |
| `test_single_element` | [42] | 42 |
| `test_duplicate_maximum` | [4, 7, 7, 2] | 7 |
| `test_32bit_boundary_values` | [-2147483648, 0, 2147483647] | 2147483647 |
| `test_large_array_near_length_constraint` | list(range(10000)) | 9999 |

All 6 tests (12 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation.

Run with:
```bash
cd Arrays/largest_element_in_array
python3 -m unittest -v
```
