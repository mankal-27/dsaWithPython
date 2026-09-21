# Quotient and Remainder of a Division

**Topic:** Variables, I/O & Operators
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/quotient-and-remainder
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given two integers `dividend` and `divisor`, return an array `[quotient, remainder]` where `quotient` is the result of integer division (`dividend / divisor` keeping only the whole part) and `remainder` is what is left over (`dividend % divisor`).

The two values always satisfy the relationship `dividend = divisor * quotient + remainder`.

**Example 1**
```
Input:  dividend = 17, divisor = 5
Output: [3, 2]
```

**Example 2**
```
Input:  dividend = 3, divisor = 8
Output: [0, 3]
```

**Constraints**
```
divisor != 0
Both values fit in the 32-bit signed integer range: -2^31 <= dividend, divisor <= 2^31 - 1
```

## How to Solve It — Thought Process

The quotient answers "how many whole times does the divisor fit into the dividend?" and the remainder answers "what's left over after taking out those whole copies?" Think of splitting 17 candies among 5 children: each child gets 3 candies (the quotient), and 2 are left over (the remainder). The identity `dividend = divisor * quotient + remainder` is exactly that — `5 * 3 + 2 = 17` — and it's the easiest way to sanity-check any answer you compute.

The most literal, "simulate it by hand" approach is repeated subtraction: keep subtracting the divisor from the dividend, counting how many times you can do that before what's left is smaller than the divisor. That count is the quotient, and whatever's left is the remainder. It works, but it's slow — if `dividend` is large and `divisor` is small (say `dividend = 2^31 - 1` and `divisor = 1`), you'd loop over two billion times just to count up to two billion. That inefficiency is exactly what integer division and modulo operators exist to avoid: they compute the same result in one hardware operation instead of a loop.

So the "optimized" approach here isn't a clever algorithmic trick like it was for other problems — it's simply "use the operators the language gives you" (`//` and `%` in Python), which are O(1) because division is a primitive CPU operation, not something that needs to loop.

**One subtlety worth understanding (not just using):** languages disagree on how they handle negative numbers in division. In Java, C++, C#, Go, Rust, and JavaScript, `-17 % 5` gives `-2` — the remainder takes the sign of the *dividend*, and the division truncates toward zero. Python's `%` gives `3` instead — the remainder takes the sign of the *divisor*, because Python's `//` floors toward negative infinity rather than truncating toward zero. Both conventions still satisfy the identity `dividend = divisor * quotient + remainder`, they just land on a different valid `[quotient, remainder]` pair. Since this problem's own examples only use non-negative operands, both conventions agree on the two given examples — but it's worth building the repeated-subtraction version to be sign-aware from first principles (matching Python's floor-based convention) rather than assuming truncation, precisely because the two approaches below need to agree with each other on negative inputs too.

## Solution

Implemented as a `Solution` class with one method per approach:

```python
class Solution:
    def quotient_remainder_brute(self, dividend, divisor):
        # Brute Force - Repeated Subtraction
        if dividend == 0:
            return [0, 0]

        sign_differs = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        count = 0
        while a >= b:
            a -= b
            count += 1

        if sign_differs and a != 0:
            quotient = -(count + 1)
        else:
            quotient = -(count if sign_differs else count)

        remainder = dividend - divisor * quotient
        return [quotient, remainder]

    def quotient_remainder_optimized(self, dividend, divisor):
        # Optimized - Built-in Integer Division and Modulo
        quotient = dividend // divisor
        remainder = dividend % divisor
        return [quotient, remainder]
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().quotient_remainder_brute(dividend, divisor)`), not on the class directly.

> **⚠️ Known bug in `quotient_remainder_brute`:** the line `quotient = -(count if sign_differs else count)` always evaluates to `-count`, because both branches of that ternary are the same expression (`count`) — the `if sign_differs else` adds no actual branching. This means whenever `dividend` and `divisor` have the **same sign** (both positive or both negative), the quotient comes out negated and the remainder — recomputed from the identity using that wrong quotient — comes out wrong too. For example, `quotient_remainder_brute(17, 5)` currently returns `[-3, 32]` instead of `[3, 2]`. The mixed-sign path (`sign_differs and a != 0` branch) is unaffected and correct. `quotient_remainder_optimized` doesn't have this bug and is correct for all sign combinations — confirmed by the tests below. **This hasn't been fixed here** — see the Tests section for what's failing and where to look.

### Brute Force — `quotient_remainder_brute`

Simulate long division by hand: repeatedly subtract the divisor's magnitude from the dividend's magnitude, counting how many subtractions happen, then fix up the signs at the end to (intend to) match Python's floor-division convention.

**Algorithm (as intended)**
1. Handle `dividend == 0` directly (`[0, 0]`).
2. Work with magnitudes (`abs(dividend)`, `abs(divisor)`) and repeatedly subtract, counting each subtraction, until what's left is smaller than the divisor's magnitude.
3. Adjust the quotient's sign (and bump it by one more toward negative infinity when there's a nonzero remainder and the signs differ) to match floor-division semantics.
4. Recompute `remainder` from the identity `dividend - divisor * quotient`, so it's always consistent with the chosen quotient.

Step 3 is where the bug lives — see the callout above.

### Optimized — `quotient_remainder_optimized`

Every language provides operators that compute exactly this, so there's no reason to simulate it manually.

**Algorithm**
1. Compute the quotient using integer division: `quotient = dividend // divisor`.
2. Compute the remainder using modulo: `remainder = dividend % divisor`.
3. Return `[quotient, remainder]`.

## Dry Run

### Brute Force — `dividend = 17, divisor = 5` (traces the actual buggy behavior)

