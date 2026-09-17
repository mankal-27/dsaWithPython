from collections import deque

dq = deque([2,3,1])

dq.append(5)
print(dq)

dq.appendleft(7)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.extend([10,19])
print(dq)

dq.extendleft([34,55])
print(dq)

dq.rotate(2)
print(dq)