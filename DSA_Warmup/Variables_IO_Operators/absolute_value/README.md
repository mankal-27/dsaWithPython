# Absolute Value Without Built-in

**Topic:** Variables, I/O & Operators
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/absolute-value
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer `n`, return its absolute value without using any built-in absolute value function (such as `Math.abs`, `abs`, or `fabs`).

The absolute value of a number is its distance from zero, so it is always non-negative. For example, the absolute value of -5 is 5, and the absolute value of 5 is also 5.

**Example 1**
```
Input:  n = -5
Output: 5
```

**Example 2**
```
Input:  n = 42
Output: 42
```

**Constraints**
```
-2^31 <= n <= 2^31 - 1
The input fits in a 32-bit signed integer.
```

## How to Solve It — Thought Process

The definition itself splits the problem into two cases: when `n` is zero or positive, its absolute value is just `n`; when `n` is negative, the absolute value is `n` with its sign flipped. So really the problem is just "detect the sign, and negate only if it's negative" — there's no searching, no data structure, just a decision.

The first-instinct approach follows that definition almost word for word: compare `n` against zero, and if it's negative, return `-n`; otherwise return `n` unchanged. That's it — one comparison, at most one negation. It's already O(1), so there's no complexity to "optimize away" in the usual sense. What makes this problem interesting isn't speed, it's that there's a second, branch-free way to get the same answer using only the bit pattern of the integer, which is worth knowing because avoiding a branch matters in some low-level contexts (SIMD code, hardware description languages, or CPU pipelines where branch mispredictions are costly).

The insight behind the bit-manipulation version comes from two's complement representation: for any negative number, `-n` equals `(~n) + 1` (flip every bit, then add one). An arithmetic right shift of `n` by 31 positions produces a `mask` that is all `1` bits (`-1`) when `n` is negative, and all `0` bits (`0`) when `n` is non-negative — because that shift copies the sign bit into every position. Once you have that mask, `(n ^ mask) - mask` does the right thing automatically: XOR-ing with all-1s flips every bit (giving `~n`), and subtracting `-1` is the same as adding `1` — together that's exactly `(~n) + 1`, i.e. `-n`. XOR-ing with all-0s leaves `n` untouched, and subtracting `0` does nothing, so non-negative inputs pass straight through. One expression, no `if`.

**A note specific to Python:** the classic "INT_MIN overflows when negated" edge case (`-2^31` has no positive 32-bit representation, so negating it wraps back to itself in fixed-width languages like Java or C) genuinely doesn't apply here — Python integers are arbitrary-precision, so `abs(-2**31)` simply produces the correct, larger positive number with no overflow at all. It's still worth understanding the edge case conceptually since it would bite in a fixed-width language, but neither approach below needs a special guard for it in Python.

## Solution

Implemented as a `Solution` class with one method per approach:

```python
class Solution:
    def absolute_value_conditional(self, n):
        # Brute Force - Conditional Negation
        if n < 0:
            return -n
        return n

    def absolute_value_bitwise(self, n):
        # Optimized - Bit Manipulation, branch-free
        mask = n >> 31
        return (n ^ mask) - mask
```

> **Calling convention:** both are instance methods (they take `self`), so call them on an instance — `Solution().absolute_value_conditional(n)` — not on the class directly. The tests below instantiate `Solution()` once and call both methods on it.

### Brute Force — `absolute_value_conditional`

Translates the definition directly into code.

**Algorithm**
1. Check whether `n` is less than 0.
2. If it is, return `-n` (the negation, which is positive).
3. Otherwise return `n` as is.

### Optimized — `absolute_value_bitwise`

Uses the integer's own bit pattern to negate only when needed, with no comparison.

**Algorithm**
1. Compute `mask = n >> 31`, an arithmetic right shift. This gives all `1` bits (`-1`) for negatives and all `0` bits (`0`) otherwise.
2. Return `(n ^ mask) - mask`.

## Dry Run

### Conditional Negation — `n = -5`

| Step | Check | Result |
|---|---|---|
| 1 | `-5 < 0`? → True | go to negation branch |
| 2 | `return -(-5)` | `5` |

