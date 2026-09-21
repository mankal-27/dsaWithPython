# Even or Odd

**Topic:** Conditionals & Decision Making
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/even-or-odd
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer `n`, determine whether it is even or odd.

Return the string `"Even"` if `n` is divisible by 2, and `"Odd"` otherwise.

**Example 1**
```
Input:  n = 4
Output: "Even"
```

**Example 2**
```
Input:  n = -3
Output: "Odd"
```

**Constraints**
```
n is an integer that fits in a 32-bit signed range.
n can be negative, zero, or positive.
```

## How to Solve It — Thought Process

An even number divides by 2 with nothing left over; an odd number always leaves exactly one unit over. So the whole problem reduces to one question: what's the remainder when `n` is divided by 2?

The first-instinct approach is `n % 2 == 1` — "if the remainder is 1, it's odd." That's a trap for negative numbers in most languages: in Java, C++, C#, Go, and JavaScript, `-3 % 2` evaluates to `-1`, not `1`, because those languages' `%` keeps the *dividend's* sign. Testing for `== 1` would then wrongly call every negative odd number even. The fix is to test `n % 2 != 0` instead of `n % 2 == 1` — `-1` is just as "not zero" as `1` is, so this version is correct regardless of which sign convention the remainder ends up with.

**A note specific to Python:** Python's `%` operator keeps the *divisor's* sign (floor-division semantics), so `-3 % 2` is `1` in Python, not `-1` — meaning the naive `n % 2 == 1` check would actually work correctly here, unlike in Java/C++. It's still worth writing `!= 0` rather than `== 1`: it's the portable, self-documenting version that doesn't depend on which of the two sign conventions the language happens to use, and it reads as "test whether the remainder is nonzero" rather than "test whether the remainder happens to equal this one specific value."

There's a second way to answer the same question that skips division entirely: look at the number's binary representation. Only the last bit determines parity — every other bit represents a place value of 2, 4, 8, etc., all of which are even and can't change whether the whole number is even or odd. So `n & 1` (bitwise AND with `1`) isolates just that last bit: `1` means odd, `0` means even. This works for negative numbers too, because two's complement preserves that same parity bit in the lowest position. Both approaches are O(1), so the "optimization" here isn't about big-O — it's that a single bitwise AND is typically a cheaper CPU operation than a division/modulo, which is why `n & 1` is the idiom experienced programmers reach for.

## Solution

Implemented as a `Solution` class with one method per approach:

```python
class Solution:
    def even_or_odd_modulo(self, n):
        # Brute Force - Modulo Check
        if n % 2 != 0:
            return "Odd"
        return "Even"

    def even_or_odd_bitwise(self, n):
        # Optimized - Bitwise AND
        if n & 1:
            return "Odd"
        return "Even"
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().even_or_odd_modulo(n)`), not on the class directly.

### Brute Force — `even_or_odd_modulo`

Computes the remainder of `n` divided by 2, and tests whether it's zero.

**Algorithm**
1. Compute `n % 2`.
2. If the result is not `0`, return `"Odd"`.
3. Otherwise return `"Even"`.

### Optimized — `even_or_odd_bitwise`

Looks at the number's lowest bit directly instead of computing a division.

**Algorithm**
1. Compute `n & 1` to isolate the lowest bit.
2. If the result is `1`, return `"Odd"`.
3. Otherwise return `"Even"`.

## Dry Run

### Modulo Check — `n = -3`

| Step | Operation | Value |
|---|---|---|
| 1 | `n % 2` (Python: floor-division semantics) | `1` |
| 2 | `1 != 0`? → True | return `"Odd"` |

Return `"Odd"`. ✅ matches expected output. (Note: in Python this works even with a naive `== 1` check, since Python's `%` gives `1` here rather than `-1` — but `!= 0` is used anyway for portability, as explained above.)

**Second dry run — `n = 4`:**

| Step | Operation | Value |
|---|---|---|
| 1 | `n % 2` | `0` |
| 2 | `0 != 0`? → False | return `"Even"` |

Return `"Even"`. ✅ matches expected output.

### Bitwise AND — `n = 7` (binary `0111`)

| Step | Operation | Value |
|---|---|---|
| 1 | `n & 1` (`0111 AND 0001`) | `0001` = `1` |
| 2 | `1` is truthy | return `"Odd"` |

Return `"Odd"`. ✅ matches expected output.

**Second dry run — `n = -4` (negative, binary in two's complement: `...11111100`):**

| Step | Operation | Value |
|---|---|---|
| 1 | `n & 1` (`...11111100 AND ...00000001`) | `0` |
| 2 | `0` is falsy | return `"Even"` |

Return `"Even"`. ✅ correct — confirms the bitwise approach handles negatives correctly via two's complement, without any sign-specific logic.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Modulo Check (`% 2 != 0`) | O(1) | O(1) | Single division/modulo operation, correct for all signs when compared against 0 rather than 1. |
| Bitwise AND (`& 1`) | O(1) | O(1) | Single bitwise operation, no division at all; typically cheaper at the hardware level even though both are O(1) asymptotically. |

Both approaches are O(1) time and space; like the Absolute Value problem, the "optimization" here is about using a cheaper primitive operation (bitwise AND vs. division), not about reducing algorithmic complexity — there's nothing left to reduce at O(1).

## Real-World Use Case

Parity checking is a tiny operation, but it's a building block used constantly:

- **Alternating UI styling** — "zebra-striping" table rows or list items (alternating background colors) checks `index % 2` to decide which style to apply.
- **Load balancing and simple hashing** — routing requests to one of two servers, or bucketing data into even/odd groups, uses parity as the cheapest possible 2-way split.
- **Checksums and error detection** — parity bits in memory (ECC RAM) and simple network protocols use exactly this even/odd bit check to detect single-bit transmission errors.
- **Algorithm patterns** — many array/matrix problems branch on index parity (e.g. alternating merge of two lists, checkerboard patterns, "swap adjacent pairs" problems), and bit-level parity checks (`n & 1`) show up throughout bit-manipulation problems as the fundamental primitive.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1_even` | 4 | "Even" |
| `test_example_2_negative_odd` | -3 | "Odd" |
| `test_zero` | 0 | "Even" |
| `test_positive_odd` | 7 | "Odd" |
| `test_negative_even` | -4 | "Even" |
| `test_small_positive_odd` | 1 | "Odd" |
| `test_max_32bit_signed_int_odd` | 2147483647 | "Odd" |
| `test_min_32bit_signed_int_even` | -2147483648 | "Even" |

All 8 tests (16 sub-assertions across the 2 methods) pass against the current `sol.py`.

Run with:
```bash
cd Conditionals_Decision_Making/even_or_odd
python3 -m unittest -v
```
