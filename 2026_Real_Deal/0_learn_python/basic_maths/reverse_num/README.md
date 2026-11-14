# Reverse Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged, bug comments added) |
| `bug_free_solution.py` | `reverse_num_brute_force` and `reverse_num_optimized` with tests |

## 1. Problem Statement

Given an integer `number`, return it with its digits reversed. Keep the sign. Trailing zeros vanish because they become leading zeros.

| Input | Output | Why |
|---|---|---|
| `123` | `321` | digits flipped |
| `120` | `21` | `021` is `21` |
| `0` | `0` | nothing to flip |
| `-123` | `-321` | sign kept |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `reverse_num_brute_force` | `reverse_num_optimized` |
| Idea | `str(abs(n))[::-1]`, then `int()` | Pop the last digit with `% 10`, push it with `rev * 10 + digit` |
| Why it works | Slicing reverses characters; `int()` drops leading zeros | `% 10` isolates a digit, `// 10` removes it, `* 10` shifts the result left |
| Edge handling | Sign stored separately | Sign stored separately; `0` skips the loop and returns 0 |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `reverse_num(num)` | Missing `self`; `Solution().reverse_num(123)` raises `TypeError` | `def reverse_num(self, num)` |
| 2 | `while(num > 0)` | Negatives skip the loop, so `-123` returns `0` | Store the sign, work on `abs(num)` |
| 3 | `reverseNumWithMethod(num)` | Missing `self` | Add `self` |
| 4 | `reversed(num)` | `reversed(123)` raises `TypeError`; on a string it returns an iterator, not a number | `int(str(num)[::-1])` |
| 5 | Style | camelCase, `while(...)` parentheses | `snake_case`, no parentheses |

The loop logic itself is correct for non-negative input.

## 4. Dry Run

**Optimized on `123`:**

| Step | `number` | `last_digit` | `reversed_number` | `number` after `// 10` |
|---|---|---|---|---|
| 1 | 123 | 3 | 0·10+3 = 3 | 12 |
| 2 | 12 | 2 | 3·10+2 = 32 | 1 |
| 3 | 1 | 1 | 32·10+1 = 321 | 0 |

Loop stops at `number == 0`. Result: **321**.

**Brute force on `-120`:** sign `-1`, `"120"[::-1]` is `"021"`, `int` gives `21`, result **-21**.

## 5. Complexity

Let `d` be the number of digits, so `d ≈ log10(n)`.

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d) | O(d) | String and its reverse are d characters |
| Optimized | O(d) | O(1) | One loop pass, three integer variables |

## 6. Real-World Use Case

Digit reversal is the core of palindrome-number checks, and shows up in hashing, number-base conversion and the Luhn checksum.
