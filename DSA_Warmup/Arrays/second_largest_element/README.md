# Second Largest Element

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/second-largest-element
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer array nums, return the second largest distinct value in the array.

If the array does not contain a second distinct value, return -1. For example, [5, 5, 4] returns 4, while [5, 5, 5] returns -1 because every element is the same.

**Example 1**
```
Input:  nums = [3, 9, 5]
Output: 5
```

**Example 2**
```
Input:  nums = [5, 5, 5]
Output: -1
```

**Constraints**
```
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
The second largest refers to the second largest distinct value. Duplicates of the maximum do not count.
```

## How to Solve It — Thought Process

The word "distinct" is doing all the work in this problem statement, and it's the detail most likely to get glossed over. Without it, "second largest" would just mean "the value at index 1 after sorting descending" — but with duplicates in the picture, that's not what's being asked. In `[5, 5, 4]`, sorting descending gives `[5, 5, 4]`, and the element at position 1 is another `5` — yet the expected answer is `4`. Repeated copies of the maximum are still just the maximum; none of them are eligible to be the *second* largest, because that title belongs to the next-largest *different* value. This immediately rules out any approach that treats the array as a plain sorted sequence without first collapsing duplicates or explicitly skipping ties with the maximum.

The second edge case worth naming up front is what happens when there simply isn't a second distinct value: an array where every element is the same (`[5, 5, 5]`), or an array with only one element (`[7]`). Neither has a legitimate "second largest" to report, so both must return `-1`. This means the solution needs some way to detect "I never found a qualifying second value" and distinguish that from "the second value happens to be very small (but still legitimate)."

That detection is where the sentinel choice matters. A natural instinct might be to start a tracking variable at `0` and update it as larger qualifying values are found — but that silently breaks the moment the real answer is negative: for `[-5, -2, -9]`, the second-largest distinct value is `-5`, and a tracker seeded at `0` would never get updated (since `-5 < 0`), incorrectly reporting `0` — a value that isn't even in the array — instead of `-5`. In a language with fixed-width integers, the standard fix is to seed the tracker with the smallest representable value (`Long.MIN_VALUE`, or similar) so that any real array value will be recognized as "found." Python doesn't need a numeric sentinel at all, though, since it can just use `None` and ask "is this still `None`?" — which sidesteps having to know or guess the smallest possible input value, and reads more directly as "nothing has been found yet" rather than relying on a magic number that happens to be smaller than anything else.

