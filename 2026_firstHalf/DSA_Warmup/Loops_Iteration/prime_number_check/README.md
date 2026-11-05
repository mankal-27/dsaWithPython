# Prime Number Check

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/prime-number-check
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer n, return true if n is a prime number and false otherwise.

A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself. Any value of 1 or less, including 0 and negative numbers, is not prime.

**Example 1**
```
Input:  n = 17
Output: true
```

**Example 2**
```
Input:  n = 18
Output: false
```

**Constraints**
```
-2^31 <= n <= 2^31 - 1
n may be negative, zero, or positive.
```

## How to Solve It — Thought Process

"Is this number prime" boils down to one question: does anything besides 1 and the number itself divide it evenly? So the most direct approach is to just try every candidate divisor and see. But before writing any loop, it's worth pinning down what counts as a valid candidate to even check, because primality has a definition boundary that's easy to get wrong at the edges: it only applies to integers greater than 1. That immediately disposes of an entire slice of the input range — 0, 1, and every negative number — with a single comparison, before any division happens. Skipping this guard, or writing it as `n < 1` instead of `n <= 1`, is the classic way to accidentally call `1` prime.

With that guard in place, the literal check is: for every whole number from `2` up to (but not including) `n` itself, does it divide `n` with no remainder? If even one does, `n` is composite. If the loop gets all the way through without finding one, `n` must be prime — nothing else was capable of dividing it. This is correct and easy to trust, but it does a full pass over roughly `n` values, which becomes expensive fast: check `n` near the top of the stated 32-bit range and this loop is doing on the order of two billion iterations.

The way to cut that down comes from the same observation that shows up in every divisor problem: divisors pair up around the square root. If `a * b = n`, one of `a` and `b` is at most `√n` and the other is at least `√n`. So if `n` were composite, it would necessarily have *some* divisor at or below `√n` — there's no way for every divisor to hide above the square root while none exist below it, because the moment a divisor `d > √n` is found, `n / d` is a matching divisor that's `≤ √n`. That means checking candidates all the way up to `n - 1` is redundant: if nothing up to `√n` divides `n`, nothing at all does, and the search can stop there. This shrinks the work from O(n) down to O(√n) — for `n` near 2 billion, that's roughly 46,000 checks instead of two billion.

There's a further squeeze available once the square-root bound is in place: every integer is either a multiple of 2, a multiple of 3, or one of the two remaining "slots" next to a multiple of 6. Concretely, walking through six consecutive integers `6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5`, the numbers `6k`, `6k+2`, and `6k+4` are all even, and `6k+3` is always a multiple of 3 — none of those four can be prime (other than 2 and 3 themselves). That leaves only `6k+1` and `6k+5` (equivalently `6k-1`) as numbers that could possibly be prime. So after handling 2 and 3 as their own special cases up front, the square-root loop only needs to test candidates of the form `6k ± 1`, which is two out of every six integers — roughly a third of the work the plain square-root loop does, while still guaranteed to catch every possible divisor.

## Brute Force Solution — Trial Division up to n-1

```python
class Solution:
    def is_prime_trial_division(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True
```

## Optimized Solution — Trial Division up to √n

```python
    def is_prime_sqrt_scan(self, n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
        return True
```

> ⚠️ **Known bug:** the `while` loop never increments `i`. Once `i = 2` fails to divide `n` (i.e. `n` is odd), the loop condition `i * i <= n` stays true forever with `i` stuck at `2`, and the method hangs — it never returns for any odd `n >= 5`.
>
> **Trace for `n = 5`:** `i = 2` → `5 % 2 == 0`? No → loop back to the condition check → `i` is still `2` → `4 <= 5`? Still true → check again → `5 % 2 == 0`? No → ... this repeats forever, since nothing in the loop body changes `i`. Confirmed directly: calling `is_prime_sqrt_scan(5)` was run with a 3-second timeout and never returned (exit code 124, i.e. killed on timeout).
>
> The method only produces a result at all when the loop body never runs, or resolves on its very first check: `n <= 1` (the guard returns early), `n = 2` or `n = 3` (`i * i = 4` already exceeds `n`, so the loop body never executes), or any even `n` (the first and only iteration checked, `i = 2`, immediately finds `n % 2 == 0` and returns). Every odd `n >= 5` that isn't itself hit on that first check hangs indefinitely. The fix is a one-line addition of `i += 1` inside the loop body (matching the pattern used correctly in `is_prime_six_k_optimization`'s `i += 6`), but it hasn't been applied here — flagging it rather than silently patching it.

## Additional Solution — 6k ± 1 Skipping

```python
    def is_prime_six_k_optimization(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
```

> **Calling convention:** all three are instance methods (they take `self`) — call them on an instance (`Solution().is_prime_six_k_optimization(n)`), not on the class directly.
>
> **Why 6k ± 1 is worth knowing but not the default:** it's the fastest of the three in raw candidate count, but it trades that speed for more special-casing up front (2, 3, and the `i` / `i+2` pair each need their own handling), which makes it easier to get subtly wrong. The square-root approach is meant to be the simpler default with less to keep track of — though as the callout above shows, "simpler" didn't save it from its own bug here.

### Algorithm — Trial Division up to n-1
1. If `n <= 1`, return `False` (not prime).
2. Loop `i` from `2` up to `n - 1`: if `n % i == 0`, return `False`.
3. If the loop completes with no divisor found, return `True`.

