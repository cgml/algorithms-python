# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        m, c, q, p = 0, 0, [[i.start, i.end] for i in intervals], []
        heapq.heapify(q)
        while q:
            item = heapq.heappop(q)
            while p and p[0] <= item[0]:
                c -= 1
                heapq.heappop(p)
            c, m = c+1, max(m,c+1)
            heapq.heappush(p,item[1])

        return m

class SolutionNoHeaps(object):
    def minMeetingRooms(self, intervals):
        if intervals is None or len(intervals) == 0: return 0
        sl = sorted([j.start for j in intervals])
        el = sorted([j.end for j in intervals])
        avail = extra = i = j = 0
        while i < len(sl):
            if sl[i] < el[j]:
                if avail == 0: extra += 1
                else: avail -= 1
                i += 1
            else: avail, j = avail + 1, j+1
        return extra

print(Solution().minMeetingRooms( [Interval(i[0],i[1]) for i in [[0, 30],[5, 10],[15, 20]]]))
print(Solution().minMeetingRooms( [Interval(i[0],i[1]) for i in [[7,10],[2,4]]]))