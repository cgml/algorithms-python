# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

from collections import defaultdict
from collections import deque
import heapq


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int

        Worst case in any case O(n^2), cause it's necessary to check everyone if it has any out link

        Optimizations:
        1. Prioritize list of celebrities to check by number of incoming links
        2. Prioritize outcoming check for each particular celebrity by:
            a. friends first (person most likely follows back friend)
            b. following count (if not friend - then go for popular first)

        """
        g = defaultdict(dict)

        for idx in range(n): g[idx] = {'idx': idx, 'out': [], 'in': []}

        # potential celebrities to check
        q = [(0, c) for c in g]
        while q:
            followers, c = q.pop(0)
            if self._celebrity(c, g): return c
            q = sorted([(len(g[c]['in']), c) for c in q])
        return -1

    def _celebrity(self, c, g):
        h = []
        for v in g:
            if v == c: continue
            heapq.heappush(h, (float('-inf') if c in g[v]['out'] else -len(g[v]['in']), v))
        celebrity = True
        while h:
            priority, v = heapq.heappop(h)
            if knows(c, v):
                celebrity = False
                g[c]['out'].append(v)
                g[v]['in'].append(c)
        return celebrity
