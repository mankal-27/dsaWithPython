# Count Number of Odd Digits in a Number

**Step:** Concept Basics → Basic Maths
**Difficulty:** Easy
**Link:** https://takeuforward.org/plus/dsa/problems (Basic Maths category — "Count number of odd digits in a number")
**File:** `Concept_Basics/cnt_odd_digits_num/ex1.py`

## Problem Statement

You are given an integer `n`. Return the number of odd digits present in the number.

The number will have no leading zeroes, except when the number is `0` itself.

**Example 1**
```
Input:  n = 5
Output: 1
Explanation: 5 is an odd digit.
```

**Example 2**
```
Input:  n = 25
Output: 1
Explanation: The only odd digit in 25 is 5.
```

**Example 3**
```
Input:  n = 15
Output: 2
```

**Constraints**
```
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
```

## Approach

Strip digits off `n` one at a time from the right (same digit-extraction pattern as "Count all digits"), and for each extracted digit check if it's odd (`digit % 2 != 0`). Increment a counter whenever it is.

```python
class Solution:
    def countOddDigits(self, n):
        count = 0
        if n == 0:
            return 0            # 0 itself is an even digit, so no odd digits

        while n > 0:
            digit = n % 10
            if digit % 2 != 0:
                count += 1
            n //= 10
        return count
```

- `n % 10` gives the last digit.
- `digit % 2 != 0` checks oddness (1, 3, 5, 7, 9 are odd).
- `n //= 10` drops the last digit and moves to the next one.

## Complexity

- **Time Complexity:** O(d), where `d` is the number of digits in `n` (equivalently O(log₁₀ n)) — one pass over each digit, constant work per digit.
- **Space Complexity:** O(1) — only a counter and the shrinking copy of `n`, no extra data structures.

## Dry Run

`n = 15`

| Iteration | n (start) | digit = n % 10 | odd? | count | n = n // 10 |
|---|---|---|---|---|---|
| 1 | 15 | 5 | yes | 1 | 1 |
| 2 | 1 | 1 | yes | 2 | 0 |
| 3 | 0 | — | loop exits (n > 0 false) | 2 | — |

Return `count = 2`. ✅ matches expected output (digits 1 and 5 are both odd).

**Second dry run — `n = 25`:**

| Iteration | n (start) | digit = n % 10 | odd? | count | n = n // 10 |
|---|---|---|---|---|---|
| 1 | 25 | 5 | yes | 1 | 2 |
| 2 | 2 | 2 | no | 1 | 0 |

Return `count = 1`. ✅ matches expected output (only `5` is odd; `2` is even).

**Edge case — `n = 0`:** returns `0` directly, since `0` is an even digit and there's nothing to iterate over.

## Real-World Use Case

Digit-parity checks like this generalize to "scan every digit and classify it" problems, which show up in:

- **Checksum / validation algorithms:** card-number validators (e.g. Luhn's algorithm) and ID checksums process each digit individually and apply parity/weighting rules to detect typos or fraud.
- **Data quality rules:** flagging numeric fields (phone numbers, serial numbers) that don't match an expected digit-composition pattern, e.g. "must contain at least one odd digit" as a simple randomness/format check.
- **Cryptography/PRNG sanity checks:** quick digit-distribution checks (odd vs even counts) are sometimes used as lightweight statistical tests on generated numbers.
- **Teaching/competitive programming building block:** this pattern (extract digit → classify → accumulate) is the base case for many "digit DP" problems (count numbers with k odd digits, sum of odd digits, etc.).

## Tests (to add once implemented)

Planned test cases for `test_ex1.py`, following the same style as `cnt_all_digits_num`:

| Test | Input | Expected |
|---|---|---|
| Example 1 | 5 | 1 |
| Example 2 | 25 | 1 |
| Example 3 | 15 | 2 |
| Zero edge case | 0 | 0 |
| All even digits | 2468 | 0 |
| All odd digits | 1357 | 4 |
| Max constraint | 5000 | 1 |
| Single odd digit | 9 | 1 |
| Single even digit | 8 | 0 |
