import heapq  # heapq = Python's built-in min-heap (smallest item is always at index 0)

# A heap is just a normal list; heapq functions keep it in "heap order".
val = []

# heappush(heap, item) -> returns None. Adds item and keeps the heap valid.
heapq.heappush(val, 10)
heapq.heappush(val, 8)
heapq.heappush(val, 6)
print(val)  # [6, 10, 8] -> smallest (6) is at index 0; rest isn't fully sorted

heapq.heappush(val, 12)
heapq.heappush(val, 20)
print(val)  # [6, 10, 8, 12, 20]

# heappop(heap) -> removes AND returns the smallest item (O(log n)).
smallest = heapq.heappop(val)
print(smallest)  # 6
print(val)  # [8, 10, 20, 12]

# heap[0] -> peek at the smallest item without removing it.
print(val[0])  # 8

# heappushpop(heap, item) -> push item, THEN pop smallest, return it.
# Faster than push followed by pop. If item is smaller than everything, it comes right back.
popped = heapq.heappushpop(val, 5)
print(popped)  # 5 (5 was smaller than all, so it's returned immediately)
print(val)  # [8, 10, 20, 12] (unchanged)

popped = heapq.heappushpop(val, 15)
print(popped)  # 8 (smallest was popped, 15 got added)
print(val)  # [10, 12, 20, 15]

# heapreplace(heap, item) -> POP smallest first, THEN push item. Returns the popped one.
# Heap size stays the same. Raises IndexError if heap is empty.
# Difference from heappushpop: the returned value can be bigger than item.
replaced = heapq.heapreplace(val, 5)
print(replaced)  # 10 (old smallest returned, even though 5 is smaller)
print(val)  # [5, 12, 20, 15]

# heapify(list) -> turns an existing list into a heap IN PLACE in O(n). Returns None.
nums = [9, 4, 7, 1, 8, 2]
heapq.heapify(nums)
print(nums)  # [1, 4, 2, 9, 8, 7] -> nums[0] is now the smallest

# nlargest(n, iterable) -> returns a NEW list of the n biggest items, biggest first.
print(heapq.nlargest(3, nums))  # [9, 8, 7]

# nsmallest(n, iterable) -> returns a NEW list of the n smallest items, smallest first.
print(heapq.nsmallest(3, nums))  # [1, 2, 4]

# Both accept key= to compare by something else (e.g. second element of a tuple).
pairs = [("a", 3), ("b", 1), ("c", 2)]
print(heapq.nsmallest(2, pairs, key=lambda p: p[1]))  # [('b', 1), ('c', 2)]

# merge(*sorted_iterables) -> lazily merges already-sorted inputs into one sorted iterator.
print(list(heapq.merge([1, 4, 7], [2, 5, 8])))  # [1, 2, 4, 5, 7, 8]

# Max-heap trick: heapq only has min-heap, so push NEGATED values.
max_heap = []
for x in [3, 1, 5]:
    heapq.heappush(max_heap, -x)
print(-heapq.heappop(max_heap))  # 5 (largest)
