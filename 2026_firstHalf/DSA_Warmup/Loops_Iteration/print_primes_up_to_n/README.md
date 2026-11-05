# Print All Primes Up to N

**Topic:** Loops & Iteration
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/print-primes-up-to-n
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given an integer n, return an array of all prime numbers p with 2 <= p <= n, in increasing order.

A prime number is a whole number greater than 1 whose only divisors are 1 and itself. If there are no primes in range, return an empty array.

**Example 1**
```
Input:  n = 10
Output: [2,3,5,7]
```

**Example 2**
```
Input:  n = 1
Output: []
```

**Constraints**
```
0 <= n <= 10^6
When n < 2, the answer is an empty array.
```

## How to Solve It — Thought Process

This is a step up from just checking whether a single number is prime — now every number from `2` to `n` needs that check, and the results need collecting into an ordered list. The most direct way to build on a single-number primality test is to just run it `n - 1` times: for each candidate `m` from `2` to `n`, ask "is `m` prime?" using the same square-root trial-division idea (a composite `m` always has a divisor at or below `√m`, since divisors pair up around the square root — if `a * b = m`, one of `a` or `b` is `≤ √m`). If nothing up to `√m` divides `m`, keep it; otherwise skip it.

That's correct, but it's wasteful in a way that's easy to miss: every single candidate restarts its divisor search from scratch. Checking whether `100` is divisible by `2` happens for `m = 100`, but the fact that `2` divides *every* even number from `4` to `n` was already knowable the moment `2` was confirmed prime — nothing about checking `100` specifically needed to happen. Testing each number independently throws away that shared structure. For `n` near the top of the allowed range (`10^6`), this per-candidate approach does roughly `n * √n` work in total, since each of the `n` candidates pays its own `O(√m)` divisor search.

The better idea flips the direction of the work entirely: instead of asking "for this number, does anything divide it?" one candidate at a time, mark off *multiples* of each prime as soon as that prime is found, so every later candidate that's a multiple of it is already known to be composite before it's ever individually inspected. Start by assuming every number from `2` to `n` might be prime. Walk up from `2`: since nothing has ruled `2` out yet, it's prime — so every multiple of `2` (`4, 6, 8, ...`) gets marked composite in one pass, because a multiple of a prime can never itself be prime (except the prime itself). Move to the next number still unmarked, `3` — it's prime for the same reason, so its multiples (`6, 9, 12, ...`) get marked too (some, like `6`, were already marked by `2`, which is fine — marking twice does no harm). Keep going, and whatever survives every sweep by the time the process finishes is exactly the set of primes.

One refinement matters for how much work this actually does: when sweeping out multiples of a prime `p`, the marking can start at `p * p` rather than `2 * p`. Every smaller multiple of `p` (like `2p`, `3p`, ..., up to `(p-1) * p`) has a factor smaller than `p`, which means it was already marked composite by an earlier, smaller prime's sweep — starting the sweep at `p * p` skips redoing work that's already done. This also bounds how far the outer "find the next prime to sweep with" loop needs to go: once `p * p` exceeds `n`, every remaining composite in range must already have been caught by a smaller prime's sweep, so the outer loop can stop at `√n`. This turns the total work into roughly `n log log n` — for practical purposes, barely more than linear in `n`, and dramatically better than the `n√n` of checking each candidate independently. The cost of this speed is that it needs an array of size `n + 1` to track which numbers are still standing, rather than the constant extra space the per-candidate approach uses.

## Brute Force Solution — Check Each Number

```python
class Solution:
    def primes_up_to_n_trial_division(self, n):
        result = []
        for m in range(2, n+1):
            is_prime = True
            d = 2
            while d*d <= n:
                if m % d == 0 :
                    is_prime = False
                    break
                d += 1
                if is_prime:
                    result.append(m)
        return result
```

