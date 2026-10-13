# Count Digits in an Integer

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/count-digits
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

**Note:** This overlaps with `Concept_Basics/cnt_all_digits_num` (an earlier, takeuforward.org-based version of the same core idea), but this version's constraints are meaningfully harder — it spans the full 32-bit signed range including negative numbers and the `INT_MIN` overflow edge case, and its source presents three distinct approaches instead of one — so it gets its own folder here rather than being folded into the earlier one.

## Problem Statement

Given an integer n, return the number of digits in n.

Count the digits of the absolute value, so the sign of a negative number does not count. The number 0 has 1 digit.

**Example 1**
```
Input:  n = 12345
Output: 5
```

**Example 2**
```
Input:  n = -789
Output: 3
```

**Constraints**
```
-2^31 <= n <= 2^31 - 1
n may be negative, zero, or positive.
```

## How to Solve It — Thought Process

"How many digits does this number have" is really asking "how many decimal places does it take to write down its magnitude." Two values need to be handled with a bit of care before diving into any technique: zero, and the sign.

Zero is a special case no matter which approach is used — it's written with exactly one symbol (`0`), so the answer is `1`, but zero has no leading digit to "strip away" the way every other number does, so any digit-stripping approach needs to check for it up front rather than expect the general logic to produce `1` naturally.

The sign is the second thing to get right: a negative number's minus sign isn't a digit, so `-789` should count as `3` digits, not 4. The cleanest way to sidestep sign-handling entirely is to work with the number's magnitude — but that's where a subtle trap lives. The most negative 32-bit integer, `-2147483648`, has no positive counterpart that fits back into the same 32-bit range (`2147483648` is one more than the largest positive `int`, `2147483647`). In a fixed-width-integer language this makes naively negating or taking `abs()` of that one specific value overflow and wrap back around to something wrong. Python doesn't have that problem — its integers grow arbitrarily large, so `abs(-2147483648)` is simply `2147483648`, no overflow, no special case needed — but it's still worth knowing about, since the technique used here (dividing toward zero rather than negating first) is the same one that stays safe in languages that do have fixed-width integers.

With those two things noted, the most direct way to count digits is to physically strip them off one at a time: integer division by 10 removes the last digit and shifts everything else one place to the right (`12345 → 1234 → 123 → 12 → 1 → 0`), and integer division in Python already rounds toward negative infinity, but critically it still drives a negative number toward `0` in the same number of steps as its positive counterpart would take (`-789 → -78 → -7 → 0`, three steps, matching `789`'s three steps) — so working with the magnitude via `abs()` up front keeps this simple and correct either way. Counting how many divisions it takes to reach `0` (with `0` itself handled as an immediate special case returning `1`) gives the digit count directly.

A completely different way to get the same number sidesteps arithmetic altogether: convert the integer to its string representation and just measure the string's length, stripping off a leading `-` first if present. This trades a division loop for a string-length lookup, and it's arguably the most "honest" definition of the problem — digit count really is "how many characters does this take to print" — though it does allocate a string proportional to the digit count rather than using constant extra space.

There's a third option that avoids looping or string-building entirely: math. A `d`-digit number sits somewhere in the range `10^(d-1)` to `10^d - 1` (e.g. every 3-digit number is between `100` and `999`), and `log10` of any value in that range lands strictly between `d - 1` and `d`. So `floor(log10(|n|)) + 1` recovers `d` directly, in constant time, with `n = 0` handled as its own special case (since `log10(0)` is undefined). The catch is that this relies on floating-point arithmetic, which is not always exact: right at an exact power of 10 (like `1000`), `log10` can compute a value that's a hair below the true integer (e.g. `2.9999999999996` instead of `3.0`), and flooring that gives the wrong digit count by one. That makes this approach the fastest on paper but the riskiest in practice — worth knowing, but not the default choice for a problem where correctness at every boundary value matters.

## Brute Force Solution — Repeated Division

```python
import math

class Solution:
    def count_digits_repeated_division(self, n):
        n = abs(n)
        if(n == 0):
            return 1
        count = 0
        while(n != 0):
            n = n // 10
            count = count + 1
        return count
```

## Optimized Solution — Convert to String

```python
    def count_digits_string_length(self, n):
        s = str(n)
        if s.startswith("-"):
            s = s[1:]
        return len(s)
```

## Additional Solution — Logarithm (fast, but has a floating-point caveat)

```python
    def count_digits_logarithm(self, n):
        n = abs(n)
        if(n == 0):
            return 1
        return math.floor(math.log10(n)) + 1
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().count_digits_string_length(n)`), not on the class directly.
>
> **Caveat on the Logarithm approach:** `log10` uses floating-point math, and floating-point values near an exact power of 10 (like `1000`, `10000`, ...) can come out a hair below the true value due to rounding, which flips the `floor(...)` result down by one and produces a wrong count exactly at those boundaries. The Repeated Division and Convert to String approaches don't have this risk, since they never do floating-point arithmetic. In practice, this hasn't been observed to actually occur for any power of 10 within this problem's 32-bit range in Python (verified directly: `10` through `10^9` all compute correctly) — but the risk is real and platform/language-dependent, so it's still presented as an *additional* approach worth knowing rather than the recommended optimized one, despite being O(1).

