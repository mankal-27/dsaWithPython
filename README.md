# DSA with Python — Strivers A2Z Sheet (takeuforward.org Plus)

Tracking my Data Structures & Algorithms practice using the [TUF+ DSA Problem Set](https://takeuforward.org/plus/dsa/problems/input-output?subject=dsa), based on [Striver's A2Z DSA Course/Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z) (17 steps, ~450 problems). Every solved problem is documented here with its time/space complexity, a manual dry run, and where the underlying technique shows up in real systems — so this file doubles as a revision sheet before interviews.

## How this repo is organized

```
dsaWithPython/
├── 01_sorting/
├── 02_arrays/
├── 03_binary_search/
├── 04_strings/
├── 05_linked_list/
├── 06_recursion/
├── 07_bit_manipulation/
├── 08_stack_queue/
├── 09_sliding_window_two_pointer/
├── 10_heaps/
├── 11_greedy/
├── 12_binary_trees/
├── 13_binary_search_trees/
├── 14_graphs/
├── 15_dynamic_programming/
├── 16_tries/
├── 17_strings_advanced/
└── README.md   <- this file
```

Each solved problem gets a `.py` file named after the problem (e.g. `two_sum.py`) inside its topic folder, plus an entry in the matching table below.

## Entry template

Copy this block into the relevant topic section whenever a new problem is solved:

```
### <Problem Name> (<Difficulty>)
- **Link:** <takeuforward.org / leetcode link>
- **File:** `0X_topic/problem_name.py`
- **Approach:** one or two lines on the technique used
- **Time Complexity:** O(...)
- **Space Complexity:** O(...)
- **Dry Run:** step-by-step trace on a small example
- **Real-World Use Case:** where this pattern shows up in production systems
```

## Progress Tracker

| # | Step / Topic | Problems in Step | Solved | Status |
|---|---|---|---|---|
| 1 | Sorting Techniques | 7 | 0 | Not started |
| 2 | Arrays (Easy → Hard) | 40 | 0 | Not started |
| 3 | Binary Search (1D, 2D, Search Space) | 32 | 0 | Not started |
| 4 | Strings (Basic & Medium) | 15 | 0 | Not started |
| 5 | LinkedList (Single, Double, Medium, Hard) | 31 | 0 | Not started |
| 6 | Recursion (Patternwise) | 25 | 0 | Not started |
| 7 | Bit Manipulation | 18 | 0 | Not started |
| 8 | Stack & Queues | 30 | 0 | Not started |
| 9 | Sliding Window & Two Pointer | 12 | 0 | Not started |
| 10 | Heaps | 17 | 0 | Not started |
| 11 | Greedy Algorithms | 15 | 0 | Not started |
| 12 | Binary Trees | 38 | 0 | Not started |
| 13 | Binary Search Trees | 16 | 0 | Not started |
| 14 | Graphs | 53 | 0 | Not started |
| 15 | Dynamic Programming | 55 | 0 | Not started |
| 16 | Tries | 7 | 0 | Not started |
| 17 | Strings (Advanced) | 9 | 0 | Not started |
| | **Total** | **~450** | **0** | |

Update the "Solved" column and flip "Status" to `In progress` / `Done` as problems get solved.

---

## Worked Examples

The four problems below are filled in completely so the format above is easy to copy. Replace/extend this section as more problems are solved — keep the worked examples that are genuinely useful for revision.

### 1. Two Sum (Easy) — Step 2: Arrays

- **Link:** https://takeuforward.org/plus/dsa/problems/two-sum
- **File:** `02_arrays/two_sum.py`
- **Approach:** Single pass with a hash map storing `value -> index`. For each element, check if `target - element` was already seen.

```python
def two_sum(nums, target):
    seen = {}                      # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

- **Time Complexity:** O(n) — one pass, O(1) average hash map lookups.
- **Space Complexity:** O(n) — hash map can hold up to n elements.
- **Dry Run:** `nums = [2, 7, 11, 15]`, `target = 9`
  | i | num | complement | seen (before) | seen (after) | match? |
  |---|---|---|---|---|---|
  | 0 | 2 | 7 | {} | {2: 0} | no |
  | 1 | 7 | 2 | {2: 0} | — | yes → return `[0, 1]` |

  Result: `[0, 1]` since `nums[0] + nums[1] = 2 + 7 = 9`.
- **Real-World Use Case:** Hash-based complement lookups like this power fraud/duplicate-pair detection (e.g. matching a debit and a credit that cancel out in a ledger) and "find two items whose combined price equals a budget" features in shopping/recommendation engines.

### 2. Binary Search on Sorted Array (Easy) — Step 3: Binary Search

- **Link:** https://takeuforward.org/plus/dsa/problems/binary-search
- **File:** `03_binary_search/binary_search.py`
- **Approach:** Repeatedly halve the search space by comparing the middle element to the target.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

- **Time Complexity:** O(log n) — search space halves each iteration.
- **Space Complexity:** O(1) — iterative, no extra structures.
- **Dry Run:** `arr = [2, 4, 6, 8, 10, 12]`, `target = 10`
  | low | high | mid | arr[mid] | action |
  |---|---|---|---|---|
  | 0 | 5 | 2 | 6 | 6 < 10 → low = 3 |
  | 3 | 5 | 4 | 10 | match → return 4 |

  Result: index `4`.
- **Real-World Use Case:** Database index lookups (B-tree search), `bisect` in Python's standard library, autocomplete/dictionary lookups, and "find the first failing commit" style bisection in git bisect / CI debugging all rely on this pattern.

### 3. Reverse a Linked List (Easy) — Step 5: LinkedList

- **Link:** https://takeuforward.org/plus/dsa/problems/reverse-linked-list
- **File:** `05_linked_list/reverse_linked_list.py`
- **Approach:** Iterate through the list, flipping each node's `next` pointer to point backward, tracking `prev` and `curr`.

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev   # new head
```

- **Time Complexity:** O(n) — visits every node once.
- **Space Complexity:** O(1) — reversal done in place with pointers.
- **Dry Run:** List `1 -> 2 -> 3 -> None`
  | curr | next_node | curr.next (after) | prev (after) |
  |---|---|---|---|
  | 1 | 2 | None | 1 |
  | 2 | 3 | 1 | 2 |
  | 3 | None | 2 | 3 |

  Loop ends when `curr` is `None`; return `prev` = node `3`. Final list: `3 -> 2 -> 1 -> None`.
- **Real-World Use Case:** Undo/redo history and browser back/forward stacks are often modeled as linked structures that get reversed or traversed backward; reversing a linked list is also a common step in "reverse in groups of k" problems used in low-level buffer/packet reordering.

### 4. Fibonacci with Memoization (Easy/Medium) — Step 15: Dynamic Programming

- **Link:** https://takeuforward.org/plus/dsa/problems/fibonacci-number
- **File:** `15_dynamic_programming/fibonacci_memo.py`
- **Approach:** Top-down recursion with a memo dictionary to avoid recomputing overlapping subproblems.

```python
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

- **Time Complexity:** O(n) — each subproblem `fib(k)` computed once and cached (vs O(2^n) for naive recursion).
- **Space Complexity:** O(n) — memo dictionary plus O(n) recursion stack.
- **Dry Run:** `fib(4)`
  ```
  fib(4) -> fib(3) + fib(2)
  fib(3) -> fib(2) + fib(1)
  fib(2) -> fib(1) + fib(0) = 1 + 0 = 1   (cached as memo[2] = 1)
  fib(1) = 1
  fib(3) = fib(2) + fib(1) = 1 + 1 = 2    (cached as memo[3] = 2)
  fib(2) -> already in memo -> returns 1 instantly
  fib(4) = fib(3) + fib(2) = 2 + 1 = 3
  ```
  Result: `fib(4) = 3`, and `fib(2)` was computed only once thanks to the memo.
- **Real-World Use Case:** Memoization/DP underlies caching layers in web backends, route-cost calculations in navigation apps (shortest path DP), and financial pricing models (e.g. option pricing recurrences) where repeated subproblems would otherwise be recomputed millions of times.

---

## Notes

- Problem counts per step are taken from Striver's A2Z DSA Sheet structure as of Sep 2026; TUF+ may add/reorder problems over time, so re-check counts periodically.
- Keep dry runs short (3–6 steps) — the goal is to catch off-by-one and edge-case errors, not to trace every element for large inputs.
- When a problem has multiple valid approaches (brute force → better → optimal), document the optimal one here but keep the brute-force version in code comments for interview discussions.
