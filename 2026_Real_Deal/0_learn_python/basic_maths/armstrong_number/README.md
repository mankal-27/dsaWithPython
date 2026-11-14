# Armstrong Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `armstrong_brute_force` and `armstrong_optimized` with tests |

## 1. Problem Statement

A number with `d` digits is an Armstrong number if the sum of each digit raised to the power `d` equals the number. Return `True`/`False`.

| Input | Output | Why |
|---|---|---|
| `153` | `True` | 1³ + 5³ + 3³ = 153 |
| `9474` | `True` | 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 |
| `154` | `False` | 1 + 125 + 64 = 190 |
| `0` | `True` | 0¹ = 0 |
| `-153` | `False` | negatives are not Armstrong |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `armstrong_brute_force` | `armstrong_optimized` |
| Idea | Convert to string; `len` gives digit count, power each char | Count digits with `// 10`, then peel digits with `% 10` |
| Why it works | Each char is one digit | Pure integer math, no string allocation |
| Extra | O(d) string memory | O(1) memory |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `math.log10(abs(number))` | `number = 0` raises `ValueError` (math domain error); 0 should be `True` | Handle 0 (digit count 1) |
| 2 | `sum = 0` | Shadows the built-in `sum()` | Rename to `total` |
| 3 | `math.pow(...)` | Returns a float, so large numbers lose precision and the `==` comparison can fail | Use integer `**` |
| 4 | `int(log10(n) + 1)` | Float rounding can miscount digits on big values | `len(str(n))` or a `// 10` loop |
| 5 | `import math` inside method | Re-imported on every call, poor style | Drop it (no longer needed) |
| 6 | Style | No trailing newline, `while(...)` parentheses | Clean formatting |

Negatives return `False` by accident (loop never runs, sum is 0), which is the right answer but should be explicit.

## 4. Dry Run

**Optimized on `153`:** digit count = 3

| Step | `remaining` | digit | digit³ | `total` |
|---|---|---|---|---|
| 1 | 153 | 3 | 27 | 27 |
| 2 | 15 | 5 | 125 | 152 |
| 3 | 1 | 1 | 1 | 153 |
| end | 0 | - | - | 153 == 153 -> **True** |

**Brute force on `154`:** `"154"` -> 1³ + 5³ + 4³ = 190 ≠ 154 -> **False**.

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d) | O(d) | String of `d` digits; one power per digit |
| Optimized | O(d) | O(1) | Two passes over digits with integer variables |

`d = log10(n) + 1`, so time is O(log n).
