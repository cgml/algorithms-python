# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import heapq

class Solution(object):
    def merge(self, ixs):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        p = [[i.start, i.end] for i in ixs]
        heapq.heapify(p)
        result = []
        while p:
            i = heapq.heappop(p)
            if p and p[0][0]<=i[1]:
                ni = heapq.heappop(p)
                heapq.heappush(p,[i[0],max(ni[1],i[1])])
            else:
                result.append(Interval(i[0], i[1]))
        return result

