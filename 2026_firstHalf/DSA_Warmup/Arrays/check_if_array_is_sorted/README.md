# Check if an Array is Sorted

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/check-if-array-is-sorted
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer array nums, return true if it is sorted in non-decreasing order, and false otherwise.

An array is sorted in non-decreasing order when each element is less than or equal to the element that follows it. Equal adjacent values are allowed, so [1, 2, 2, 3] counts as sorted. An empty array or a single-element array is considered sorted.

**Example 1**
```
Input:  nums = [1, 2, 2, 3]
Output: true
```

**Example 2**
```
Input:  nums = [3, 1, 2]
Output: false
```

**Constraints**
```
0 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
The array may be empty or contain a single element.
```

## How to Solve It — Thought Process

"Is this array sorted" sounds like it might call for actually sorting something, but it doesn't — sorting the array and comparing it to the original would work, but it's solving a harder problem than what's being asked. The question isn't "what would this array look like if sorted," it's just "does the order already hold," and that's something that can be checked directly without rearranging anything.

The key phrase to get precise about is "non-decreasing," which is a weaker condition than "strictly increasing" and it's worth being explicit about the difference. Strictly increasing would forbid any two equal neighbors; non-decreasing explicitly allows them — `[1, 2, 2, 3]` counts as sorted even though two adjacent `2`s are equal, because neither of them is *smaller* than the one before it. The only thing that actually breaks non-decreasing order is a strict drop: some `nums[i]` that's *greater than* `nums[i + 1]`. So the comparison to make at each adjacent pair is "is the left one bigger than the right one," not "are they different," and getting that comparison operator right (`>` for a violation, not `!=` or `>=`) is what separates a correct solution from one that would wrongly reject legitimately sorted arrays containing duplicates.

Since a single decreasing pair anywhere in the array is enough to disqualify the whole thing, there's no need to look any further once one is found — checking can stop and immediately report "not sorted." That's a meaningful shortcut in practice (an array that goes wrong near the beginning gets rejected almost instantly), even though it doesn't change the worst-case complexity: a fully sorted array, or an array that's almost sorted with the one violation near the very end, still requires looking at every adjacent pair before concluding anything. Every element (except the very first) has exactly one relationship that matters — how it compares to the element immediately before it — so checking each of those `n - 1` adjacent pairs once, in order, is both necessary and sufficient: necessary, because skipping any pair means a violation could hide there undetected; sufficient, because non-decreasing order for the whole array is entirely defined by all of its adjacent pairs individually holding.

The empty-array and single-element cases fall out of this naturally rather than needing special-case code: with zero or one elements, there simply are no adjacent pairs to compare, so a loop that iterates over pairs never finds a violation and correctly reports "sorted" by default — which matches the problem statement's explicit rule that both cases count as sorted.

## Solution — Adjacent Comparison (this is already optimal; every adjacent pair must be checked in the worst case, since a violation could be hiding anywhere)

```python
class Solution:
    def is_sorted_adjacent_comparison(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
```

## Additional Solution — Built-in `all()` with `zip()`

