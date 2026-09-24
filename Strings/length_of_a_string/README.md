# Length of a String

**Topic:** Strings
**Difficulty:** Easy
**Link:** https://algomaster.io/learn/dsa/length-of-a-string
**Files:** `sol.py` (solution), `test_sol.py` (unit tests)

## Problem Statement

Given a string s, return its length by counting the characters one by one with a loop. Do not use any built-in length function.

The length is the number of characters in the string, including spaces and digits. For example, "hello" has length 5.

An empty string has no characters, so its length is 0.

**Example 1**
```
Input:  s = "hello"
Output: 5
```

**Example 2**
```
Input:  s = "open ai"
Output: 7
```

**Constraints**
```
0 <= s.length <= 10^4
s consists of printable ASCII characters.
```

## How to Solve It — Thought Process

This is the first problem in the "Strings" topic, and it's worth noticing right away that a string isn't really a new kind of object to reason about here — for the purpose of "how many things are in this container," a string behaves exactly like the arrays from the previous topic: it's an ordered sequence of elements (characters instead of numbers), and Python lets you iterate over either one with the exact same `for` loop syntax. So the instinct that solved "sum an array" or "search an array" by walking through it one element at a time applies unchanged here — the only difference is what's living in each slot.

The problem is explicit that the built-in length helper is off-limits, which is really asking for the mechanism behind that helper rather than a call to it: how would you count something if you couldn't just ask "how many"? The natural answer is a tally — start a counter at zero, and for every character you pass on your way through the string, add one to it. By the time you've visited every character exactly once, the counter holds the true count, because it was incremented exactly as many times as there were characters to visit.

The one edge case worth being deliberate about is the empty string. It doesn't need a special `if` check because it falls out of the same logic that handles every other case: iterating over `""` simply produces zero characters to loop over, so the counter never gets incremented and correctly stays at its starting value of `0`. Starting the counter at `0` rather than `1` (or leaving it uninitialized) is exactly what makes this work — the "do nothing" behavior of an empty loop has to agree with the "nothing happened yet" value of the counter.

Since every character in the string has to be looked at at least once to be counted — there's no way to know how many characters exist without examining each one — a single linear pass is already the best this problem can do. There's no shortcut that avoids visiting an element to count it.

## Brute Force Solution — Character Loop (this is already optimal; every character must be visited once to be counted, so a single linear pass can't be improved on)

```python
class Solution:
    def length_of_string_char_loop(self, s):
        count = 0
        for char in s:
            count += 1
        return count
```

## Additional Solution — Built-in `len()`

```python
    def length_of_string_builtin_len(self, s):
        return len(s)
```

> **Calling convention:** both are instance methods (they take `self`) — call them on an instance (`Solution().length_of_string_char_loop(s)`), not on the class directly.
>
> **Why `len()` is kept separate rather than being "the" solution:** the problem statement explicitly disallows a built-in length function for the exercise — the whole point is practicing the counting mechanism a helper like `len()` normally hides. `length_of_string_char_loop` is the method that actually satisfies that constraint; `length_of_string_builtin_len` is included only as the "how you'd really write this in production Python" counterpart, the same way earlier problems paired a hand-written loop with `sum()`/`max()`/`list.index()`. Unlike those, this one isn't a *different algorithmic approach* to the same O(n) work — Python's `len()` on a `str` is O(1), since strings carry their length as stored metadata rather than computing it on demand, so it's asymptotically faster, not just more concise.

### Algorithm — Character Loop
1. Create a counter `count` and set it to `0`.
2. Move through the string one character at a time, from the first to the last.
3. At each character, increase `count` by `1`.
4. After the loop finishes, return `count`.

### Algorithm — Built-in `len()`
1. Call `len(s)`, which reads the string's stored length directly.
2. Return it.

## Dry Run

### Character Loop — `s = "hello"`

| Character visited | `count` after |
|---|---|
| h | 1 |
| e | 2 |
| l | 3 |
| l | 4 |
| o | 5 |

No more characters. Return `5`. ✅ matches expected output.

### Character Loop — `s = ""` (empty string)

The `for char in s:` loop has zero characters to iterate over, so its body never runs. `count` stays at its initial value of `0`. Return `0`. ✅ matches the stated rule that an empty string has length `0`.

### Built-in `len()` — `s = "open ai"`

`len("open ai")` reads the string's length directly — `7` characters, including the space between "open" and "ai". Return `7`. ✅ matches expected output.

## Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Character Loop | O(n) | O(1) | Visits every character exactly once; a counter is the only extra state. Already optimal — counting requires examining each character at least once. |
| Built-in `len()` | O(1) | O(1) | Python's `str` stores its length as metadata at creation time, so `len()` reads it directly rather than counting on demand — asymptotically faster than the hand-written loop, not just shorter. |

## Real-World Use Case

Counting elements in a sequence one at a time — the exact mechanism this problem asks you to build by hand — is what every length/size operation in a standard library actually does under the hood for structures that don't cache their size, and understanding it matters wherever that caching assumption doesn't hold:

- **Streamed or generator-based text processing** — when text arrives as a stream (reading a file line-by-line, consuming a network response in chunks) rather than as a single in-memory string, there's no stored `len()` to call; the running-count pattern from this problem is exactly how length, word counts, or byte counts get tracked incrementally as data arrives.
- **Custom data structures and containers** — implementing your own linked list, queue, or other structure that doesn't track its size in a field requires exactly this counting-by-traversal technique to answer "how many elements do I have."
- **Input validation and length limits** — enforcing a maximum input length (a username field, a tweet-like character limit, a form field) sometimes needs a manual count in languages or contexts where encoding makes a built-in length unreliable (e.g., counting user-visible characters rather than raw bytes in multi-byte encodings).
- **Teaching and interviewing** — this exact "count without the built-in" constraint is a standard way to confirm someone understands what a length operation is actually doing, rather than only knowing which function to call.

## Tests

`test_sol.py` instantiates `Solution()` once (in `setUp`) and runs both methods against the same inputs using `subTest`, so a single test method reports which specific method fails.

| Test | Input | Expected |
|---|---|---|
| `test_example_1` | `"hello"` | 5 |
| `test_example_2_with_space` | `"open ai"` | 7 |
| `test_empty_string` | `""` | 0 |
| `test_single_character` | `"a"` | 1 |
| `test_all_spaces` | `"   "` | 3 |
| `test_string_with_digits` | `"a1b2c3"` | 6 |
| `test_long_string_near_length_constraint` | `"x" * 10000` | 10000 |

All 7 tests (14 sub-assertions across the 2 methods) pass against the current `sol.py` — no bugs were found in either implementation. Confirmed identically in the cloud container and re-run directly on-device as ground truth.

Run with:
```bash
cd Strings/length_of_a_string
python3 -m unittest -v
```
