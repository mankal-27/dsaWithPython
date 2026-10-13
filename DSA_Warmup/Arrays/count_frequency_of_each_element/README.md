# Count Frequency of Each Element

**Topic:** Arrays
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/count-frequency-of-each-element
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer array nums, return a 2D array where each row is [value, count], giving the frequency of every distinct value in nums.

The rows must be ordered by the value's first appearance in nums. If the array is empty, return an empty array.

**Example 1**
```
Input:  nums = [1, 2, 2, 3]
Output: [[1,1],[2,2],[3,1]]
```

**Example 2**
```
Input:  nums = [-1, -1, 2, -1, 2]
Output: [[-1,3],[2,2]]
```

**Constraints**
```
0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
The order of rows follows the first appearance of each value in nums.
```

## How to Solve It — Thought Process

Counting how many times each value shows up is a fundamentally different kind of task than the array problems that came before it (summing, finding a max, searching) — those all boiled a whole array down to a single number. This one needs to track *multiple* running totals simultaneously, one per distinct value, and then present them back out in a specific order. The counting itself isn't hard; the interesting part is deciding how to remember "how many of each value have I seen so far" without redoing work.

The most literal way to get the counts, without inventing any new data structure, is to lean entirely on the array itself: for each position, first check whether this exact value has already been counted (by looking at everything to its left — if it's shown up before, its row has already been produced, so skip it), and if it hasn't, scan forward from here to the end and tally every match. Processing a value only the first time it's encountered, and skipping it on every later repeat, is what naturally keeps duplicates from producing more than one row — and doing that scan-and-tally at the value's very first occurrence is also what makes the rows come out in first-appearance order for free, since positions are visited left to right. The cost is that this "look backward, then look forward" pattern happens at up to every index, so in the worst case (many distinct values) the total work scales with the square of the array's length.

The redundant work in that approach is memory, or the lack of it: nothing is carried forward between iterations, so the same comparisons get redone from scratch at each position. The fix is to keep a running tally that updates in real time — a mapping from value to count that's incremented once per element in a single left-to-right pass. By the end of that one pass, every value's true final count is already sitting in the mapping, computed with exactly one increment per array element rather than repeated rescanning.

That handles the counting cleanly, but it introduces a wrinkle around ordering, which is where the Java-oriented framing of this problem usually reaches for a second, separate list purely to remember first-appearance order — because in many languages, a hash map's iteration order isn't guaranteed to match insertion order at all. Python sidesteps that wrinkle entirely: since Python 3.7, the built-in `dict` is guaranteed by the language itself to iterate in insertion order — the order keys were first added, not some hash-based scramble. That means the exact same dictionary used to hold the running counts can *also* serve as the record of first-appearance order, just by checking membership before incrementing (a key's very first insertion happens exactly once, at its first appearance) and then iterating the dictionary at the end. There's no need for the parallel `order` list the Java version keeps — one dictionary structurally captures both pieces of information the problem requires, which turns "count efficiently" and "remember first-seen order" from two separate concerns into one.

## Brute Force Solution — Nested Loop

**⚠️ Known bug:** as implemented, this method has two separate defects and crashes with a `TypeError` on almost every non-trivial input. The intended algorithm is described below the code; see the "Known bug" note directly under it for the confirmed, traced behavior of the actual code.

```python
from collections import Counter

class Solution:
    def count_frequency_nested_loop(self, nums):
        result = []
        for i in range(len(nums)):
            seen = False
            for j in range(i):
                if nums[i] == nums[j]:
                    seen = True
                    break
                if seen:
                    continue
                count = 0
                for k in range(i, len(nums)):
                    if nums[k] == nums[i]:
                        count += 1
                result.append([nums[i]], count)
        return result
```

> **⚠️ Known bug 1 — wrong argument count to `.append()`:** the last line is `result.append([nums[i]], count)`, which calls `list.append()` with *two* positional arguments (`[nums[i]]` and `count`) instead of one list argument `[nums[i], count]`. `list.append()` only ever accepts a single argument, so this raises `TypeError: list.append() takes exactly one argument (2 given)` the first time it's reached. Confirmed trace for `nums = [1, 2, 2, 3]`: `i=0` never reaches this line (see bug 2 below), but `i=1, j=0` does — `nums[1]=2`, `nums[0]=1` aren't equal, so `seen` stays `False`, `count` is computed as `2`, and then `result.append([2], 2)` raises the `TypeError` immediately. This reproduces on every array of length ≥ 2 that isn't made entirely of one repeated value (see bug 2 for why an all-duplicates array avoids it).
>
> **⚠️ Known bug 2 — wrong indentation traps the counting logic inside the `for j` loop:** the `if seen: continue`, `count = 0`, the `for k` loop, and the final `result.append(...)` are all indented one level too deep — they sit *inside* `for j in range(i):` rather than after it. The intended structure runs the duplicate-check (`for j`) to completion first, and only then counts and appends once per index `i`. As written:
> - For `i = 0`, `range(0)` is empty, so the loop body (and therefore any append) never runs at all — the first element of the array is silently dropped from `result` no matter what.
> - For an array where every value is identical (e.g. `[2, 2, 2, 2]`), every `i > 0` immediately hits `nums[i] == nums[j]` at `j = 0` and `break`s out of the `for j` loop before the append code is ever reached — so `result` stays `[]` for the whole array, not just index 0.
> - For a single-element array (e.g. `[5]`), `i` is only ever `0`, so `range(0)` is empty and `result` stays `[]` — confirmed: `count_frequency_nested_loop([5])` returns `[]` instead of `[[5, 1]]`.
> - For any array with at least two distinct values, the append line is reached (typically at `i = 1`) and bug 1's `TypeError` fires before this indentation bug can cause a further wrong-output case.
>
> These are reported here, not silently fixed — see `test_sol.py` below for the tests that confirm this behavior against the real code (5 errors, 2 failures out of 8 tests).

### Intended Algorithm — Nested Loop
1. Create an empty result list.
2. For each index `i`: check whether `nums[i]` appeared at any earlier index `j < i`. If it did, skip this index.
3. Otherwise, scan from `i` to the end and count how many elements equal `nums[i]`.
4. Append `[nums[i], count]` to the result.
5. Return the result.

## Optimized Solution — Hash Map (Single Pass)

```python
    def count_frequency_hash_map(self, nums):
        counts = {}
        for v in nums:
            counts[v] = counts.get(v,0) + 1
        return [[v,c] for v, c in counts.items()]
```

## Additional Solution — Built-in `collections.Counter`

```python
    def count_frequency_builtin_counter(self, nums):
        return [[v,c] for v, c in Counter(nums).items()]
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().count_frequency_hash_map(nums)`), not on the class directly.
>
> **Why the Hash Map solution needs no separate "order" list in Python:** since Python 3.7, dictionary iteration order is guaranteed by the language to match insertion order. A value's first insertion into `counts` (via `counts.get(v, 0) + 1` when it isn't present yet) happens at exactly its first appearance in `nums`, so `counts.items()` at the end naturally yields entries in first-appearance order — no auxiliary list needed, unlike the two-structure approach a language without this ordering guarantee (like Java's `HashMap`) requires.
>
> **Why `Counter` counts as a genuinely different approach, not just a shorter Hash Map:** `Counter` is itself a `dict` subclass purpose-built for counting, and it inherits the same insertion-order guarantee, so it needs no separate order-tracking either — but it moves the counting logic itself into a built-in constructor (`Counter(nums)` tallies every element in one call, implemented in C) rather than a hand-written accumulation loop, which is typically faster in practice for the same O(n) work.

### Algorithm — Hash Map (Single Pass)
1. Create an empty dictionary `counts`.
2. For each value `v` in `nums`, increment `counts[v]` (defaulting to `0` via `.get(v, 0)` if not yet present).
3. Build the result by iterating `counts.items()`, which yields entries in first-appearance (insertion) order.

### Algorithm — Built-in `Counter`
1. Call `Counter(nums)`, which tallies every element's frequency in one pass internally.
2. Build the result by iterating its `.items()`, which also yields entries in first-appearance order.

## Dry Run

### Nested Loop (intended algorithm) — `nums = [1, 2, 2, 3]`

| `i` | `nums[i]` | Seen before `i`? | Count (scan from `i`) | Action |
|---|---|---|---|---|
| 0 | 1 | No | 1 | append `[1, 1]` |
| 1 | 2 | No | 2 | append `[2, 2]` |
| 2 | 2 | Yes (at `j=1`) | — | skip |
| 3 | 3 | No | 1 | append `[3, 1]` |

Intended return: `[[1,1],[2,2],[3,1]]`. This is what the algorithm *should* produce — see the traced dry run below for what the real, buggy code does instead.

### Nested Loop (as implemented) — `nums = [1, 2, 2, 3]`

| `i` | `j` | What happens |
|---|---|---|
| 0 | — | `range(0)` is empty — the `for j` loop body never runs, so nothing is appended for index 0 (element `1` is silently dropped). |
| 1 | 0 | `nums[1]=2`, `nums[0]=1` — not equal, `seen` stays `False`. Falls into the (wrongly indented) body: `count` scans `nums[1:]` for value `2` → `count = 2`. Reaches `result.append([2], 2)` → **raises `TypeError: list.append() takes exactly one argument (2 given)`.** |

Actual result: crashes with `TypeError` before returning anything. ❌ does not match the expected `[[1,1],[2,2],[3,1]]` — confirmed via direct execution (see the "Known bug" callouts above and the `test_sol.py` results below).

### Hash Map (Single Pass) — `nums = [-1, -1, 2, -1, 2]`

| Step | `v` | `counts` after |
|---|---|---|
| 1 | -1 | `{-1: 1}` |
| 2 | -1 | `{-1: 2}` |
| 3 | 2 | `{-1: 2, 2: 1}` |
| 4 | -1 | `{-1: 3, 2: 1}` |
| 5 | 2 | `{-1: 3, 2: 2}` |

`counts.items()` → `[(-1, 3), (2, 2)]`, in the order `-1` and `2` were first inserted. Return `[[-1,3],[2,2]]`. ✅ matches expected output.

### Built-in `Counter` — `nums = [9, 8, 9, 8, 7]`

`Counter([9, 8, 9, 8, 7])` tallies internally to `Counter({9: 2, 8: 2, 7: 1})`, preserving first-insertion order (`9` before `8` before `7`, since `9` was seen first). `.items()` → `[(9, 2), (8, 2), (7, 1)]`. Return `[[9,2],[8,2],[7,1]]` — matching first-appearance order, not numeric order.

## Complexity

| Approach | Time Complexity (intended) | Space Complexity (intended) | Notes |
|---|---|---|---|
| Nested Loop | O(n²) | O(1) beyond the output | **As implemented: crashes with `TypeError` on any array of length ≥ 2 that isn't made entirely of one repeated value, and silently returns the wrong (incomplete) result for a single-element or all-duplicates array.** Intended: for each index, may scan everything before it (duplicate check) and everything from it onward (counting) — work grows with the square of the length. |
| Hash Map (Single Pass) | O(n) | O(k) | One pass tallies every element; k is the number of distinct values. No separate order-tracking structure needed in Python, unlike languages without dict insertion-order guarantees. Matches actual implementation — no bugs found. |
| Built-in `Counter` | O(n) | O(k) | Same asymptotic complexity as Hash Map; the tally runs in CPython's C implementation instead of an interpreted accumulation loop, which is typically faster in practice for the same work. Matches actual implementation — no bugs found. |

For `n = 10^4`, Nested Loop can do on the order of 10^8 comparisons in the worst case (many distinct values), while both Hash Map and Counter do on the order of 10^4 operations — a difference that grows sharply as `n` grows.

## Real-World Use Case

Counting frequencies while preserving first-seen order shows up wherever "what happened, and in what order did it start happening" both matter:

- **Log and event analysis** — counting how many times each distinct error code, event type, or user action occurred, while keeping the report ordered by when each type first appeared, is a direct application of this exact pattern.
- **Deduplication with provenance** — building a list of unique items from a stream while tracking how many duplicates of each were seen (and preserving the order items were first introduced) is common in data-cleaning and ETL pipelines.
- **Word/token frequency analysis** — counting word occurrences in text while preserving the order words first appear (rather than alphabetical or by-count order) is a common preprocessing step in basic text analysis and tokenization tasks.
- **UI elements like "recently used" or tag clouds** — showing distinct categories or tags in the order a user first encountered or created them, alongside how many times each was used, is this same counting-with-order-preservation problem applied directly.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports exactly which method fails or errors.

| Test | Input | Expected | Result |
|---|---|---|---|
| `test_example_1` | `[1, 2, 2, 3]` | `[[1,1],[2,2],[3,1]]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (`TypeError`) |
| `test_example_2` | `[-1, -1, 2, -1, 2]` | `[[-1,3],[2,2]]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (`TypeError`) |
| `test_empty_array` | `[]` | `[]` | All three ✅ |
| `test_first_appearance_order_differs_from_numeric_order` | `[9, 8, 9, 8, 7]` | `[[9,2],[8,2],[7,1]]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (`TypeError`) |
| `test_all_distinct_elements` | `[4, 1, 7, 3]` | `[[4,1],[1,1],[7,1],[3,1]]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (`TypeError`) |
| `test_all_same_element` | `[2, 2, 2, 2]` | `[[2,4]]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (wrong output: returns `[]`) |
| `test_single_element` | `[5]` | `[[5,1]]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (wrong output: returns `[]`) |
| `test_large_array_near_length_constraint` | `list(range(9999)) + [9998]` (10,000 elements) | 9,998 singleton rows + `[9998, 2]` | Hash Map ✅, Counter ✅, Nested Loop ❌ (`TypeError`) |

**8 tests, 24 sub-assertions.** `count_frequency_hash_map` and `count_frequency_builtin_counter` pass every case — no bugs found in either. `count_frequency_nested_loop` fails or errors on 7 of 8 (`FAILED (failures=2, errors=5)`), confirmed identically in the cloud container and re-run directly on-device as ground truth. See the "⚠️ Known bug" callouts above the Nested Loop code block for the root cause and traced behavior — these were reported, not silently patched, and the tests above use the mathematically correct expected values throughout rather than being adjusted to match the buggy output.

Run with:
```bash
cd Arrays/count_frequency_of_each_element
python3 -m unittest -v
```
