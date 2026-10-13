# Sum of Even or Odd Numbers from 1 to N

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/sum-even-or-odd-1-to-n
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer n and a string parity that is either "even" or "odd", return the sum of all numbers of that parity from 1 to n inclusive.

For example, when n is 10 and parity is "even", the numbers in range are 2, 4, 6, 8, and 10, which sum to 30. When parity is "odd", the numbers are 1, 3, 5, 7, and 9, which sum to 25. If there is no matching number in the range, return 0.

**Example 1**
```
Input:  n = 10, parity = "even"
Output: 30
```
The even numbers from 1 to 10 are 2, 4, 6, 8, and 10. They add up to 30.

**Example 2**
```
Input:  n = 9, parity = "odd"
Output: 25
```
The odd numbers from 1 to 9 are 1, 3, 5, 7, and 9, which sum to 25.

**Constraints**
```
0 <= n <= 10000
parity is always either "even" or "odd"
The sum fits comfortably in a 32-bit signed integer for the given range. For much larger values of n, switch to a 64-bit type to avoid overflow.
```

## How to Solve It — Thought Process

Strip away the "even or odd" framing for a second and this is really "sum every number in `1..n` that matches a filter." The most literal way to do that is to walk every integer from 1 to n and, for each one, ask "does it match the requested parity?" — if `parity` is `"even"`, that's asking whether `i % 2 == 0`; if `"odd"`, whether `i % 2 == 1`. That's a perfectly correct O(n) approach, and it's the natural first thing to write, because it treats "sum matching numbers" as literally as possible: visit everything, keep what matches.

The wasteful part is that half the numbers visited get thrown away — for `parity = "even"` you check every odd number just to discard it. Since even and odd numbers already form their own evenly-spaced sequences (2, 4, 6, ... or 1, 3, 5, ...), there's no need to inspect the ones in between at all: start directly at the first matching number (`2` for even, `1` for odd) and jump forward by `2` each time, adding as you go. This still touches roughly `n / 2` numbers — still O(n) — but it removes the modulo check from the loop entirely and visits only numbers that are guaranteed to count.

Neither of those approaches, though, actually needs a loop at all, because the answer has a closed-form shape once you notice what's being summed. The even numbers up to `n` are `2, 4, 6, ..., 2k` where `k = n // 2` is how many of them there are; factor the `2` out of every term and that's `2 * (1 + 2 + ... + k)`, and the sum of the first `k` positive integers is the classic `k * (k + 1) / 2` — so the even sum collapses to `k * (k + 1)`. The odd numbers have an even tidier pattern: the sum of the first `k` odd numbers is always a perfect square, `k * k` (`1 = 1`, `1+3 = 4`, `1+3+5 = 9`, `1+3+5+7 = 16`, and so on — each new odd number extends the square by one more "layer"), where `k = (n + 1) // 2` is how many odd numbers are in range. Once that pattern is recognized, the whole problem is one division and one multiplication — no loop, no per-number work, and the runtime stops depending on `n` at all.

One edge case worth naming explicitly: when there's no matching number in range at all (e.g. `n = 0` or `n = 1` with `parity = "even"`), every approach above should naturally fall out to `0` — the loop-based versions never add anything, and in the formula version `k` itself becomes `0`, so `k * (k + 1)` and `k * k` are both `0` without needing a special case.

## Brute Force Solution — Loop with Modulo

```python
class Solution:
    def sum_even_or_odd_loop_modulo(self, n, parity):
        target = 0 if parity == "even" else 1
        total = 0
        for i in range(1, n + 1):
            if i % 2 == target:      # keep only numbers matching the requested parity
                total += i
        return total
```

## Optimized Solution — Direct Formula

```python
    def sum_even_or_odd_formula(self, n, parity):
        if parity == "even":
            k = n // 2
            return k * (k + 1)
        else:
            k = (n + 1) // 2
            return k * k
```

## Additional Solution — Step by Two

A middle ground between the two above: still a loop (still touches every matching number one at a time), but skips the numbers that don't match instead of testing and discarding them.

```python
    def sum_even_or_odd_step_by_two(self, n, parity):
        start = 2 if parity == "even" else 1
        total = 0
        i = start
        while i <= n:
            total += i
            i += 2
        return total
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().sum_even_or_odd_formula(n, parity)`), not on the class directly.

### Algorithm — Loop with Modulo
1. Set `target` to `0` for `"even"`, `1` for `"odd"`.
2. Start `total = 0`.
3. Loop `i` from `1` to `n` inclusive: if `i % 2 == target`, add `i` to `total`.
4. Return `total`.

