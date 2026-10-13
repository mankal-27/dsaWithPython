# Reverse an Array In Place

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/reverse-an-array-in-place
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer array nums, reverse the order of its elements in place and return the reversed array.

Reversing in place means you must rearrange the elements within the same array. Do not allocate a second array to hold the result.

**Example 1**
```
Input:  nums = [1, 2, 3, 4]
Output: [4, 3, 2, 1]
```

**Example 2**
```
Input:  nums = [-3, -1, -2, -5, -4]
Output: [-4, -5, -2, -1, -3]
```

**Constraints**
```
0 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
You must modify the array in place using O(1) extra space.
```

## How to Solve It — Thought Process

The most obvious way to reverse an array is to build a brand-new one by walking the original from back to front and copying each value into the new array in that order. That's correct and easy to reason about, but it directly violates the constraint here: it needs an entire second array's worth of memory, which is O(n) extra space, not O(1). The word "in place" in the problem statement is the real instruction — the rearrangement has to happen entirely within the original array's existing storage, using only a small, fixed number of helper variables regardless of how large the array is.

Reversing without extra storage means the elements have to trade positions with each other directly, rather than being copied somewhere else. The natural way to do that is to think about which pairs of positions need to swap: in a reversed array, the element that was first needs to end up last, and the element that was last needs to end up first — and more generally, the element at position `i` needs to end up at position `n - 1 - i`. That's a mutual relationship: if position `0` needs position `n-1`'s value, then position `n-1` also needs position `0`'s value. So the two elements at the very ends of the array can simply be swapped with each other, and each is instantly in its correct final position — no extra memory required beyond a temporary variable to hold one value during the swap.

That same logic applies moving inward: after swapping the outermost pair, the next pair to fix is the ones just inside them, then the pair inside that, and so on. This naturally suggests two pointers — one starting at the left end, one at the right end — that swap their values and then step toward each other, one position at a time. Each swap permanently places two elements into their correct final positions simultaneously, so the pointers only need to travel until they meet (or cross) in the middle; there's no need to keep going once every pair has been swapped. For an array with an odd number of elements, the middle element sits exactly on the axis of symmetry — reversing it around itself is a no-op, so the pointers simply meet there without needing a swap, which is exactly what happens when `left == right` and the loop's `left < right` condition stops it naturally.

Since every element needs to end up in a different (or the same, for the middle one) position, and each swap fixes two elements at once using only a constant amount of extra memory, this two-pointer approach is already optimal on both fronts — it does the minimum possible work (roughly `n/2` swaps to move `n` elements) and uses the minimum possible extra space (O(1), just the two indices and one temporary value). What's still worth knowing is that Python offers a built-in way to express the same in-place idea without writing the swap loop by hand: `list.reverse()` performs the identical in-place reversal internally, genuinely using O(1) extra space (unlike a slice-based idiom such as `nums[::-1]`, which builds a whole new list before reassigning — that would silently violate the O(1) space constraint despite looking similarly concise).

## Solution — Two Pointers (this is already optimal; O(n) time is required since every element must be repositioned, and O(1) extra space is the minimum needed to perform a swap)

```python
class Solution:
    def reverse_array_two_pointers(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
```

## Additional Solution — Built-in `list.reverse()`

```python
    def reverse_array_builtin_reverse(self, nums):
        nums.reverse()
        return nums
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().reverse_array_builtin_reverse(nums)`), not on the class directly.
>
> **Why this counts as a genuinely different approach, not just a one-liner restatement:** `list.reverse()` performs the same in-place swap-based reversal internally, but inside CPython's C implementation rather than as an interpreted Python loop, which is typically faster in practice for the same O(n) work — and critically, it genuinely respects the O(1) extra-space constraint, unlike the tempting-looking `nums[:] = nums[::-1]` idiom, which internally builds a full reversed copy of the list (O(n) space) before slice-assigning it back, silently defeating the point of doing this "in place" at all.
>
> **A note on the Python-idiomatic swap:** the two-pointer solution above uses Python's tuple-unpacking swap (`nums[left], nums[right] = nums[right], nums[left]`) instead of a manual three-line temp-variable swap. This is still the same two-pointer algorithm and the same O(1) extra space — Python evaluates the right-hand side tuple first and then assigns both targets, so no separate named temporary variable is needed, though the underlying interpreter does use its own internal temporary storage to hold that tuple during the swap.

