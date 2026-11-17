# Count Odd Elements

**Topic:** Basic Array · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (bug notes in comments) |
| `bug_free_solution.py` | `count_odd_brute_force` and `count_odd_optimized` with tests |

## 1. Problem Statement

Given an array of integers, return how many of its elements are odd.

| Input | Output | Why |
|---|---|---|
| `[1, 2, 3]` | `2` | 1 and 3 are odd |
| `[10, 20]` | `0` | all even |
| `[-3, -2, 7]` | `2` | negatives count too |
| `[]` | `0` | nothing to count |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `count_odd_brute_force` | `count_odd_optimized` |
| Idea | Loop, test `value % 2 != 0`, increment counter | `sum(value & 1 for value in numbers)` |
| Why it works | An odd number leaves remainder 1 when divided by 2 | The last bit of an odd number is 1, so `& 1` gives 1/0 and `sum` counts the 1s |
| Care needed | Use the element, not an index | None |

Both are O(n): every element must be inspected once.

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | `arr[value]` treats the element as an index; `[1, 2, 3]` hits `arr[3]` and raises `IndexError` | Bug | Use `value % 2 != 0` |
| 2 | Even without a crash it inspects the wrong elements, e.g. `[1, 0, 0]` | Bug | Same fix |
| 3 | Parentheses around `if` condition, vague name `total` | Style | `if value % 2 != 0`, `odd_count` |

## 4. Dry Run

**Brute force, `[1, 2, 3]`:**

| Step | `value` | `value % 2` | `odd_count` after |
|---|---|---|---|
| start | - | - | 0 |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 0 | 1 |
| 3 | 3 | 1 | 2 |

Result: `2`

## 5. Complexity

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n) | O(1) | One check per element, one counter |
| Optimized | O(n) | O(1) | Generator is lazy, no extra list; same single pass |
