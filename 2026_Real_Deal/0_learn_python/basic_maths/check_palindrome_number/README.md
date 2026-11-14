# Check Palindrome Number

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged, bug comments added) |
| `bug_free_solution.py` | `is_palindrome_brute_force` and `is_palindrome_optimized` with tests |

## 1. Problem Statement

Given an integer `number`, return `True` if it reads the same forwards and backwards, else `False`. Negative numbers are never palindromes.

| Input | Output | Why |
|---|---|---|
| `121` | `True` | same both ways |
| `123` | `False` | `321 != 123` |
| `10` | `False` | reversed is `01` = `1` |
| `-121` | `False` | `121-` is not `-121` |
| `0` | `True` | single digit |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `is_palindrome_brute_force` | `is_palindrome_optimized` |
| Idea | `str(n) == str(n)[::-1]` | Rebuild the number reversed with `% 10` and `// 10`, compare with the original |
| Why it works | A palindrome string equals its reverse | A palindrome number equals its digit-reversal |
| Edge handling | `n < 0` returns `False` | `n < 0` returns `False`; `0` skips the loop and equals itself |

Further idea: reverse only half the digits (stop when reversed >= remaining). Useful in languages with 32-bit overflow; Python ints are unbounded so full reversal is safe.

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `checkPalindrome(num)` | Missing `self`; `Solution().checkPalindrome(121)` raises `TypeError` | `def check_palindrome(self, num)` |
| 2 | `reverseNumb(num)` | Typo (`reverseNumber`) and called without `self.` so it is a `NameError` | `self.reverse_number(num)` |
| 3 | `while(num > 0)` | Negatives return `0`, so the `sign` variable is dead code. `-121` is `False` only by accident | Explicit `if num < 0: return False` |
| 4 | Style | camelCase, `while(...)` parentheses, no trailing newline | `snake_case`, no parentheses |

The digit-reversal loop itself is correct for non-negative input.

## 4. Dry Run

**Optimized on `121`:**

| Step | `number` | `last_digit` | `reversed_number` | `number` after `// 10` |
|---|---|---|---|---|
| 1 | 121 | 1 | 0·10+1 = 1 | 12 |
| 2 | 12 | 2 | 1·10+2 = 12 | 1 |
| 3 | 1 | 1 | 12·10+1 = 121 | 0 |

Reversed `121 == 121`, result **True**.

**Brute force on `123`:** `"123"[::-1]` is `"321"`, not equal, result **False**.

## 5. Complexity

Let `d` be the number of digits, so `d ≈ log10(n)`.

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(d) | O(d) | String and its reverse are d characters |
| Optimized | O(d) | O(1) | One loop pass, a few integer variables |

## 6. Real-World Use Case

Palindrome checks appear in symmetric ID/serial validation, DNA sequence analysis and as a building block for harder string/number problems.
