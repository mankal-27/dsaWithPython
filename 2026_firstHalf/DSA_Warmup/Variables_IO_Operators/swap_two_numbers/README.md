# Swap Two Numbers

**Topic:** Variables, I/O & Operators
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/swap-two-numbers
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given two numbers `a` and `b`, swap their values and return the result as a two-element array `[b, a]`.

In other words, the value that started in `a` should appear in the second position, and the value that started in `b` should appear in the first position.

**Example 1**
```
Input:  a = 5, b = 7
Output: [7, 5]
```

**Example 2**
```
Input:  a = -3, b = 9
Output: [9, -3]
```

**Constraints**
```
Both a and b fit in the 32-bit signed integer range: -2^31 <= a, b <= 2^31 - 1.
The values may be negative, zero, or equal to each other.
```

## Solution

Implemented as a `Solution` class with four swap variants, each demonstrating a different technique:

```python
class Solution:
    def swap_two_num_with_built_in_method(self, a, b):
        a, b = b, a
        return [a, b]

    def swap_two_num_with_temp(self, a, b):
        temp = a
        a = b
        b = temp
        return [a, b]

    def swap_two_num_with_arithmetic(self, a, b):
        a = a + b     # a now holds the sum of both original values
        b = a - b     # subtract original b from the sum -> b becomes original a
        a = a - b     # subtract new b (original a) from the sum -> a becomes original b
        return [a, b]

    def swap_two_num_with_or(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return [a, b]
```

> **Note on `self` / calling convention:** these are regular instance methods — `self` is the parameter Python automatically binds to whichever object the method is called through. Calling `Solution().swap_two_num_with_temp(5, 7)` is equivalent to `Solution.swap_two_num_with_temp(instance, 5, 7)` under the hood, so `self` is what catches that auto-inserted instance. That means these methods must be called **on an instance** — `Solution().swap_two_num_with_temp(a, b)` — not on the class directly. `Solution.swap_two_num_with_temp(5, 7)` would bind `5` to `self` and `7` to `a`, leaving `b` unfilled and raising `TypeError: missing 1 required positional argument: 'b'`. None of these methods actually use `self` (no `self.something`), so the strictly "correct" version would mark them `@staticmethod` instead — but `self` works fine and matches the common `class Solution` convention used on most coding-practice platforms. The tests below instantiate `Solution()` once and call every method on that instance.

**Brute Force (most straightforward): `swap_two_num_with_built_in_method`** — uses Python's native tuple-unpacking assignment (`a, b = b, a`), which is the idiomatic Python way to swap and needs no extra reasoning about intermediate state.

**Optimized / instructive variants:**
- `swap_two_num_with_temp` — the classic temporary-variable swap (language-agnostic, no overflow risk).
- `swap_two_num_with_arithmetic` — swaps using addition/subtraction only, no extra variable.
- `swap_two_num_with_or` — swaps using XOR only, no extra variable, and (in fixed-width-integer languages) no overflow risk either, unlike the arithmetic version.

## Dry Run

### `swap_two_num_with_temp` — `a = 5, b = 7`

| Step | Operation | a | b | temp |
|---|---|---|---|---|
| start | — | 5 | 7 | — |
| 1 | `temp = a` | 5 | 7 | 5 |
| 2 | `a = b` | 7 | 7 | 5 |
| 3 | `b = temp` | 7 | 5 | 5 |

Return `[a, b]` = `[7, 5]`. ✅ matches expected output.

### `swap_two_num_with_arithmetic` — `a = 5, b = 7`

| Step | Operation | a | b |
|---|---|---|---|
| start | — | 5 | 7 |
| 1 | `a = a + b` (5 + 7) | 12 | 7 |
| 2 | `b = a - b` (12 - 7) | 12 | 5 |
| 3 | `a = a - b` (12 - 5) | 7 | 5 |

Return `[a, b]` = `[7, 5]`. ✅ matches expected output.

