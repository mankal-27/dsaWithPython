# Positive, Negative, or Zero

**Topic:** Conditionals & Decision Making
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/positive-negative-or-zero
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer `n`, classify it as positive, negative, or zero.

Return `"Positive"` if `n` is greater than 0, `"Negative"` if `n` is less than 0, and `"Zero"` if `n` equals 0.

**Example 1**
```
Input:  n = 5
Output: "Positive"
```

**Example 2**
```
Input:  n = 0
Output: "Zero"
```

**Constraints**
```
n is an integer that fits in a 32-bit signed range.
n can be negative, zero, or positive.
```

## How to Solve It — Thought Process

Every integer falls into exactly one of three buckets: positive, negative, or zero. The question is just how to report which bucket `n` is in, using as few comparisons as possible.

The natural first instinct is to check all three conditions independently: "is `n > 0`?", "is `n < 0`?", "is `n == 0`?" That works, but it's redundant — if the first two checks are both false, the third one is guaranteed to be true, so there's no need to actually test for it. Zero is what's *left over* once positive and negative have both been ruled out, not something that needs its own comparison.

That observation is exactly what an if/elif/else (or else-if) ladder captures: test the first condition, and only if it fails, test the second; if both fail, fall through to a final branch that doesn't test anything at all, because by then only one possibility remains. So the whole problem reduces to two comparisons and a catch-all — ask "greater than 0?", then "less than 0?", and let the `else` absorb zero. There's no bit-trick or arithmetic shortcut that improves on this: three mutually exclusive outcomes fundamentally need at least two comparisons to distinguish between them, so the straightforward ladder already is the optimal solution here — same as with Even or Odd, the "optimization" opportunities in a problem like this are about which comparisons you write, not about algorithmic complexity.

## Brute Force / Optimized Solution

There's only one meaningful approach here — an else-if ladder is already O(1) and about as simple as this problem gets, so brute force and optimized are the same solution (see the Thought Process above for why no further improvement is possible):

```python
class Solution:
    def classify_sign(self, n):
        if(n > 0):
            return "Positive"
        elif (n < 0):
            return "Negative"
        else:
            return "Zero"
```

> **Calling convention:** an instance method (it takes `self`) — call it on an instance (`Solution().classify_sign(n)`), not on the class directly.

### Algorithm
1. If `n` is greater than `0`, return `"Positive"`.
2. Otherwise, if `n` is less than `0`, return `"Negative"`.
3. Otherwise, `n` must be `0`, so return `"Zero"`.

## Dry Run

### `n = 5`

| Step | Operation | Value |
|---|---|---|
| 1 | `n > 0`? (`5 > 0`) → True | return `"Positive"` |

Return `"Positive"`. ✅ matches expected output.

### `n = 0`

| Step | Operation | Value |
|---|---|---|
| 1 | `n > 0`? (`0 > 0`) → False | continue |
| 2 | `n < 0`? (`0 < 0`) → False | fall through to `else` |
| 3 | neither matched | return `"Zero"` |

Return `"Zero"`. ✅ matches expected output.

### `n = -7`

| Step | Operation | Value |
|---|---|---|
| 1 | `n > 0`? (`-7 > 0`) → False | continue |
| 2 | `n < 0`? (`-7 < 0`) → True | return `"Negative"` |

Return `"Negative"`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Else-If Ladder | O(1) | O(1) | At most two comparisons run before a result is returned; no data structures grow with the input. |

## Real-World Use Case

Classifying a value's sign is a small check, but it's a building block used constantly:

- **Financial applications** — flagging a transaction or balance as a gain, loss, or break-even (deposit vs. withdrawal vs. no change) uses exactly this three-way sign classification.
- **Control systems and games** — deciding whether to accelerate, decelerate, or hold steady (e.g. comparing a target value to a current value) branches on the sign of the difference.
- **Data validation and analytics** — bucketing sentiment scores, temperature deltas, or stock price changes into positive/negative/neutral categories for dashboards and reports.
- **Sorting and comparator functions** — comparator-based sorts (like `compareTo`/`cmp` in many languages) return a negative, zero, or positive number specifically so callers can branch on its sign the same way this problem does.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and checks `classify_sign` against each case:

| Test | Input | Expected |
|---|---|---|
| `test_example_1_positive` | 5 | "Positive" |
| `test_example_2_zero` | 0 | "Zero" |
| `test_negative` | -7 | "Negative" |
| `test_small_positive_boundary` | 1 | "Positive" |
| `test_small_negative_boundary` | -1 | "Negative" |
| `test_max_32bit_signed_int_positive` | 2147483647 | "Positive" |
| `test_min_32bit_signed_int_negative` | -2147483648 | "Negative" |

All 7 tests pass against the current `sol.py`.

Run with:
```bash
cd Conditionals_Decision_Making/positive_negative_or_zero
python3 -m unittest -v
```