> ⚠️ **Known bug:** `result.append(m)` is written one indentation level too deep — it sits inside the `while` loop's body (aligned with `d += 1`), not after the loop finishes. That means `m` gets appended once for *every* iteration of the inner `while` loop where `is_prime` is still `True` at that point, instead of once after the whole divisor search completes. On top of that, the loop condition is `d*d <= n` (comparing against the outer bound `n`) instead of `d*d <= m` (comparing against the *current candidate*), so the inner search runs for longer than it should and against the wrong target entirely.
>
> **Trace for `n = 10` (confirmed by direct execution: actual output is `[3, 5, 5, 7, 7, 9]`, not `[2, 3, 5, 7]`):**
> - `m = 2`: `d=2`, `4<=10` → `2 % 2 == 0` → `is_prime = False`, `break` *before* the append line is ever reached. **`2` is never appended, even though it's prime.**
> - `m = 3`: `d=2`, `4<=10` → `3 % 2 = 1` → `d becomes 3`, append **once** (`3` is still believed prime at this point) → loop continues: `9<=10` → `3 % 3 == 0` → break. Net: `3` appended once — correct by coincidence.
> - `m = 5`: appended **twice** (once after passing the `d=2` check, once after passing the `d=3` check, before the loop condition `d*d=16<=10` finally fails) → `5, 5` in the output.
> - `m = 7`: same pattern as `5` → appended **twice** → `7, 7` in the output.
> - `m = 9`: `d=2` passes (`9 % 2 != 0`) → appended **once** → then `d=3`: `9 % 3 == 0` → breaks. So the composite number `9` gets appended once, purely because the divisor that disqualifies it (`3`) wasn't reached until after one "still looks prime" append already fired.
> - `m = 4, 6, 8, 10`: each is caught by `d = 2` on the very first check, before the append line is reached, so none of them appear — correct outcome, but for the same structural reason `2` incorrectly doesn't appear (the divisor is found before any append happens).
>
> The fix is a two-part correction: change `d*d <= n` to `d*d <= m`, and dedent `result.append(m)` so it runs once, after the `while` loop exits, guarded by the `is_prime` flag — not on every passing iteration inside it. Flagging this rather than silently correcting it.

## Optimized Solution — Sieve of Eratosthenes

```python
    def primes_up_to_n_sieve_of_eratosthenes(self, n):
        if n < 2:
            return []
        is_prime = [True] * [n + 1]
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1
        return [i for i in range(2, n + 1) if is_prime[i]]
```

