# Sum of All Elements

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/sum-of-array-elements
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer array nums, return the sum of all its elements.

If the array is empty, return 0.

**Example 1**
```
Input:  nums = [3, 9, 5]
Output: 17
```

**Example 2**
```
Input:  nums = [-3, 10, -7, 4]
Output: 4
```

**Constraints**
```
0 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
The array may be empty.
```

## How to Solve It — Thought Process

"Sum everything in this array" is about as direct a problem statement as they come — there's no clever trick to discover, because touching every element at least once is unavoidable: no algorithm can know the total without having looked at each value that contributes to it. So the real question here isn't "how do I avoid work," it's "what needs to be gotten right while doing the unavoidable work."

The first thing to get right is the starting state. A running total that starts at `0` handles the empty-array case for free — if `nums` has nothing in it, the loop body never runs, and the total that was never touched is still `0`, which is exactly the expected answer. No special `if not nums: return 0` branch is needed; it falls out of the initial value being correct.

The second thing — and this is where a language like Java or C++ would need real care — is the width of the accumulator. Each individual element is bounded to fit in a 32-bit signed integer (`-2^31` to `2^31 - 1`), but the *sum* of up to `10^5` such elements is a different story: stack `100,000` values near `2^31 - 1` and the total reaches roughly `2 * 10^14`, which overflows a 32-bit accumulator by a wide margin (32-bit signed integers top out around `2.1 * 10^9`). In a fixed-width-integer language, this means deliberately choosing a wider accumulator type (`long`, `int64`, etc.) for the running total, even though every individual array element would fit in the narrower type. Python sidesteps this specific danger structurally — its integers grow arbitrarily large automatically, so there's no separate "wide accumulator" type to opt into, and no overflow to guard against no matter how large the sum gets. It's still worth naming, though, both because it's the kind of constraint that would silently break this same code in most other languages, and because a running total in Python is exactly the same accumulator concept, just without the width ceiling.

With those two things settled, the implementation is a single pass: walk through the array once, adding each element to the running total, and return the total once every element has been visited. Since every element must be examined at least once and each examination is constant-time work, this is already the best possible approach — there's no faster way to sum `n` numbers than to look at all `n` of them. Beyond the direct loop, Python does offer a different way to express the same idea: its built-in `sum()` function performs the identical accumulation, but the iteration happens inside CPython's C implementation rather than in an interpreted Python loop, which is typically faster in practice for the same O(n) work. That's a genuinely different way of expressing the solution — reaching for a language-provided reduction instead of hand-rolling the loop — even though both do fundamentally the same thing.

## Solution — Linear Scan (this is already optimal; there's no faster approach, since every element must be visited at least once)

```python
class Solution:
    def sum_of_array_elements_linear_scan(self, nums):
        total = 0
        for num in nums:
            total += num
        return total
```

## Additional Solution — Built-in `sum()`

```python
    def sum_of_array_elements_builtin_sum(self, nums):
        return sum(nums)
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().sum_of_array_elements_builtin_sum(nums)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a one-liner restatement:** both do the same O(n) accumulation, but `sum()` runs its loop inside CPython's C implementation rather than as interpreted Python bytecode, which is typically measurably faster in practice for the same asymptotic work — the same reason built-in reductions are generally preferred over hand-written loops in idiomatic Python when no custom per-element logic is needed.

### Algorithm — Linear Scan
1. Initialize `total = 0`.
2. Loop over each `num` in `nums`, adding it to `total`.
3. Return `total` (an empty `nums` never enters the loop, so `total` stays `0`).

### Algorithm — Built-in `sum()`
1. Call Python's built-in `sum(nums)`, which performs the same accumulation internally.
2. Return its result directly.

## Dry Run

### Linear Scan — `nums = [-3, 10, -7, 4]`

| Step | `num` | `total` after |
|---|---|---|
| — | — | 0 (initial) |
| 1 | -3 | -3 |
| 2 | 10 | 7 |
| 3 | -7 | 0 |
| 4 | 4 | 4 |

Return `4`. ✅ matches expected output.

### Built-in `sum()` — `nums = [3, 9, 5]`

`sum([3, 9, 5])` performs the equivalent accumulation internally (`0 + 3 = 3`, `3 + 9 = 12`, `12 + 5 = 17`) and returns `17` directly. ✅ matches expected output.

**Empty array — `nums = []`:** Linear Scan's loop body never executes, so `total` stays at its initial `0`. `sum([])` returns `0` by definition (its own default starting value). Both return `0`. ✅ matches the stated behavior for an empty array.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Linear Scan | O(n) | O(1) | Visits every element exactly once; only the running total is stored. Already optimal — no algorithm can sum n numbers without examining all n. |
| Built-in `sum()` | O(n) | O(1) | Same asymptotic complexity as Linear Scan; the accumulation loop runs in CPython's C implementation instead of interpreted Python, which is typically faster in practice for the same work. |

Python's arbitrary-precision integers mean neither approach needs a separate wide-accumulator type the way a fixed-width-integer language would, despite the sum potentially reaching roughly `2 * 10^14` at the stated constraints.

## Real-World Use Case

Summing a collection of values is one of the most common building blocks in software, showing up well beyond a standalone "add these numbers" feature:

- **Aggregation queries** — computing totals (revenue, item counts, transaction amounts) over a dataset is the same accumulate-while-scanning pattern, whether done in application code or as the `SUM()` aggregate in SQL.
- **Running statistics** — sums are the first building block toward derived metrics like averages, variance, and moving totals, all of which extend the same single-pass accumulation idea.
- **Financial and analytics dashboards** — totals across line items, daily totals across transactions, or aggregate counters in metrics pipelines all reduce to summing a sequence of numbers, often at a scale where accumulator width and numeric precision genuinely matter.
- **A building block for other array algorithms** — prefix sums, sliding-window techniques, and average/mean calculations all start from being able to correctly and efficiently sum a range of elements.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | [3, 9, 5] | 17 |
| `test_example_2_mixed_signs` | [-3, 10, -7, 4] | 4 |
| `test_empty_array` | [] | 0 |
| `test_single_element` | [42] | 42 |
| `test_all_negative` | [-5, -10, -3] | -18 |
| `test_large_array_near_32bit_boundary` | [2147483647] × 100000 | 214748364700000 |

All 6 tests (12 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation. The large-array test confirms Python's arbitrary-precision integers handle a sum well beyond the 32-bit signed range without any special accumulator type, as discussed above.

Run with:
```bash
cd Arrays/sum_of_array_elements
python3 -m unittest -v
```
