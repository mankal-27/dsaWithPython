# LCM of Two Numbers

**Topic:** Basic Maths · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (empty so far) |
| `bug_free_solution.py` | `lcm_brute_force` and `lcm_optimized` with tests |

## 1. Problem Statement

Given two integers, return their least common multiple (the smallest positive number divisible by both).

| Input | Output | Why |
|---|---|---|
| `4, 6` | `12` | multiples of 4: 4, 8, 12; of 6: 6, 12 |
| `7, 13` | `91` | coprime, so the product |
| `4, 8` | `8` | the larger can itself be the lcm |
| `0, 9` | `0` | lcm with 0 is defined as 0 |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `lcm_brute_force` | `lcm_optimized` |
| Idea | Walk the multiples of the larger number until one is divisible by the smaller | `lcm(a, b) = a / gcd(a, b) * b` using Euclid for gcd |
| Why it works | The lcm is a multiple of both, so it is a multiple of the larger | `gcd * lcm = a * b` |
| Care needed | Handle 0 (infinite loop otherwise), use `abs` | Divide before multiplying to keep numbers small; handle 0 |

## 3. Common Bugs to Avoid

| # | Bug | Fix |
|---|---|---|
| 1 | Loop `range(1, a * b)` excludes `a * b`, so coprime inputs fail | Include `a * b` or use a `while` loop |
| 2 | Input `0` makes the brute-force loop run forever | Return 0 early |
| 3 | Using `&` instead of `and` in the divisibility check | Use `and` |
| 4 | Negatives give a negative lcm | Use `abs` |

## 4. Dry Run

**Brute force, `lcm(4, 6)`:** larger = 6

| `candidate` | % 4 | % 6 | Both 0? |
|---|---|---|---|
| 6 | 2 | 0 | no |
| 12 | 0 | 0 | **yes -> 12** |

**Optimized, `lcm(12, 18)`:** gcd = 6, so `12 // 6 * 18 = 36`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(a * b / gcd) at worst, i.e. up to `min(a, b)` steps | O(1) | Each step jumps by the larger number; at most `smaller / gcd` jumps |
| Optimized | O(log min(a, b)) | O(1) | Dominated by Euclid's gcd |