> ⚠️ **Known bug:** `is_prime = [True] * [n + 1]` uses square brackets around `n + 1`, making it `[True] * [n + 1]` — multiplying a list by another list, which Python doesn't support. This isn't a logic bug so much as a straightforward typo (it should be `[True] * (n + 1)`, parentheses not brackets), but the effect is that the method **crashes** rather than returning a wrong answer.
>
> **Confirmed directly:** calling `primes_up_to_n_sieve_of_eratosthenes(10)` (or any `n >= 2`) raises `TypeError: can't multiply sequence by non-int of type 'list'` immediately, every time. The `n < 2` guard on the line before it works fine and returns `[]` correctly for `n = 0` or `n = 1` — the crash only happens once execution reaches the line that builds the tracking array. Flagging this rather than silently correcting it.

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().primes_up_to_n_sieve_of_eratosthenes(n)`), not on the class directly.

### Algorithm — Check Each Number (as intended)
1. Create an empty result list.
2. Loop `m` from `2` to `n` inclusive.
3. For each `m`, test divisors `d` from `2` while `d * d <= m`; if any divides evenly, `m` is not prime.
4. If no divisor was found, append `m` to the result.
5. Return the result list.

*(See the bug callout above for how the actual code deviates from this.)*

### Algorithm — Sieve of Eratosthenes (as intended)
1. If `n < 2`, return an empty list immediately (no primes exist in range).
2. Create a boolean list `is_prime` of size `n + 1`, all `True`, then set indices `0` and `1` to `False`.
3. For each `p` from `2` while `p * p <= n`: if `is_prime[p]` is still `True`, mark every multiple of `p` from `p * p` to `n` (stepping by `p`) as `False`.
4. Collect every index from `2` to `n` whose entry is still `True`.
5. Return that list.

*(See the bug callout above — step 2 crashes before this algorithm can run at all.)*

## Dry Run

The bug callouts above already trace both implementations against `n = 10` and `n = 2` step by step, since the interesting behavior here *is* the bug. For reference, here's what a correct execution looks like conceptually, using the intended algorithms:

### Check Each Number (intended) — `n = 10`

| `m` | Divisor search | Result |
|---|---|---|
| 2 | `d=2`: `2*2=4 > 2`, loop never runs | prime → append |
| 3 | `d=2`: `2*2=4 > 3`, loop never runs | prime → append |
| 4 | `d=2`: `4<=4`, `4 % 2 == 0` | composite → skip |
| 5 | `d=2`: `4<=5`, no; `d=3`: `9>5`, loop ends | prime → append |
| 6 | `d=2`: `4<=6`, `6 % 2 == 0` | composite → skip |
| 7 | `d=2`: `4<=7`, no; `d=3`: `9>7`, loop ends | prime → append |
| 8, 9, 10 | each hits a divisor (2, 3, 2) | composite → skip |

Intended return: `[2, 3, 5, 7]`.

### Sieve of Eratosthenes (intended) — `n = 10`

| Step | Action | `is_prime` state (indices 2–10) |
|---|---|---|
| init | all `True` except 0, 1 | `[2:T, 3:T, 4:T, 5:T, 6:T, 7:T, 8:T, 9:T, 10:T]` |
| `p=2` | mark 4, 6, 8, 10 | `[2:T, 3:T, 4:F, 5:T, 6:F, 7:T, 8:F, 9:T, 10:F]` |
| `p=3` | mark 9 | `[2:T, 3:T, 4:F, 5:T, 6:F, 7:T, 8:F, 9:F, 10:F]` |
| `p=4`, `4*4=16>10` | loop stops | (unchanged) |

Intended return: `[2, 3, 5, 7]`.

## Complexity

| Approach | Time Complexity (intended) | Actual Behavior | Space Complexity | Notes |
|---|---|---|---|---|
| Check Each Number | O(n√n) | Runs, but returns wrong results (see bug callout) | O(1) extra (excluding output) | The misplaced append and wrong loop bound produce duplicates, omissions, and misclassified composites. |
| Sieve of Eratosthenes | O(n log log n) | Crashes with `TypeError` for any `n >= 2` | O(n) | The `[True] * [n + 1]` typo prevents the array from ever being built. |

## Real-World Use Case

Generating primes in bulk, and the sieve technique specifically, show up wherever a range of prime numbers is needed rather than a single check:

- **Cryptographic key generation** — while individual large-prime testing typically uses probabilistic methods, sieving is commonly used to quickly rule out small-prime-divisible candidates before running more expensive tests.
- **Precomputed lookup tables** — competitive programming and numerical libraries often precompute "is prime" or "smallest prime factor" tables for a bounded range once, so that many later queries are O(1) lookups instead of repeated primality tests.
- **Number-theoretic research and puzzles** — twin-prime search, Goldbach-conjecture verification tools, and similar explorations all need an efficient way to enumerate primes over a range rather than test one number at a time.
- **Teaching the "batch elimination beats repeated individual checks" pattern** — the sieve's core idea (do the shared work once, propagate it to everything affected, instead of redoing it per item) generalizes to caching and precomputation strategies well beyond number theory.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails. Expected values are the mathematically correct ones per the problem statement, not adjusted to match either bug.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | n=10 | [2, 3, 5, 7] |
| `test_example_2_below_smallest_prime` | n=1 | [] |
| `test_zero` | n=0 | [] |
| `test_smallest_prime_boundary` | n=2 | [2] |
| `test_just_above_smallest_prime` | n=3 | [2, 3] |
| `test_mid_range` | n=30 | [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] |
| `test_upper_bound_is_prime` | n=29 (n itself is prime) | [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] |
| `test_larger_range_count` | n=1000 | 168 primes (count only) |

**Current result against the real `sol.py`: 2 of 8 tests pass, 6 fail, and `primes_up_to_n_sieve_of_eratosthenes` errors (crashes) on every test where `n >= 2`.** The two passing tests (`n=0` and `n=1`) pass trivially for both methods — `primes_up_to_n_trial_division`'s `for m in range(2, n+1)` loop body never executes for those inputs, and `primes_up_to_n_sieve_of_eratosthenes`'s `n < 2` guard returns before ever reaching the crashing line. Every test with `n >= 2` fails or errors, confirmed identically both in this container and re-run directly on-device.

Run with:
```bash
cd Loops_Iteration/print_primes_up_to_n
python3 -m unittest -v
```
