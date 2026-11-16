# GCD of Two Numbers

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `gcd_brute_force` and `gcd_optimized` with tests |

## 1. Problem Statement

Given two integers, return their greatest common divisor (the largest number that divides both).

| Input | Output | Why |
|---|---|---|
| `12, 18` | `6` | divisors of both: 1, 2, 3, 6 |
| `4, 8` | `4` | the smaller number can itself be the gcd |
| `7, 13` | `1` | coprime |
| `0, 9` | `9` | gcd(a, 0) = a |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `gcd_brute_force` | `gcd_optimized` |
| Idea | Try every candidate from `min(a, b)` down to 1, return the first that divides both | Euclid: replace `(a, b)` by `(b, a % b)` until `b` is 0 |
| Why it works | Gcd can't exceed the smaller number; going downward, the first hit is the largest | gcd(a, b) = gcd(b, a % b), since any common divisor of a and b also divides a % b |
| Care needed | Include `min` itself (`range(min, 0, -1)`); use `and`, handle 0 | Handle negatives with `abs` |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `gcd`: `range(1, min(...))` | End is exclusive, so `min` is never tried: `gcd(4, 8)` returns 2 | `range(1, min + 1)` |
| 2 | `gcd` and `gcd1`: `a % i == 0 & b % i == 0` | `&` binds tighter than `==`, giving a chained comparison that only checks `num1 % i` | Use `and` |
| 3 | `gcd1`: `range(min, 1)` | No `-1` step, so the range is empty and the method returns `None` | `range(min, 0, -1)` |
| 4 | `gcd1`: stop value `1` | Even with a step, 1 would be excluded | Stop at `0` |
| 5 | Both | No handling of `0` or negatives | Use `abs`, return the other number when one is 0 |
| 6 | Style | `if(...)` parentheses, camelCase-ish names | PEP 8 formatting |

## 4. Dry Run

**Brute force, `gcd(12, 18)`:** start at `min = 12`

| `divisor` | 12 % d | 18 % d | Both 0? |
|---|---|---|---|
| 12 | 0 | 6 | no |
| 11 .. 7 | nonzero | - | no |
| 6 | 0 | 0 | **yes -> return 6** |

**Euclid, `gcd(48, 180)`:**

| Step | `num1` | `num2` | `num1 % num2` |
|---|---|---|---|
| 1 | 48 | 180 | 48 |
| 2 | 180 | 48 | 36 |
| 3 | 48 | 36 | 12 |
| 4 | 36 | 12 | 0 |
| 5 | 12 | 0 | stop -> **12** |

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(min(a, b)) | O(1) | At most `min` candidates, each checked in O(1) |
| Optimized (Euclid) | O(log min(a, b)) | O(1) | The remainder at least halves every two steps |
