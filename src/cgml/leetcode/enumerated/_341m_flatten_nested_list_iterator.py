print(isinstance([], list))

from collections import deque

l = [10,12,13,14,15,16,17]

q = deque(l)

del q[3]
# q.remove(3)

print(list(q))