| Step | a (start) | a >= b? | a -= b | count |
|---|---|---|---|---|
| 1 | 17 | yes | 12 | 1 |
| 2 | 12 | yes | 7 | 2 |
| 3 | 7 | yes | 2 | 3 |
| 4 | 2 | no → loop exits | — | 3 |

`sign_differs` is `False` (both positive), so control goes to the `else` branch: `quotient = -(count if sign_differs else count)`. Both sides of that ternary are `count`, so this is just `-(count)` = `-3`, regardless of `sign_differs`. That's the bug — it *should* be `+3` here. `remainder` is then recomputed from the (already wrong) quotient: `17 - 5*(-3) = 17 + 15 = 32`. Return `[-3, 32]`. ❌ does **not** match the expected `[3, 2]` — this is the bug described above, reproduced step by step.

### Optimized — `dividend = 17, divisor = 5`

| Step | Operation | Value |
|---|---|---|
| 1 | `quotient = 17 // 5` | `3` |
| 2 | `remainder = 17 % 5` | `2` |

Return `[3, 2]`. ✅ matches expected output.

**Second dry run (both approaches) — `dividend = 3, divisor = 8`:** since `3 < 8`, the brute-force loop never executes (`a >= b` is false immediately), so `count = 0`. The buggy `else` branch computes `quotient = -(count) = -0`, which is just `0` — the bug happens to be invisible here only because negating zero doesn't change it. `remainder = 3 - 8*0 = 3`. The optimized version gives `3 // 8 = 0` and `3 % 8 = 3` directly. Both return `[0, 3]`. ✅ matches expected output — but this is a case where the same-sign bug coincidentally doesn't manifest, not evidence that the brute-force method is correct.

**Negative-input illustration (within the stated constraints, not one of the problem's given examples) — `dividend = -17, divisor = 5`:** magnitudes are `17` and `5`, so the subtraction loop again produces `count = 3` with leftover `2`. Since `sign_differs` is `True` and the leftover (`2`) is nonzero, execution takes the **`if` branch** (`quotient = -(count + 1) = -4`), which is the branch that isn't affected by the bug. `remainder = -17 - 5*(-4) = -17 + 20 = 3`. Return `[-4, 3]`. Python's native operators agree: `-17 // 5 == -4` and `-17 % 5 == 3`. (This is also the case where Java-style languages would instead return `[-3, -2]` — same identity, different valid pair — the cross-language subtlety called out above.) Mixed-sign inputs land on this correct branch; same-sign inputs land on the buggy one.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Brute Force (Repeated Subtraction) | O(dividend / divisor) | O(1) | Loops once per whole copy of the divisor subtracted out — can be up to ~2 billion iterations for large dividends and a divisor of 1. |
| Optimized (Built-in `//` and `%`) | O(1) | O(1) | Division is a constant-time primitive CPU operation, not a loop. |

The brute-force version isn't just "less elegant" here — it's genuinely unusable for large inputs (e.g. `dividend = 2^31 - 1, divisor = 1` would take billions of loop iterations), which is a good concrete illustration of why O(1) built-in operators matter, not just a style preference.

## Real-World Use Case

Integer division and modulo are two of the most-used primitives in software, well beyond obvious arithmetic:

- **Pagination**: given `total_items` and `items_per_page`, `total_items // items_per_page` (plus a check on the remainder) computes the number of pages needed.
- **Hashing and bucketing**: hash tables map a hash value into a fixed number of buckets using `hash % num_buckets`; consistent hashing and load-balancer routing use the same idea to distribute requests across servers.
- **Time/unit conversions**: converting total seconds into hours/minutes/seconds (`seconds // 3600` for hours, `seconds % 3600` for the remainder to further divide) is exactly this quotient/remainder pattern chained together.
- **Cyclic/wraparound logic**: circular buffers, round-robin scheduling, and clock arithmetic (e.g. "what hour is it 50 hours from now on a 24-hour clock") all use modulo to wrap an index or value back into a fixed range.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input (dividend, divisor) | Expected | Result |
|---|---|---|---|
| `test_example_1` | (17, 5) | [3, 2] | ❌ `quotient_remainder_brute` fails (returns `[-3, 32]`); optimized passes |
| `test_example_2` | (3, 8) | [0, 3] | ✅ both pass (bug doesn't manifest at count=0) |
| `test_zero_dividend` | (0, 5) | [0, 0] | ✅ both pass (short-circuit path) |
| `test_exact_division` | (10, 5) | [2, 0] | ❌ brute fails (returns `[-2, 20]`); optimized passes |
| `test_dividend_equals_divisor` | (5, 5) | [1, 0] | ❌ brute fails (returns `[-1, 10]`); optimized passes |
| `test_negative_dividend_positive_divisor` | (-17, 5) | [-4, 3] | ✅ both pass (mixed-sign branch is correct) |
| `test_positive_dividend_negative_divisor` | (17, -5) | [-4, -3] | ✅ both pass (mixed-sign branch is correct) |
| `test_both_negative` | (-17, -5) | [3, -2] | ❌ brute fails (returns `[-3, -32]`); optimized passes |
| `test_divisor_of_one` | (12345, 1) | [12345, 0] | ❌ brute fails (returns `[-12345, 24690]`); optimized passes |
| `test_max_32bit_signed_dividend_optimized_only` | (2147483647, 2) | [1073741823, 1] | ✅ optimized only — `quotient_remainder_brute` isn't run here since it's O(dividend/divisor) and this input forces ~2^30 loop iterations (~80s observed), impractical for a routine test run |

**Net result: 5 of 10 tests fail, every one of them on `quotient_remainder_brute` for same-sign inputs** — this is the real bug described in the Solution section above, not a test-writing issue. `quotient_remainder_optimized` passes every case. 
Run with:
```bash
cd Variables_IO_Operators/quotient_and_remainder
python3 -m unittest -v
```
