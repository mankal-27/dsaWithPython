# Sum of All Divisors of a Number

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/sum-of-divisors
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a positive integer n, return the sum of all of its divisors, including 1 and n itself.

A divisor of n is any positive integer that divides n with no remainder. For example, the divisors of 12 are 1, 2, 3, 4, 6, 12, and their sum is 28.

**Example 1**
```
Input:  n = 12
Output: 28
```

**Example 2**
```
Input:  n = 6
Output: 12
```

**Constraints**
```
1 <= n <= 10^6
The sum fits in a 32-bit integer at this range, but use a 64-bit accumulator to stay safe against larger inputs.
```

## How to Solve It — Thought Process

A divisor of `n` is any number that fits into it evenly — no remainder left over. The most literal way to find every one of them is to just try every candidate from `1` up to `n` and check: does `n` divide evenly by this candidate? If `n % i == 0`, add `i` to a running total. That's correct and about as easy to reason about as this problem gets, but it means checking up to a million candidates when `n` is at its largest allowed value (`10^6`) — most of which won't be divisors at all.

The insight that unlocks something faster is that divisors always come in pairs that multiply together to make `n`. Take `n = 12`: `1` pairs with `12` (`1 × 12 = 12`), `2` pairs with `6` (`2 × 6 = 12`), `3` pairs with `4` (`3 × 4 = 12`). Notice that in every pair, one of the two numbers is always less than or equal to `√n` and the other is always greater than or equal to `√n` — they straddle the square root. That means it's never necessary to search past `√n`: for every divisor `i` found up to the square root, its partner `n / i` is automatically a divisor too, and can just be computed directly instead of separately checked.

So instead of scanning all the way to `n`, the loop only needs to scan up to `√n`, testing `i * i <= n` as the stopping condition (this avoids needing an actual square-root function, and sidesteps any floating-point rounding concerns that computing `sqrt(n)` directly might introduce). Each time a divisor `i` is found, both `i` and its partner `n // i` get added — with one careful exception: when `n` is a perfect square (like `16 = 4 × 4`), the middle divisor pairs with itself, so `i` and `n // i` are the same number, and it must be added only once, not twice.

This turns an O(n) scan into an O(√n) scan — for `n = 10^6`, that's the difference between roughly a million checks and roughly a thousand, which is the kind of improvement that actually matters at that scale rather than being a minor constant-factor tweak.

## Brute Force Solution — Linear Scan

```python
class Solution:
    def sum_of_divisors_linear_scan(self, n):
        total = 0
        for i in range(1, n+1):
            if(n % i == 0):
                total = total + i
        return total
```

## Optimized Solution — Scan to Square Root

```python
    def sum_of_divisors_sqrt_scan(self, n):
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                partner = n // i
                total = total + i
                if partner != i :
                    total += partner
            i += 1
        return total
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().sum_of_divisors_sqrt_scan(n)`), not on the class directly.

### Algorithm — Linear Scan
1. Initialize `total = 0`.
2. Loop `i` from `1` to `n` inclusive: if `n % i == 0`, add `i` to `total`.
3. Return `total`.

### Algorithm — Scan to Square Root
1. Initialize `total = 0` and `i = 1`.
2. While `i * i <= n`: if `n % i == 0`, add `i` to `total`, compute `partner = n // i`, and add `partner` too unless `partner == i`.
3. Increment `i` and repeat.
4. Return `total`.

## Dry Run

### Linear Scan — `n = 6`

| `i` | `6 % i == 0`? | `total` after |
|---|---|---|
| 1 | Yes | 1 |
| 2 | Yes | 3 |
| 3 | Yes | 6 |
| 4 | No | 6 |
| 5 | No | 6 |
| 6 | Yes | 12 |

Return `12`. ✅ matches expected output.

### Scan to Square Root — `n = 12`

| `i` | `i*i <= 12`? | `12 % i == 0`? | `partner = 12 // i` | `partner != i`? | `total` after |
|---|---|---|---|---|---|
| 1 | Yes (1≤12) | Yes | 12 | Yes → add both | 1 + 12 = 13 |
| 2 | Yes (4≤12) | Yes | 6 | Yes → add both | 13 + 2 + 6 = 21 |
| 3 | Yes (9≤12) | Yes | 4 | Yes → add both | 21 + 3 + 4 = 28 |
| 4 | No (16>12) | — loop exits | — | — | 28 |

Return `28`. ✅ matches expected output.

**Perfect-square dry run — `n = 16`:** at `i = 4`, `4 * 4 = 16 <= 16` so the loop runs; `16 % 4 == 0` and `partner = 16 // 4 = 4`, so `partner == i`, meaning `4` is added only **once** (not twice). Full trace: `i=1` → add `1, 16` (total 17); `i=2` → add `2, 8` (total 27); `i=3` → `16 % 3 != 0`, skip; `i=4` → add `4` only (total 31); `i=5`, `5*5=25 > 16`, loop exits. Return `31` (`1+2+4+8+16 = 31`), correctly counting the middle divisor `4` just once.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Linear Scan | O(n) | O(1) | Checks every candidate from 1 to n; only the running total is stored. |
| Scan to Square Root | O(√n) | O(1) | Checks candidates only up to √n, computing each divisor's partner directly instead of searching for it. |

For `n = 10^6`, Linear Scan does up to a million modulo checks while Scan to Square Root does about a thousand — a difference that grows every time `n` grows, unlike a constant-factor improvement.

## Real-World Use Case

Finding and summing divisors, and the square-root-bound scanning trick specifically, come up in a few recognizable places:

- **Number theory utilities** — perfect number checks (a number equal to the sum of its divisors excluding itself, like 6 = 1+2+3), abundant/deficient number classification, and GCD/factorization-adjacent tools all build on divisor enumeration.
- **Cryptography-adjacent factoring** — trial division up to `√n` is the same square-root bound used as a first-pass primality/factorization check before falling back to more sophisticated algorithms for large numbers.
- **Scheduling and resource allocation** — finding all ways to evenly divide a quantity (e.g. "which grid sizes evenly tile this area," "which batch sizes evenly divide this workload") is directly a divisor-enumeration problem.
- **Teaching the square-root optimization pattern** — the "search only needs to go to √n because factors pair up around it" insight recurs across many problems (checking primality, finding all factor pairs, certain search-space-reduction techniques), so this problem is a clean first example of a pattern used more broadly.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails:

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | n=12 | 28 |
| `test_example_2` | n=6 | 12 |
| `test_min_boundary` | n=1 | 1 |
| `test_prime` | n=13 | 14 (1 + 13) |
| `test_perfect_square` | n=16 | 31 (exercises the middle-divisor double-counting guard at i=4) |
| `test_perfect_square_larger` | n=25 | 31 (a second perfect square, 5×5, confirming the guard generalizes) |
| `test_max_constraint` | n=1000000 | 2480437 (largest value allowed by the stated constraints) |

All 7 tests (14 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation.

Run with:
```bash
cd Loops_Iteration/sum_of_divisors
python3 -m unittest -v
```
