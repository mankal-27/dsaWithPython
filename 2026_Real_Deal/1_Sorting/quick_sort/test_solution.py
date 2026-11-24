import random
from solution import Solution

s = Solution()
cases = [[], [1], [2, 1], [5, 4, 3, 2, 1], [3, 1, 2, 3, 1], [1, 2, 3], [-1, 5, 0, -7], [4] * 10]
cases += [[random.randint(-50, 50) for _ in range(random.randint(0, 30))] for _ in range(200)]
cases += [list(range(2000)), list(range(2000, 0, -1))]
for c in cases:
    exp = sorted(c)
    assert s.quickSortBruteForce(list(c)) == exp, c
    assert s.quickSortOptimized(list(c)) == exp, c
print("all passed")