### Algorithm — Step by Two
1. Set `start` to `2` for `"even"`, `1` for `"odd"`.
2. Start `total = 0` and `i = start`.
3. While `i <= n`: add `i` to `total`, then increase `i` by `2`.
4. Return `total`.

### Algorithm — Direct Formula
1. If `parity` is `"even"`: compute `k = n // 2`, return `k * (k + 1)`.
2. Otherwise (`"odd"`): compute `k = (n + 1) // 2`, return `k * k`.

## Dry Run

### Loop with Modulo — `n = 10, parity = "even"` (first 3 and last iteration)

| `i` | `i % 2 == 0`? | `total` after |
|---|---|---|
| 1 | No | 0 |
| 2 | Yes | 2 |
| 3 | No | 2 |
| ... | ... | ... |
| 10 | Yes | 30 |

Return `30`. ✅ matches expected output.

### Step by Two — `n = 9, parity = "odd"`

| Step | `i` | `i <= 9`? | `total` after `+= i` | `i` after `+= 2` |
|---|---|---|---|---|
| 1 | 1 | Yes | 1 | 3 |
| 2 | 3 | Yes | 4 | 5 |
| 3 | 5 | Yes | 9 | 7 |
| 4 | 7 | Yes | 16 | 9 |
| 5 | 9 | Yes | 25 | 11 |
| 6 | 11 | No → loop exits | — | — |

Return `25`. ✅ matches expected output.

### Direct Formula — `n = 10, parity = "even"`

| Step | Operation | Value |
|---|---|---|
| 1 | `k = 10 // 2` | `5` |
| 2 | `k * (k + 1) = 5 * 6` | `30` |

Return `30`. ✅ matches expected output.

**Second dry run — `n = 1, parity = "even"` (no matching numbers):** `k = 1 // 2 = 0`, so `k * (k + 1) = 0 * 1 = 0`. Return `0`. ✅ correctly handles the empty-range edge case without a special-case branch.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Loop with Modulo | O(n) | O(1) | Visits every integer from 1 to n, including the ones it discards. |
| Step by Two | O(n) | O(1) | Still linear (visits ~n/2 numbers), but only ever touches numbers that match — no wasted modulo checks. |
| Direct Formula | O(1) | O(1) | One division and one multiplication regardless of n — the closed-form sum replaces the loop entirely. |

The direct formula is the clear winner asymptotically — it's the only approach whose runtime doesn't grow with `n` at all. The other two are both O(n), but Step by Two does roughly half the iterations of Loop with Modulo and skips the per-iteration branch, so it's a meaningful constant-factor improvement even though it doesn't change the complexity class.

## Real-World Use Case

Summing a filtered arithmetic sequence, and recognizing when a closed-form formula can replace a loop, comes up constantly:

- **Billing and inventory systems** — computing totals over alternating or periodic subsets (e.g. "sum of charges on odd-numbered invoice cycles") uses the same filter-then-sum or step-by-two pattern.
- **Analytics dashboards on large ranges** — when a metric needs to be aggregated over millions of rows that follow a predictable arithmetic pattern, recognizing a closed-form sum (like this problem's) turns an O(n) scan into an O(1) lookup, which matters enormously at scale.
- **Test/sample data generation** — generating and summing alternating datasets (every other row, every Nth timestamp) for synthetic benchmarks often starts as a loop and gets optimized the same way once the pattern is understood.
- **Teaching mathematical induction and pattern recognition** — the "sum of the first k odd numbers is a perfect square" identity used in the Direct Formula approach is a classic entry point for proof by induction, and recognizing arithmetic-series patterns like this is a recurring skill across many other algorithmic problems (not just loops).

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | n=10, parity="even" | 30 |
| `test_example_2` | n=9, parity="odd" | 25 |
| `test_empty_range_zero` | n=0, parity="even" | 0 |
| `test_empty_range_one_even` | n=1, parity="even" | 0 |
| `test_smallest_odd` | n=1, parity="odd" | 1 |
| `test_max_constraint_even` | n=10000, parity="even" | 25005000 |
| `test_max_constraint_odd` | n=10000, parity="odd" | 25000000 |

All 7 tests (21 sub-assertions across the 3 methods) pass against the current `sol.py`.

Run with:
```bash
cd Loops_Iteration/sum_even_odd_1_to_n
python3 -m unittest -v
```
