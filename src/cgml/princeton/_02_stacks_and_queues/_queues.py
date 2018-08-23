from collections import deque

d = deque()
for s in 'abcd': d.append(s)
while d: print(d.pop())
for s in 'abcd': d.append(s)
d.extend([str(i) for i in range(100)])
while d: print(d.popleft())