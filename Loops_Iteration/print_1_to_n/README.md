# Print Numbers from 1 to N

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/print-1-to-n
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer `n`, return an array of the integers from 1 to n in increasing order.

The first element of the array is 1, the last element is n, and every integer in between appears exactly once.

**Example 1**
```
Input:  n = 5
Output: [1, 2, 3, 4, 5]
```

**Example 2**
```
Input:  n = 3
Output: [1, 2, 3]
```

**Constraints**
```
1 <= n <= 1000
n is a positive integer, so the result always contains at least one element.
```

## How to Solve It — Thought Process

The task is just counting: start at 1, keep going up by one, stop once you've reached `n`. The only real trap is the loop boundary — since `n` itself has to be included, the condition has to be "while the counter is less than or **equal to** `n`," not "while it's less than `n`." Writing `<` instead of `<=` is a classic off-by-one mistake that silently drops the last number from the output.

The most direct way to express "keep counting up" is a plain loop: start a counter at 1, append it to the result, increment, and repeat until the counter passes `n`. That's the natural first approach, and it's already about as efficient as this problem gets — one pass, one append per number, nothing wasted.

There's a second way to express the same idea without an explicit loop: recursion. The insight is that "the numbers from 1 to n" is just "the numbers from 1 to n-1" with `n` tacked on at the end — the same problem, one size smaller. A helper function can carry a running counter `i` down a chain of calls, appending `i` and recursing on `i + 1`, until `i` exceeds `n` and the chain stops (the base case). Because each call appends its own value *before* recursing (not after), the numbers come out in increasing order without needing to reverse anything afterward. Recursion doesn't do less work than the loop — it still touches every number exactly once — but it trades an explicit counter variable for the call stack, at the cost of one stack frame per number (which matters more as `n` grows, and risks hitting Python's recursion limit for larger inputs even within this problem's stated constraints).

## Brute Force Solution — Recursion

```python
class Solution:
    def print_1_to_n_recursive(self, n):
        result = []

        def helper(i):
            if i > n :
                return
            result.append(i)
            helper(i + 1)
        helper(1)
        return result
```

## Optimized Solution — Iterative Loop

```python
    def print_1_to_n_iterative(self, n):
        result = []
        i = 1
        while(i <= n):
            result.append(i)
            i += 1
        return result
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().print_1_to_n_iterative(n)`), not on the class directly.

> **Note on `print_1_to_n_recursive`'s recursion depth (not a bug, still applies):** this problem's constraints allow `n` up to `1000`, but Python's default recursion limit (`sys.getrecursionlimit()`, normally `1000`) means a plain recursive call chain of depth close to `1000` raises `RecursionError` before finishing — confirmed here: `n = 1000` fails this way, and under a test runner's own added stack frames, failure starts even a bit earlier (around `n = 985` in local testing). The algorithm's logic is correct; it's the recursion depth itself that becomes a problem at the upper end of this problem's own constraint range, exactly as flagged in the Thought Process above. `print_1_to_n_iterative` has no such limit and handles the full range including `n = 1000`.

### Algorithm — Recursion
1. Create an empty list `result`.
2. Define a helper that takes the current value `i`.
3. If `i > n`, stop — every number has already been added.
4. Otherwise, append `i` to `result`, then call the helper with `i + 1`.
5. Start the helper at `1` and return `result`.

### Algorithm — Iterative Loop
1. Create an empty list `result` and a counter `i = 1`.
2. While `i <= n`: append `i` to `result`, then increment `i`.
3. Return `result`.

## Dry Run

### Recursion — `n = 3`

| Call | `i` | `i > n`? | Action |
|---|---|---|---|
| `helper(1)` | 1 | No | append `1`, call `helper(2)` |
| `helper(2)` | 2 | No | append `2`, call `helper(3)` |
| `helper(3)` | 3 | No | append `3`, call `helper(4)` |
| `helper(4)` | 4 | Yes | return (base case) |

The numbers were appended in the order `1, 2, 3` as the calls went forward, so no reversal is needed. Return `[1, 2, 3]`. ✅ matches expected output.

### Iterative Loop — `n = 5`

| Step | `i` | `i <= 5`? | `result` after append | `i` after increment |
|---|---|---|---|---|
| 1 | 1 | Yes | `[1]` | 2 |
| 2 | 2 | Yes | `[1, 2]` | 3 |
| 3 | 3 | Yes | `[1, 2, 3]` | 4 |
| 4 | 4 | Yes | `[1, 2, 3, 4]` | 5 |
| 5 | 5 | Yes | `[1, 2, 3, 4, 5]` | 6 |
| 6 | 6 | No → loop exits | — | — |

Return `[1, 2, 3, 4, 5]`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Recursion | O(n) | O(n) | O(n) for the output list, **plus** O(n) recursion depth on the call stack — one frame per number, on top of the list itself. |
| Iterative Loop | O(n) | O(n) | O(n) for the output list only; no extra call-stack usage, so this is the more efficient of the two even though both are O(n) asymptotically. |

Both approaches do the same amount of work — one pass, touching each number once — but the iterative loop is the more practical choice: it avoids the extra stack frames recursion needs, which matters as `n` grows toward the constraint's upper bound (`1000`) and avoids any risk of hitting Python's recursion limit.

## Real-World Use Case

Counting up from a starting point to a bound is one of the most common building blocks in software:

- **Pagination and batch indexing** — generating page numbers, row indices, or batch IDs (`1` through `total_batches`) is exactly this pattern.
- **UI rendering** — numbering rows in a table, generating tick marks on a slider, or laying out a fixed-size grid all iterate a range of integers to produce their labels.
- **Generating test/sample data** — producing sequential IDs (`user_1`, `user_2`, ..., `user_n`) for seeding a database or test fixture uses the same counting loop.
- **Recursion as a teaching bridge** — the recursive version here is a small, safe example of the "solve a smaller version of the same problem" pattern that shows up in real recursive algorithms (tree traversal, divide-and-conquer, backtracking), where the base case and the "do work then recurse" order matter just as much as they do here.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | n = 5 | [1, 2, 3, 4, 5] |
| `test_example_2` | n = 3 | [1, 2, 3] |
| `test_min_boundary` | n = 1 | [1] |
| `test_large_n_within_recursion_limit` | n = 950 | [1..950] |
| `test_max_constraint_iterative_only` | n = 1000 | [1..1000] — iterative only, since `print_1_to_n_recursive` hits Python's default recursion limit at this depth (see the recursion-depth note above) |

All 5 tests (9 sub-assertions across the 2 methods) pass against the current `sol.py`. `print_1_to_n_recursive` is exercised up to `n = 950`, not the full constraint range up to `n = 1000`, for the recursion-depth reason noted above; `print_1_to_n_iterative` has no such limit and is tested at the full `n = 1000`.

Run with:
```bash
cd Loops_Iteration/print_1_to_n
python3 -m unittest -v
```
