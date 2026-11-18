# Check Palindrome

**Topic:** Basic String · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (bugs marked in comments) |
| `bug_free_solution.py` | `check_palindrome_brute_force` and `check_palindrome_optimized` with tests |

## 1. Problem Statement

Given a string, return `True` if it reads the same forwards and backwards, else `False`.

| Input | Output | Why |
|---|---|---|
| `"racecar"` | `True` | mirror image |
| `"abba"` | `True` | even length, pairs match |
| `"hello"` | `False` | `h != o` |
| `"a"` / `""` | `True` / `True` | nothing to mismatch |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `check_palindrome_brute_force` | `check_palindrome_optimized` |
| Idea | Build the reversed string, compare with the original | Two pointers from both ends, compare pairs moving inward |
| Why it works | A palindrome equals its reverse | Mirror positions must hold equal characters |
| Care needed | `range(len-1, -1, -1)` | `right = len - 1`; loop while `left < right`; return `True` at the end |

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | Final `return False` should be `return True`; every input, even `"racecar"`, returns `False` | Bug | `return True` after the loop |
| 2 | Parameter named `str` shadows the built-in | Style | rename to `text` |
| 3 | `while(...)`, `if(...)`, `left , right` spacing, camelCase name | Style | `while ...:`, `left, right`, snake_case |

The two-pointer logic itself is correct.

## 4. Dry Run

**Optimized, `"racecar"`:**

| Step | `left` | `right` | Compare | Result |
|---|---|---|---|---|
| 1 | 0 | 6 | r == r | continue |
| 2 | 1 | 5 | a == a | continue |
| 3 | 2 | 4 | c == c | continue |
| 4 | 3 | 3 | stop (`left < right` false) | return `True` |

**Optimized, `"hello"`:** step 1 compares `h` vs `o`, mismatch, return `False`.

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(n) | builds a reversed copy of n chars (repeated `+=` may cost more in theory, CPython optimizes it) |
| Optimized | O(n) | O(1) | at most n/2 comparisons, only two indices |