With the two pitfalls named — duplicates of the maximum don't count, and the "not found" state must be distinguishable from any real value including negative ones — the direct approach is to just find the maximum first, then make a second pass looking for the largest value that's strictly less than it. Two full scans is completely correct, but it does look at every element twice when the information needed to track *both* the largest and second-largest is available in a single sweep. The insight that collapses this into one pass: while scanning, every new value either beats the current largest (in which case the old largest demotes to second-largest, since it's still bigger than everything else seen so far except the new value), or it doesn't beat the largest but might still beat the current second-largest, or it ties the current largest exactly (in which case it's a duplicate of the max and gets ignored, keeping the "distinct" requirement intact), or it's too small to matter at all. Handling those cases as the array is walked once means both trackers land in their final, correct state after a single pass, without ever needing to know the maximum in advance.

## Brute Force Solution — Two Pass

```python
class Solution:
    def second_largest_two_pass(self, nums):
        if len(nums) < 2:
            return -1
        largest = nums[0]
        for x in nums:
            if x > largest:
                x = largest
        second = None
        for x in nums:
            if x < largest and (second is None or x > second):
                second = x
        return second if second is not None else -1
```

> ⚠️ **Known bug:** in the first pass, `if x > largest: x = largest` has the assignment backwards — it overwrites the loop variable `x` with `largest`'s current value, instead of updating `largest` with `x`. This means `largest` never actually changes from its initial `nums[0]`; the "find the maximum" pass silently does nothing.
>
> **Confirmed directly — `second_largest_two_pass([-5, -2, -9])` returns `-9` instead of the correct `-5`:** `largest` stays at `nums[0] = -5` throughout (the real maximum, `-2`, is never recorded). The second pass then looks for the largest value strictly less than `-5`: `-2` fails that check (`-2` is not less than `-5`), but `-9` passes (`-9 < -5`), so `second` becomes `-9` — the *smallest* value in the array, not the second-largest. On `[3, 9, 5]`, the same bug causes `largest` to stay at `3` for the whole run, so the second pass finds nothing strictly less than `3` and returns `-1` instead of `5`. The fix is changing `x = largest` to `largest = x`; flagging rather than silently correcting it.

## Optimized Solution — One Pass

```python
    def second_largest_one_pass(self, nums):
        largest = None
        second = None
        for x in nums:
            if largest is None or x > largest:
                second = largest
                largest = x
            elif x < largest and (second is None or x > second):
                second = x
            return second if second is not None else -1
```

> ⚠️ **Known bug:** `return second if second is not None else -1` is indented one level too deep — it sits inside the `for` loop body (aligned with the `if`/`elif`), so the method returns after processing only the very first element of `nums`, every time, regardless of array length.
>
> **Confirmed directly — `second_largest_one_pass([3, 9, 5])` returns `-1` instead of `5`:** on the very first iteration, `x = 3`, `largest` is `None` so it promotes (`second = None`, `largest = 3`) — and then the misplaced `return` fires immediately, returning `-1` because `second` is still `None`. The elements `9` and `5` are never even looked at. This happens on every call with more than one element; it only *looks* correct on inputs like `[5, 5, 5]` or `[7]`, where the true answer also happens to be `-1`, purely by coincidence. The fix is dedenting the `return` line so it runs once, after the loop finishes, not inside it; flagging rather than silently correcting it.

## Additional Solution — Sort Distinct Values

```python
    def second_largest_sort_distinct(self, nums):
        distinct_sorted = sorted(set(nums), reverse=True)
        return distinct_sorted[1] if len(distinct_sorted >= 2) else -1
```

> ⚠️ **Known bug:** `len(distinct_sorted >= 2)` applies `len()` to the *result* of `distinct_sorted >= 2` rather than comparing `len(distinct_sorted)` to `2`. Since `distinct_sorted` is a list and `2` is an int, Python doesn't support that comparison at all — `distinct_sorted >= 2` itself raises `TypeError: '>=' not supported between instances of 'list' and 'int'` before `len()` is ever called.
>
> **Confirmed directly:** calling `second_largest_sort_distinct` with any input at all (tested with `[3, 9, 5]`, and confirmed the same failure holds across every other test case) raises that `TypeError` immediately — this bug isn't input-dependent, it crashes unconditionally. The fix is `len(distinct_sorted) >= 2` (comparing the length to `2`), with the parentheses moved so `len()` wraps only `distinct_sorted`; flagging rather than silently correcting it.
>
> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().second_largest_one_pass(nums)`), not on the class directly.
>
> **Why sorting counts as a genuinely different approach (when working correctly):** rather than tracking running "largest so far" / "second largest so far" state by hand, this approach leans on two built-ins to do the distinct-value bookkeeping structurally — `set()` collapses duplicates away entirely (so there's no need to explicitly skip ties with the maximum), and `sorted(..., reverse=True)` puts the second-largest distinct value directly at index `1` if it exists. It trades the O(n) time and O(1) space of the tracking approaches for O(n log n) time and O(n) space (building the set and sorted list), in exchange for code that reads very close to the problem statement itself: "the second-largest *distinct* value" becomes, almost literally, `sorted(set(nums), reverse=True)[1]`.

### Algorithm — Two Pass (intended)
1. Scan once to find `largest`, the maximum value.
2. Initialize `second = None` (no qualifying value found yet).
3. Scan again: for each value strictly less than `largest`, if it's the first qualifying value found or greater than the current `second`, update `second`.
4. If `second` is still `None`, no value was below the maximum, so return `-1`. Otherwise return `second`.

*(See the bug callout above — step 1 never actually updates `largest`.)*

### Algorithm — One Pass (intended)
1. Initialize `largest = None` and `second = None`.
2. For each value `x`: if `largest` is unset or `x > largest`, the old `largest` demotes to `second` and `x` becomes the new `largest`.
3. Otherwise, if `x` is strictly less than `largest` and (no `second` yet, or `x > second`), update `second`.
4. A value equal to `largest` falls into neither branch and is skipped, keeping duplicates of the maximum out of `second`.
5. If `second` is still `None` after the scan, return `-1`. Otherwise return `second`.

*(See the bug callout above — the return statement fires after the first element, so steps 2-5 never run past one iteration.)*

### Algorithm — Sort Distinct Values (intended)
1. Collapse `nums` into its distinct values with `set(nums)`.
2. Sort those distinct values in descending order.
3. If there are at least two distinct values, return the one at index `1`; otherwise return `-1`.

*(See the bug callout above — step 3 crashes before this can complete, on every call.)*

## Dry Run

The bug callouts above already trace all three implementations against real inputs, since the interesting behavior here *is* the bugs. For reference, here's what correct execution looks like conceptually, using the intended algorithms:

### Two Pass (intended) — `nums = [5, 5, 4]`

| Pass | Step | State |
|---|---|---|
| 1 | scan for max | `largest = 5` |
| 2 | `x=5`: `5 < 5`? No, skip | `second = None` |
| 2 | `x=5`: `5 < 5`? No, skip | `second = None` |
| 2 | `x=4`: `4 < 5`? Yes, `second is None` → update | `second = 4` |

Intended return: `4`.

### One Pass (intended) — `nums = [3, 9, 5]`

| `x` | Comparison | `largest` after | `second` after |
|---|---|---|---|
| — | initial | `None` | `None` |
| 3 | `largest is None` → promote | `3` | `None` |
| 9 | `9 > 3` → promote, old largest demotes | `9` | `3` |
| 5 | `5 < 9` and (`second=3`, `5 > 3`) → update second | `9` | `5` |

Intended return: `5` (as implemented, the misplaced `return` fires after the very first row and returns `-1` — see the bug callout above).

### Sort Distinct Values (intended) — `nums = [5, 5, 5]`

`set([5, 5, 5])` → `{5}`. `sorted({5}, reverse=True)` → `[5]`. Length is `1`, which is less than `2`, so the intended result is `-1`. As implemented, this never gets computed — the method crashes on the line before it, on every call (see the bug callout above).

**All-negative case — `nums = [-5, -2, -9]` (this is exactly why the sentinel/`None` design matters):** the intended One Pass trace: `x=-5`: `largest is None` → promote, `largest = -5`. `x=-2`: `-2 > -5` → promote, `second = -5`, `largest = -2`. `x=-9`: `-9 < -2` and (`second=-5`, `-9 > -5` is `False`) → no update. Intended final: `second = -5`, correctly — a `0`-seeded tracker would have wrongly stayed at `0` the entire time. As implemented, both `second_largest_two_pass` and `second_largest_one_pass` get this wrong for their own separate reasons (see the bug callouts above): confirmed directly, `second_largest_two_pass([-5, -2, -9])` returns `-9`, and `second_largest_one_pass([-5, -2, -9])` returns `-1`.

## Complexity

| Approach | Time Complexity (intended) | Actual Behavior | Space Complexity | Notes |
|---|---|---|---|---|
| Two Pass | O(n) | Runs, but returns wrong results for many inputs (see bug callout) | O(1) | The first pass never actually updates `largest`, so it stays at `nums[0]`. |
| One Pass | O(n) | Runs, but always returns after inspecting only the first element (see bug callout) | O(1) | The misplaced `return` inside the loop prevents any real tracking from happening. |
| Sort Distinct Values | O(n log n) | Crashes with `TypeError` on every call (see bug callout) | O(n) | An invalid comparison (`list >= int`) is evaluated before `len()` is ever reached. |

## Real-World Use Case

Tracking the top few distinct values in a stream or dataset — not just the single maximum — shows up in several recognizable places:

- **Leaderboards and rankings** — displaying 1st and 2nd place (or a top-k list) requires exactly this kind of running-tracker logic, especially when ties at the top shouldn't collapse the ranking.
- **Bidding and auction systems** — a second-price auction (like those used in ad exchanges) charges the winner the *second*-highest bid, not the highest, which is a direct real-world application of this exact computation.
- **Anomaly and outlier detection** — comparing the largest and second-largest values in a window of sensor readings or metrics can reveal whether a spike is an isolated outlier or part of a broader trend.
- **A building block for order-statistics problems** — finding the k-th largest distinct element generalizes this same tracking idea, and interview-style problems often build on the single-pass largest/second-largest pattern shown here.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports which specific method fails. Expected values are the mathematically correct ones per the problem statement, not adjusted to match any of the three bugs.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | [3, 9, 5] | 5 |
| `test_example_2_all_same` | [5, 5, 5] | -1 |
| `test_single_element` | [7] | -1 |
| `test_duplicate_maximum_valid_second` | [5, 5, 4] | 4 |
| `test_all_negative` | [-5, -2, -9] | -5 |
| `test_large_array_near_length_constraint` | range(99999) + [99998] (10^5 elements) | 99997 |

**Current result against the real `sol.py`: of 18 sub-assertions (6 tests × 3 methods), 5 pass and 13 fail or error.** `second_largest_sort_distinct` errors (crashes) on every single test, unconditionally. `second_largest_two_pass` and `second_largest_one_pass` each pass a few tests where the buggy behavior coincidentally matches the correct answer (e.g. `[5, 5, 5]` and `[7]` both correctly return `-1` even though the code arrives there for the wrong reasons), but fail on every test that would actually exercise their intended logic. Confirmed identically both in this container and re-run directly on-device.

Run with:
```bash
cd Arrays/second_largest_element
python3 -m unittest -v
```