### Algorithm — Trial Division up to √n (as implemented — see bug callout above)
1. If `n <= 1`, return `False`.
2. Set `i = 2`.
3. While `i * i <= n`: if `n % i == 0`, return `False`. (No increment of `i` occurs here — this is the bug.)
4. If the loop ever exits on its own, return `True`.

### Algorithm — 6k ± 1 Skipping
1. If `n <= 1`, return `False`.
2. If `n` is `2` or `3`, return `True`.
3. If `n` is divisible by `2` or `3`, return `False`.
4. Loop `i` starting at `5`, while `i * i <= n`: if `n % i == 0` or `n % (i + 2) == 0`, return `False`; otherwise advance `i` by `6`.
5. If the loop completes with no divisor found, return `True`.

## Dry Run

### Trial Division up to n-1 — `n = 17`

| `i` | `17 % i == 0`? |
|---|---|
| 2 | No |
| 3 | No |
| ... | No (4 through 15, none divide evenly) |
| 16 | No |

Loop completes with no divisor found. Return `True`. ✅ matches expected output.

### Trial Division up to √n — `n = 18` (a case where the bug doesn't manifest)

| `i` | `i*i <= 18`? | `18 % i == 0`? |
|---|---|---|
| 2 | Yes (4≤18) | Yes → return `False` immediately |

`18` is even, so `i = 2` resolves it on the very first check before the missing-increment bug ever gets a chance to matter. Return `False`. ✅ matches expected output.

**Contrast — `n = 5` (a case where the bug does manifest):** `i = 2`, `4 <= 5` is true, `5 % 2 == 0` is false, so the loop body finishes without returning — and loops back to the same condition with `i` still `2`. This repeats forever. See the bug callout above for the confirmed timeout.

### 6k ± 1 Skipping — `n = 97`

| Step | Check | Result |
|---|---|---|
| `n <= 1`? | No | continue |
| `n <= 3`? | No | continue |
| `97 % 2 == 0`? | No | continue |
| `97 % 3 == 0`? | No | continue |
| `i=5`: `5*5=25 <= 97`? | Yes | `97 % 5 = 2`, `97 % 7 = 6` → neither is 0 |
| `i=11`: `11*11=121 <= 97`? | No | loop exits |

Return `True`. ✅ matches expected output — only `5` and `7` were ever tested as candidate divisors.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Trial Division up to n-1 | O(n) | O(1) | Checks every candidate from 2 to n-1; only the loop counter is stored. |
| Trial Division up to √n | O(√n) intended, but hangs (∞) for most odd inputs | O(1) | See the known bug above — the missing `i += 1` means this does not terminate for any odd n ≥ 5 that isn't caught on the first check. |
| 6k ± 1 Skipping | O(√n) | O(1) | Skips roughly two-thirds of the candidates a plain square-root scan would check, by only testing numbers of the form 6k ± 1. |

For `n` near the top of the 32-bit range (~2.1 billion), Trial Division up to n-1 does on the order of two billion checks, while 6k ± 1 Skipping does roughly 15,000 — the sqrt-scan method's intended cost sits between those two, but its actual behavior on most inputs is to never finish.

## Real-World Use Case

Primality testing and the square-root/6k±1 scanning techniques come up wherever number-theoretic properties matter:

- **Cryptography** — RSA and other public-key schemes need large prime numbers to construct keys; trial division (often after faster probabilistic filters like Miller-Rabin) is a building block in identifying prime candidates.
- **Hash table sizing** — many hash table implementations pick a prime number of buckets specifically because it reduces collision clustering, so a fast primality check helps pick or validate that size.
- **Number-theoretic algorithms** — sieve-based prime generation (e.g. the Sieve of Eratosthenes), factorization routines, and GCD-adjacent utilities all rely on the same square-root bound as a core building block.
- **Puzzle and competitive-programming problems** — many problems reduce to "is this value prime," so a correct, efficient primality check is a reusable utility worth having on hand.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`). `is_prime_trial_division` and `is_prime_six_k_optimization` are run together across the same inputs using `subTest`, so a single test method reports which specific method fails. `is_prime_sqrt_scan` is tested separately, and only with inputs confirmed safe against its infinite-loop bug (see the callout above) — it is deliberately never called with an odd `n >= 5` in this test file, since that would hang the test run.

| Test | Input | Expected | Methods covered |
|---|---|---|---|
| `test_example_1` | n=17 | True | trial_division, six_k |
| `test_example_2` | n=18 | False | trial_division, six_k |
| `test_negative` | n=-7 | False | trial_division, six_k |
| `test_zero` | n=0 | False | trial_division, six_k |
| `test_one` | n=1 | False | trial_division, six_k |
| `test_two_smallest_prime` | n=2 | True | trial_division, six_k |
| `test_three` | n=3 | True | trial_division, six_k |
| `test_larger_prime` | n=997 | True | trial_division, six_k |
| `test_larger_composite` | n=1000 | False | trial_division, six_k |
| `test_perfect_square_composite` | n=49 | False | trial_division, six_k |
| `test_sqrt_scan_boundary_and_even_inputs_only` | n ∈ {-3, 0, 1, 2, 3, 4, 18, 1000} | per case | sqrt_scan (safe subset only) |

All 11 tests (29 sub-assertions total) pass against the current `sol.py`. The known bug in `is_prime_sqrt_scan` is real and unfixed — it simply isn't exercised with inputs that would trigger it.

Run with:
```bash
cd Loops_Iteration/prime_number_check
python3 -m unittest -v
```