### Algorithm — Two Pointers
1. Set `left = 0` and `right = len(nums) - 1`.
2. While `left < right`: swap `nums[left]` and `nums[right]`.
3. Increment `left` and decrement `right`.
4. Stop when the pointers meet or cross, then return `nums`.

### Algorithm — Built-in `list.reverse()`
1. Call `nums.reverse()`, which reverses the list in place internally.
2. Return `nums`.

## Dry Run

### Two Pointers — `nums = [1, 2, 3, 4, 5]`

| Step | `left` | `right` | Swap | Array state |
|---|---|---|---|---|
| init | 0 | 4 | — | [1, 2, 3, 4, 5] |
| 1 | 0 | 4 | swap `nums[0]`, `nums[4]` | [5, 2, 3, 4, 1] |
| 2 | 1 | 3 | swap `nums[1]`, `nums[3]` | [5, 4, 3, 2, 1] |
| 3 | 2 | 2 | `left < right` is `False`, loop stops | [5, 4, 3, 2, 1] |

Return `[5, 4, 3, 2, 1]`. The middle element (index `2`, value `3`) never moves, since it's the axis of symmetry for an odd-length array.

### Built-in `list.reverse()` — `nums = [1, 2, 3, 4]`

`[1, 2, 3, 4].reverse()` reverses the list in place, leaving `nums` as `[4, 3, 2, 1]`. Returning `nums` afterward gives `[4, 3, 2, 1]`. ✅ matches expected output.

**Empty and single-element cases:** For `nums = []`, Two Pointers sets `left = 0`, `right = -1`; `left < right` is immediately `False`, so the loop never runs and `[]` is returned unchanged. For `nums = [7]`, `left = 0`, `right = 0`; `left < right` is `False`, so nothing swaps and `[7]` is returned unchanged. `list.reverse()` handles both the same way — reversing an empty or single-element list is a no-op.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Two Pointers | O(n) | O(1) | Roughly n/2 swaps move every element into position; only two indices and one temporary value are used. Already optimal on both time and space. |
| Built-in `list.reverse()` | O(n) | O(1) | Same asymptotic complexity as Two Pointers; the swap loop runs in CPython's C implementation instead of interpreted Python, which is typically faster in practice for the same work — and, unlike `nums[::-1]`, genuinely respects the O(1) space constraint. |

## Real-World Use Case

Reversing a sequence in place, without allocating a second copy, is a building block that matters most when memory efficiency or mutation-in-place semantics are the point:

- **Memory-constrained environments** — embedded systems, large-scale data processing, or any context where doubling memory usage just to flip an order is unacceptable benefits directly from an O(1)-space reversal.
- **Undo/redo and history navigation** — reversing the order of a recorded action list or navigation history (to replay events backward, for instance) is a direct application of this exact operation.
- **A building block for other array algorithms** — reversing a sub-range of an array (not just the whole thing) using the same two-pointer technique is the core mechanism behind array-rotation algorithms (rotate left/right by k) and certain in-place string-manipulation problems (like reversing words in a sentence while keeping the words themselves intact).
- **Teaching the two-pointer, swap-from-the-outside-in pattern** — this exact technique (pointers starting at both ends, converging while swapping) recurs across many problems: palindrome checking, partitioning arrays, and certain sorting-adjacent algorithms all build on the same "walk inward from both ends" idea introduced here.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, passing a fresh copy of the input list to each call since both methods mutate their argument in place:

| Test | Input | Expected |
|---|---|---|
| `test_example_1_even_length` | [1, 2, 3, 4] | [4, 3, 2, 1] |
| `test_example_2_odd_length_negative` | [-3, -1, -2, -5, -4] | [-4, -5, -2, -1, -3] |
| `test_empty_array` | [] | [] |
| `test_single_element` | [7] | [7] |
| `test_two_elements` | [1, 2] | [2, 1] |
| `test_odd_length_middle_element_unmoved` | [1, 2, 3, 4, 5] | [5, 4, 3, 2, 1] |
| `test_large_array_near_length_constraint` | list(range(10000)) | list(range(9999, -1, -1)) |
| `test_returns_the_same_list_object` | [1, 2, 3] | (asserts the returned object `is` the original list, confirming in-place mutation rather than a new list being built) |

All 8 tests (16 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation.

Run with:
```bash
cd Arrays/reverse_an_array_in_place
python3 -m unittest -v
```
