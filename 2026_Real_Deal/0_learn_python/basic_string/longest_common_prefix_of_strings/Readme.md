# Longest Common Prefix

**Topic:** Basic String · **Difficulty:** Easy

| File | Purpose |
|---|---|
| `my_sol.py` | Your original solution (review notes in comments) |
| `bug_free_solution.py` | `longest_common_prefix_brute_force` and `longest_common_prefix_optimized` with tests |

## 1. Problem Statement

Find the longest common prefix string among an array of strings. If there is none, return `""`.

| Input | Output | Why |
|---|---|---|
| `["flower","flow","flight"]` | `"fl"` | all start with `fl` |
| `["dog","racecar","car"]` | `""` | no shared first letter |
| `["single"]` | `"single"` | one string is its own prefix |
| `["ab","abc"]` | `"ab"` | prefix limited by shortest string |

## 2. Approaches

| | Brute Force | Optimized |
|---|---|---|
| Method | `longest_common_prefix_brute_force` | `longest_common_prefix_optimized` |
| Idea | Start with `strs[0]` as prefix; for each other word, chop the prefix's last char until the word starts with it | Sort; the smallest and largest strings differ the most, so compare only those two |
| Why it works | Prefix only ever shrinks to what every word shares | If first and last share a prefix, all strings between them do too |
| Care needed | Empty list; prefix may shrink to `""` (`startswith("")` is True, loop ends) | Empty list; stop at `min(len(first), len(last))` |

## 3. Review of `my_sol.py`

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | `sorted(s)` result is discarded, so the list is never sorted. `["flower","flight","flow"]` gives `"flow"`, expected `"fl"` | **Bug** | `s = sorted(s)` |
| 2 | Empty list crashes at `s[0]` | **Bug** | `if not s: return ""` |
| 3 | Idea (sort, compare first and last) is correct | None | keep it |
| 4 | Debug prints, `min(len-1, len-1)+1`, `if(...)` parentheses | Style | remove / simplify |

## 4. Dry Run

**Optimized, `["flower","flow","flight"]`:** sorted = `["flight","flow","flower"]`, first = `flight`, last = `flower`.

| `length` | `first[length]` | `last[length]` | Equal? |
|---|---|---|---|
| 0 | f | f | yes |
| 1 | l | l | yes |
| 2 | i | o | no, stop |

Return `first[:2]` = `"fl"`.

**Brute force, same input:** prefix `flower`; `flow` fails until prefix is `flow`; `flight` fails until prefix is `fl`. Return `"fl"`.

**`["dog","racecar","car"]`:** sorted first `car`, last `racecar`; `c != r` at index 0, return `""`.

## 5. Complexity

(n = number of strings, m = length of the shortest string)

| Approach | Time | Space | Explanation |
|---|---|---|---|
| Brute force | O(n·m) | O(1) | each word compared against a prefix of at most m chars |
| Optimized | O(n log n · m) | O(n) | sort dominates (string compares cost up to m), then one O(m) scan; `sorted` makes a copy |