### Algorithm — Repeated Division
1. If `n` is `0`, return `1`.
2. Take the absolute value of `n`.
3. Loop: while `n != 0`, integer-divide `n` by `10` and increment a counter.
4. Return the counter.

### Algorithm — Convert to String
1. Convert `n` to its string form.
2. If the string starts with `-`, strip that character.
3. Return the length of the remaining string.

### Algorithm — Logarithm
1. If `n` is `0`, return `1`.
2. Compute `floor(log10(abs(n))) + 1`.
3. Return that value.

## Dry Run

### Repeated Division — `n = -789`

| Step | `n` (start) | `n != 0`? | `n //= 10` | `count` |
|---|---|---|---|---|
| — | `abs(-789) = 789` | — | — | 0 |
| 1 | 789 | Yes | 78 | 1 |
| 2 | 78 | Yes | 7 | 2 |
| 3 | 7 | Yes | 0 | 3 |
| 4 | 0 | No → loop exits | — | 3 |

Return `3`. ✅ matches expected output.

### Convert to String — `n = -789`

| Step | Operation | Value |
|---|---|---|
| 1 | `s = str(-789)` | `"-789"` |
| 2 | `s.startswith("-")` → strip it | `"789"` |
| 3 | `len(s)` | `3` |

Return `3`. ✅ matches expected output.

### Logarithm — `n = 12345`

| Step | Operation | Value |
|---|---|---|
| 1 | `abs(12345)` | `12345` |
| 2 | `math.log10(12345)` | `≈ 4.0915` |
| 3 | `math.floor(4.0915) + 1` | `4 + 1 = 5` |

Return `5`. ✅ matches expected output.

**Edge case worth naming (not run above, see the caveat):** at `n = 1000`, the mathematically exact `log10(1000)` is `3.0`, but floating-point computation can produce something like `2.9999999999996`, whose `floor` is `2`, giving `2 + 1 = 3` — the wrong answer (`1000` has 4 digits). The other two approaches don't have this risk.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Repeated Division | O(d) = O(log n) | O(1) | One loop iteration per digit; only the counter and shrinking copy of `n` use extra space. |
| Convert to String | O(d) = O(log n) | O(d) | Building the string and measuring it both scale with digit count; the string itself is the extra space. |
| Logarithm | O(1) | O(1) | A single log10 and floor — constant time and space, but see the floating-point caveat above. |

Logarithm is the only approach whose time complexity doesn't depend on the input size, but its correctness caveat at exact powers of 10 makes Repeated Division the safer default; Convert to String is a reasonable middle ground that trades a small amount of extra space for code that reads as directly as the problem statement.

## Real-World Use Case

Counting digits is a small building block that shows up inside larger systems rather than as a standalone feature:

- **Input validation** — checking that a PIN, OTP, account number, or postal code has the expected number of digits before accepting it.
- **UI/formatting** — deciding how many placeholder boxes to render for an OTP input, or how much to pad a number with leading zeros (e.g. invoice numbers like `INV-00042`).
- **Digit DP / competitive programming** — many "digit DP" problems (count numbers with a given digit sum, count numbers without repeated digits, etc.) first need to know how many digits a number has to size a DP table.
- **Number formatting libraries** — functions that decide whether to display a number in full, abbreviate it (`1.2K`, `3.4M`), or choose a column width in a table/report use digit count internally, and often need to handle the same negative-number and edge-value cases discussed here.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs all three methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | n=12345 | 5 |
| `test_example_2_negative` | n=-789 | 3 |
| `test_zero` | n=0 | 1 |
| `test_single_digit` | n=7 | 1 |
| `test_min_32bit_signed_int` | n=-2147483648 | 10 |
| `test_max_32bit_signed_int` | n=2147483647 | 10 |
| `test_exact_power_of_ten` | n=1000 | 4 (also exercises the Logarithm approach's floating-point caveat, which doesn't actually manifest here) |

All 7 tests (21 sub-assertions across the 3 methods) pass against the current `sol.py`.

Run with:
```bash
cd Loops_Iteration/count_digits
python3 -m unittest -v
```
