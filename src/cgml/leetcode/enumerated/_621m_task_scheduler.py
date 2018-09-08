from collections import Counter, deque
from queue import PriorityQueue
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks)
        pq = PriorityQueue()
        queue = deque([None]*n)
        for t in counts: pq.put((-counts[t],t))
        result = 0
        while counts:
            if pq.queue and pq.queue[0][1] not in queue:
                cnt, t = pq.get()
                queue.append(t)
                counts[t]-=1
                if counts[t] <= 0: del counts[t]
            else:
                queue.append(None)
            t = queue.popleft()
            if t is not None and counts[t]>0: pq.put((-counts[t],t))
            result += 1
        return result