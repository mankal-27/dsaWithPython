# Multiplication Table of a Number

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/multiplication-table
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer `n`, return its multiplication table from n × 1 to n × 10 as an array of 10 integers.

The first element holds n × 1, the second holds n × 2, and so on through n × 10 in the last position.

**Example 1**
```
Input:  n = 5
Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

**Example 2**
```
Input:  n = 7
Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```

**Constraints**
```
-1000 <= n <= 1000
n can be negative, zero, or positive.
```

## How to Solve It — Thought Process

The output has a fixed shape no matter what `n` is: exactly 10 numbers, where the number at position `i` (1-indexed) is `n × i`. That fixed size is worth noticing up front — however this gets solved, the loop always runs exactly 10 times, so the work is O(1), not something that scales with `n`.

The most direct approach is to loop `i` from 1 to 10 and compute `n * i` directly, storing each product at index `i - 1` (since the array is 0-indexed but the multiplier starts at 1, not 0). That offset — "multiplier `i` goes at index `i - 1`" — is the one detail worth being careful about; getting it backwards would shift every value by one slot.

There's a second way to get the same numbers without using `*` at all: repeated addition. `n × i` is just `n` added to itself `i` times, so instead of multiplying, a running total can start at `0` and have `n` added to it once per iteration — after the first addition the total is `n` (i.e. `n × 1`), after the second it's `2n` (`n × 2`), and so on. By the tenth iteration the running total has naturally become `n × 10`, without ever calling the `*` operator. This works identically for negative `n` (adding a negative number repeatedly still produces the right negative multiples) and for `n = 0` (adding zero ten times just stays zero) — no special-casing needed for either sign or zero, which the problem statement calls out explicitly as something *not* to worry about.

Both approaches do the exact same fixed amount of work (10 iterations, one write each), so "optimized" here isn't about reducing complexity — there's nothing to reduce — it's about the multiplication operator being a single primitive operation versus simulating it with a loop of additions, similar to how earlier problems distinguished simulating an operation from just using the language's built-in for it.

## Brute Force Solution — Repeated Addition

```python
class Solution:
    def multiplication_table_repeated_addition(self, n):
        result = [0] * 10
        total = 0
        for i in range(1, 11):
            total = total + n
            result[i-1] = total
        return result
```

## Optimized Solution — Loop and Multiply

```python
    def multiplication_table_multiply(self, n):
        result = [0] * 10
        for i in range(1, 11):
            result[i-1] = n * i
        return result
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().multiplication_table_multiply(n)`), not on the class directly.

### Algorithm — Repeated Addition
1. Create a `result` array of length 10 (initialized to zeros).
2. Set a running total `sum = 0`.
3. Loop `i` from `1` to `10`: add `n` to `sum` (so `sum` now equals `n * i`), then store `sum` at index `i - 1`.
4. Return `result`.

### Algorithm — Loop and Multiply
1. Create a `result` array of length 10.
2. Loop `i` from `1` to `10`: set `result[i - 1] = n * i`.
3. Return `result`.

## Dry Run

### Repeated Addition — `n = 5` (first 3 and last step)

| Step | `i` | `total` before | `total = total + n` | `result[i-1] = total` |
|---|---|---|---|---|
| 1 | 1 | 0 | 5 | `result[0] = 5` |
| 2 | 2 | 5 | 10 | `result[1] = 10` |
| 3 | 3 | 10 | 15 | `result[2] = 15` |
| ... | ... | ... | ... | (continues through `i = 10`) |
| 10 | 10 | 45 | 50 | `result[9] = 50` |

Return `[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]`. ✅ matches expected output.

### Loop and Multiply — `n = 7` (first 3 and last step)

| Step | `i` | `n * i` | `result[i-1] = n * i` |
|---|---|---|---|
| 1 | 1 | 7 | `result[0] = 7` |
| 2 | 2 | 14 | `result[1] = 14` |
| 3 | 3 | 21 | `result[2] = 21` |
| ... | ... | ... | (continues through `i = 10`) |
| 10 | 10 | 70 | `result[9] = 70` |

Return `[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Repeated Addition | O(1) | O(1) | Always exactly 10 iterations regardless of `n`; output array is a fixed size of 10, so neither time nor space grows with the input. |
| Loop and Multiply | O(1) | O(1) | Same fixed 10 iterations; uses the `*` operator directly instead of simulating it with addition. |

Both approaches are O(1) in both time and space because the loop bound (10) and the output size (10) never depend on `n` — the "optimization" here is using a single multiplication per step instead of simulating it with repeated addition, not a reduction in algorithmic complexity.

## Real-World Use Case

Fixed-size lookup tables and repeated-scaling patterns show up constantly:

- **Unit conversion tables** — precomputing a small fixed-size table of conversions (e.g. inches to centimeters for 1 through 10 units) uses exactly this "loop a fixed number of times, scale by a constant" pattern.
- **Pricing and billing tiers** — generating a price list for quantities 1 through N (bulk pricing previews, "buy 1 get the per-unit cost at 2, 3, 4...") is the same fixed-range multiplication.
- **Graphics and animation** — computing evenly-spaced scaled values (tick marks on a ruler, frame positions in an animation moving at constant velocity) repeatedly applies the same scale factor across a fixed range of steps.
- **Teaching repeated addition vs. multiplication** — the repeated-addition approach here is the same idea CPUs historically used (and some embedded/low-level contexts still use) when hardware multiplication was expensive or unavailable, replacing a multiply instruction with a loop of adds.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | n = 5 | [5, 10, ..., 50] |
| `test_example_2` | n = 7 | [7, 14, ..., 70] |
| `test_zero` | n = 0 | [0] × 10 |
| `test_negative` | n = -3 | [-3, -6, ..., -30] |
| `test_one` | n = 1 | [1, 2, ..., 10] |
| `test_min_constraint` | n = -1000 | [-1000, ..., -10000] |
| `test_max_constraint` | n = 1000 | [1000, ..., 10000] |

All 7 tests (14 sub-assertions across the 2 methods) pass against the current `sol.py`.

Run with:
```bash
cd Loops_Iteration/multiplication_table
python3 -m unittest -v
```