```python
    def is_sorted_builtin_all_zip(self, nums):
        return all(a <= b for a, b in zip(nums, nums[1:]))
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().is_sorted_builtin_all_zip(nums)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a one-liner restatement:** rather than manually indexing into `nums` at `i` and `i + 1`, `zip(nums, nums[1:])` restructures the problem declaratively — it produces the sequence of adjacent pairs directly, and `all()` expresses "every pair must satisfy this condition" as a single expression rather than an explicit loop with an early-return. `all()` also short-circuits on the first `False` just like the hand-written loop does, so it doesn't sacrifice the early-exit behavior — the tradeoff is the O(n) space from building `nums[1:]` as a sliced copy, in exchange for code that reads very close to the mathematical definition of non-decreasing order: "every consecutive pair satisfies `a <= b`."

### Algorithm — Adjacent Comparison
1. Loop `i` from `0` to `len(nums) - 2` (covering every adjacent pair).
2. If `nums[i] > nums[i + 1]`, return `False` immediately — a violation was found.
3. If the loop completes without finding a violation, return `True`.
4. An empty or single-element array never enters the loop body, so it returns `True` by default.

### Algorithm — Built-in `all()` with `zip()`
1. Pair each element with its successor using `zip(nums, nums[1:])`, which naturally produces zero pairs for an empty or single-element array.
2. Use `all()` to check that every paired `(a, b)` satisfies `a <= b`, short-circuiting and returning `False` on the first pair that doesn't.
3. If every pair satisfies the condition (including vacuously, when there are no pairs), `all()` returns `True`.

## Dry Run

### Adjacent Comparison — `nums = [1, 2, 2, 3]`

| `i` | `nums[i]` | `nums[i+1]` | `nums[i] > nums[i+1]`? |
|---|---|---|---|
| 0 | 1 | 2 | No |
| 1 | 2 | 2 | No (equal is allowed) |
| 2 | 2 | 3 | No |

Loop completes with no violation. Return `True`. ✅ matches expected output.

### Built-in `all()` with `zip()` — `nums = [3, 1, 2]`

`zip([3, 1, 2], [1, 2])` produces the pairs `(3, 1)` and `(1, 2)`. `all()` checks `3 <= 1` first — that's `False`, so `all()` short-circuits immediately and returns `False`. ✅ matches expected output (the second pair, `(1, 2)`, is never even checked).

**Empty and single-element cases:** for `nums = []`, `zip([], [])` produces no pairs, so `all()` over an empty sequence returns `True` by definition — vacuously, there's no pair that violates the condition. For `nums = [5]`, `nums[1:]` is `[]`, so `zip([5], [])` also produces no pairs, giving the same vacuous `True`. Adjacent Comparison handles both the same way: `range(len(nums) - 1)` is `range(-1)` or `range(0)`, both empty, so the loop body never runs and `True` is returned by default.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Adjacent Comparison | O(n) worst case | O(1) | Returns early on the first violation found; worst case (sorted or almost-sorted array) checks every adjacent pair. Already optimal. |
| Built-in `all()` with `zip()` | O(n) worst case | O(n) | `nums[1:]` creates a sliced copy of the array (minus the first element), so this uses O(n) space rather than the O(1) of the hand-written loop, in exchange for a more declarative, "read like the definition" expression of the same check. |

## Real-World Use Case

Verifying that a sequence is in order shows up as a validation or precondition step wherever ordering assumptions matter:

- **Precondition checks before applying an algorithm** — binary search and many other divide-and-conquer techniques only work correctly on sorted data; validating sortedness first (or as a debugging assertion) catches a broken assumption before it silently produces wrong answers.
- **Data quality and pipeline validation** — confirming that timestamps in a log, event IDs in a stream, or version numbers in a changelog arrive in non-decreasing order is a direct application of this exact check, and a common early-warning sign of out-of-order delivery or a bug upstream.
- **Testing and verifying sort implementations** — this is literally the correctness check used to confirm that a custom sorting algorithm actually produced sorted output.
- **UI and reporting** — validating that a "sorted by date" or "sorted by priority" list actually maintains that invariant after edits, insertions, or merges, before displaying it to a user.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1_with_duplicates` | [1, 2, 2, 3] | True |
| `test_example_2_not_sorted` | [3, 1, 2] | False |
| `test_empty_array` | [] | True |
| `test_single_element` | [5] | True |
| `test_violation_near_the_end` | [1, 2, 3, 4, 0] | False (confirms the full scan is necessary, not just an early check) |
| `test_strictly_decreasing` | [5, 4, 3, 2, 1] | False |
| `test_large_sorted_array_near_length_constraint` | list(range(100000)) | True |

All 7 tests (14 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation.

Run with:
```bash
cd Arrays/check_if_array_is_sorted
python3 -m unittest -v
```
