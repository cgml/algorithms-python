import heapq

import numpy as np
h = []
for i in range(10):
    heapq.heappush(h, 10-i)

print(h)