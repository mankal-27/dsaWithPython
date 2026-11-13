# Count Digits in a Number

**Topic:** Basic Maths · **Difficulty:** Easy
**Files:** `cnt.py` (original solutions, commented) · `updt.py` (bug fixes + extra approach)

## Problem Statement

Given an integer `num`, return the number of digits in it.

| Input | Output |
|---|---|
| `12345` | `5` |
| `7` | `1` |
| `0` | `1` |
| `-123` | `3` (sign is not a digit) |

## Thought Process

The number of digits is the number of times you can chop off the last digit before nothing is left. In base 10, `num // 10` drops the last digit (`123 -> 12 -> 1 -> 0`). Count the chops and you have the answer.

That is a loop that runs once per digit. A second idea is that digit count is really the "size" of a number in base 10, and that is what a logarithm measures. `log10(1000) = 3` and 1000 has 4 digits. Any `n` in `[10^(k-1), 10^k)` has `k` digits and `floor(log10(n)) = k-1`. So `digits = floor(log10(n)) + 1`, with no loop.

Edge cases decide whether either version is correct:
- **0** has one digit, but the loop never runs and `log10(0)` is undefined.
- **Negatives** need `abs()` first. The loop `while num > 0` skips them.
- **Floating-point error.** `log10` returns a float. Near a power of ten (e.g. `999999999999999`) the float rounds up to the integer, so the formula is off by one.

## Brute Force: digit-chopping loop (`cnt.py -> count`)

```python
def count(self, num):
    if num == 0:          # 0 has one digit
        return 1
    count = 0
    while num > 0:
        num = num // 10   # drop last digit
        count = count + 1
    return count
```

**Bug:** a negative `num` fails `num > 0` immediately, so it returns `0`. `count(-123)` gives `0`, not `3`.

**Fix** (`updt.py -> count_fixed`): `num = abs(num)` before the loop.

## Optimized: logarithm (`cnt.py -> countOptimized`)

```python
def countOptimized(self, num):
    if num == 0:
        return 1
    return int(math.log10(abs(num)) + 1)
```

**Bug:** float rounding. `countOptimized(999999999999999)` returns `16` (correct is `15`), and `10**30 - 1` returns `31`.

**Fix** (`updt.py -> count_log_fixed`): use the log as an estimate, then check it with exact integer math:

```python
digits = int(math.log10(num)) + 1
if 10 ** (digits - 1) > num:   # estimate overshot
    digits -= 1
```

## Additional: string length (`updt.py -> count_str`)

```python
def count_str(self, num):
    return len(str(abs(num)))
```

This is the shortest and always correct, because Python ints have arbitrary precision and `str()` is exact. It costs O(d) extra memory for the temporary string. In interviews it is often disallowed because it skips the point of the exercise.

## Dry Runs

**Loop on `12345`:**

| Step | num before | num after `// 10` | count |
|---|---|---|---|
| 1 | 12345 | 1234 | 1 |
| 2 | 1234 | 123 | 2 |
| 3 | 123 | 12 | 3 |
| 4 | 12 | 1 | 4 |
| 5 | 1 | 0 | 5 |

Loop ends because `num = 0`, so the answer is **5**.

**Log on `12345`:** `log10(12345) ≈ 4.0915`, `+ 1 = 5.0915`, `int(...) = 5`.

**Log (original) on `999999999999999`:** `log10 ≈ 15.0` (rounded up from 14.99999...), `+ 1 = 16`, which is **wrong**. The fixed version gives `digits = 16`, sees `10**15 > 999999999999999`, and decrements to **15**.

**String on `-123`:** `abs -> 123`, `str -> "123"`, `len -> 3`.

## Complexity

| Approach | Time | Space | Notes |
|---|---|---|---|
| Loop (`count` / `count_fixed`) | O(d) | O(1) | one iteration per digit; d = digit count |
| Log (`countOptimized`) | O(1)* | O(1) | *fast, but wrong near powers of 10 for large n |
| Log fixed (`count_log_fixed`) | O(1)* | O(1) | one extra integer power check |
| String (`count_str`) | O(d) | O(d) | simplest and always correct |

Since d = log10(n), the loop is O(log n) in the value of n.

## Real-World Use Case

Digit counting is used when formatting and validating numbers. Examples are padding invoice or order IDs to a fixed width, checking that a card or phone number has the right length, and sizing columns in report and terminal output. It is also a building block for other digit problems such as palindrome numbers, Armstrong numbers and digit sums. In systems code the same idea sizes buffers for number-to-string conversion and estimates how many bits or characters a value needs.

## Running

```bash
python3 -c "from updt import Solution; print(Solution().count_fixed(-123))"
```