Return `5`. ✅ matches expected output.

**Second dry run — `n = 42` (non-negative branch):**

| Step | Check | Result |
|---|---|---|
| 1 | `42 < 0`? → False | go to else branch |
| 2 | `return 42` | `42` |

Return `42`. ✅ matches expected output.

### Bit Manipulation — `n = -5`

| Step | Operation | Value |
|---|---|---|
| start | `n = -5` (binary `...11111011`) | — |
| 1 | `mask = n >> 31` | `-1` (all `1` bits, since `n` is negative) |
| 2 | `n ^ mask` (`...11111011 XOR ...11111111`) | `...00000100` = `4` |
| 3 | `(n ^ mask) - mask` = `4 - (-1)` | `5` |

Return `5`. ✅ matches expected output.

**Second dry run — `n = 42` (non-negative case):**

| Step | Operation | Value |
|---|---|---|
| start | `n = 42` | — |
| 1 | `mask = n >> 31` | `0` (all `0` bits, since `n` is non-negative) |
| 2 | `n ^ mask` (`42 XOR 0`) | `42` |
| 3 | `(n ^ mask) - mask` = `42 - 0` | `42` |

Return `42`. ✅ matches expected output — confirms non-negative inputs pass through unchanged.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Brute Force (Conditional Negation) | O(1) | O(1) | One comparison, at most one negation. Simple and readable, includes a branch. |
| Optimized (Bit Manipulation) | O(1) | O(1) | Fixed sequence of bitwise/arithmetic ops, no branch. One extra variable (`mask`). Same big-O as the conditional version — the win is avoiding a branch, not asymptotic speed. |

Both approaches are O(1) time and space; this problem's "optimization" is about eliminating a conditional branch (useful in branch-sensitive contexts), not about reducing algorithmic complexity — there's nothing left to reduce at O(1).

## Real-World Use Case

Absolute value itself shows up everywhere (distance/error calculations, sorting by magnitude, clamping), but the *branch-free* technique here is the more specialized, interesting takeaway:

- **Branch-free / branchless programming** is used in performance-critical code (game engines, audio/signal processing, graphics shaders) where an `if` can cause a CPU pipeline stall from branch misprediction; replacing a comparison with pure arithmetic/bitwise ops keeps execution speed predictable.
- **SIMD (Single Instruction, Multiple Data) code**, which processes many values in parallel lanes, generally can't branch per-element at all — techniques like this mask-and-XOR trick are exactly how absolute value, min/max, and similar conditional logic get vectorized.
- **Cryptography and constant-time code** deliberately avoids branches on secret data, because a branch's timing can leak information via timing side-channel attacks; branch-free arithmetic like this is a building block for writing "constant-time" comparisons.
- **Hardware/digital logic design** (e.g. in Verilog/VHDL for absolute-value circuits) uses the exact same two's-complement identity (`(~n) + 1`), since real circuits are naturally suited to bitwise operations over conditional branching.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same set of inputs using `subTest`, so a single test method reports which specific variant fails if one does:

| Test | Input | Expected |
|---|---|---|
| `test_example_1_negative` | -5 | 5 |
| `test_example_2_positive` | 42 | 42 |
| `test_zero` | 0 | 0 |
| `test_already_positive` | 7 | 7 |
| `test_small_negative` | -1 | 1 |
| `test_max_32bit_signed_int` | 2147483647 | 2147483647 |
| `test_min_safely_negatable_32bit_int` | -2147483647 | 2147483647 |
| `test_true_int_min` | -2147483648 | 2147483648 |

The last test is the classic INT_MIN edge case: it would overflow in a fixed-width language (Java/C), but Python's arbitrary-precision ints handle it correctly with no special-casing needed — and the tests confirm both `absolute_value_conditional` and `absolute_value_bitwise` get it right.

Run with:
```bash
cd Variables_IO_Operators/absolute_value
python3 -m unittest -v
```

All 8 tests (16 sub-assertions across the 2 methods) pass against the current `sol.py`.
