# Count Primes Till N

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (unchanged logic, bug comments added) |
| `bug_free_solution.py` | `count_primes_brute_force` and `count_primes_optimized` with tests |

## 1. Problem Statement

Given `n`, return how many prime numbers are in the range `[2, n]` (n inclusive).

| Input | Output | Why |
|---|---|---|
| `10` | `4` | 2, 3, 5, 7 |
| `7` | `4` | 2, 3, 5, 7 (n itself counts) |
| `2` | `1` | smallest prime |
| `1` | `0` | no primes |
| `0` / negative | `0` | no primes |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `count_primes_brute_force` | `count_primes_optimized` |
| Idea | Run `is_prime` (trial division to sqrt) on every number in `[2, n]` | Sieve of Eratosthenes: cross out multiples of each prime |
| Why it works | Directly applies the definition | Every composite has a prime factor ≤ sqrt(n), so crossing out multiples of primes up to sqrt(n) removes all composites |
| Care needed | `range(2, n + 1)` so `n` is included | Start crossing at `p * p`; handle `n < 2` |

## 3. Bugs Found in the Original Solution

| # | Where | Bug | Fix |
|---|---|---|---|
| 1 | `for num in range(number)` | End is exclusive, so `n` is never tested: `n = 7` returns 3 instead of 4 | `range(2, number + 1)` |
| 2 | `printPrimeNumberTillN` | Name says "print" but it returns a count | Rename to `count_primes_...` |
| 3 | `isPrime` | Correct (`<= 1` guard, `isqrt`, `+ 1`) | None |
| 4 | Performance | O(n sqrt n) is slow for big `n` | Sieve is O(n log log n) |
| 5 | Style | `if(...)` parentheses, camelCase names | PEP 8 formatting |

## 4. Dry Run

**Sieve for `n = 10`:** `isqrt(10) = 3`, start `[F, F, T, T, T, T, T, T, T, T, T]` (index 0..10)

| `number` | Prime? | Crossed out | Remaining True |
|---|---|---|---|
| 2 | yes | 4, 6, 8, 10 | 2, 3, 5, 7, 9 |
| 3 | yes | 9 | 2, 3, 5, 7 |

Count of True = **4**.

**Brute force on `n = 7`:** 2 ✓, 3 ✓, 4 ✗, 5 ✓, 6 ✗, 7 ✓ -> **4** (the original code stops at 6 and returns 3).

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n √n) | O(1) | n numbers, each checked in O(√n) |
| Optimized (sieve) | O(n log log n) | O(n) | Each composite is crossed out a few times; needs a boolean array |