**Negative-number dry run — `a = -3, b = 9`:**

| Step | Operation | a | b |
|---|---|---|---|
| start | — | -3 | 9 |
| 1 | `a = a + b` (-3 + 9) | 6 | 9 |
| 2 | `b = a - b` (6 - 9) | 6 | -3 |
| 3 | `a = a - b` (6 - (-3)) | 9 | -3 |

Return `[a, b]` = `[9, -3]`. ✅ matches expected output — confirms negatives work without special-casing.

### `swap_two_num_with_or` (XOR) — `a = 5 (0b101), b = 7 (0b111)`

| Step | Operation | a (binary) | b (binary) |
|---|---|---|---|
| start | — | 101 | 111 |
| 1 | `a = a ^ b` | 010 | 111 |
| 2 | `b = a ^ b` (010 ^ 111) | 010 | 101 |
| 3 | `a = a ^ b` (010 ^ 101) | 111 | 101 |

Return `[a, b]` = `[7, 5]`. ✅ matches expected output.

### `swap_two_num_with_built_in_method` — `a = 5, b = 7`

Python evaluates the right-hand side `(b, a)` = `(7, 5)` as a tuple *before* assigning, so both variables update simultaneously — no intermediate step to trace. Result: `[7, 5]` in one line. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Built-in tuple unpacking (`a, b = b, a`) | O(1) | O(1) | Idiomatic Python; a temporary tuple is created internally but it's still constant size. |
| Temp variable | O(1) | O(1) | Fixed number of assignments; one extra variable (`temp`) used regardless of input size. |
| Arithmetic (+/-) | O(1) | O(1) | Fixed number of arithmetic ops; no extra variable. Can overflow in fixed-width-integer languages (not an issue in Python, which has arbitrary-precision ints). |
| XOR (^) | O(1) | O(1) | Fixed number of bitwise ops; no extra variable and no overflow risk in any language — the safest "no temp variable" choice. |

All four are O(1) time and space in the big-O sense; the practical differences are readability, whether an extra variable is used, and overflow safety in languages with fixed-width integers.

## Real-World Use Case

Swapping is one of the most-used micro-operations in software, even though it rarely appears as a standalone feature:

- **Sorting algorithms** (bubble sort, selection sort, quicksort's partition step) repeatedly swap two array elements to move them into order.
- **In-place array/list rearrangement** — reversing an array, rotating a list, or shuffling (Fisher-Yates) all swap pairs of elements without allocating new memory.
- **Register allocation in compilers/CPUs** — swapping the contents of two registers without a spare one is a classic low-level trick (this is exactly where the XOR-swap idea comes from).
- **State/variable exchange in algorithms** — two-pointer techniques (e.g. swapping `left`/`right` pointer targets) and graph algorithms that swap node labels during traversal both rely on this basic operation.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs each of the 4 methods against the same set of inputs using `subTest`, so a single test method reports which specific variant fails if one does:

| Test | Input (a, b) | Expected |
|---|---|---|
| `test_example_1` | (5, 7) | [7, 5] |
| `test_example_2_negative` | (-3, 9) | [9, -3] |
| `test_equal_values` | (4, 4) | [4, 4] |
| `test_one_value_zero` | (0, 6) | [6, 0] |
| `test_both_zero` | (0, 0) | [0, 0] |
| `test_both_negative` | (-8, -2) | [-2, -8] |
| `test_max_32bit_signed_boundary` | (2147483647, -2147483648) | [-2147483648, 2147483647] |

Each test checks all 4 methods (`swap_two_num_with_built_in_method`, `swap_two_num_with_temp`, `swap_two_num_with_arithmetic`, `swap_two_num_with_or`) against the expected result.

Run with:
```bash
cd Variables_IO_Operators/swap_two_numbers
python3 -m unittest -v
```

All 7 tests (28 sub-assertions across the 4 methods) pass against the current `sol.py`.
