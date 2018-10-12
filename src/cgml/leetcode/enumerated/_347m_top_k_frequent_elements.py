from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c, h = Counter(nums), []
        for ck, v in c.items():
            if len(h) < k: heapq.heappush(h, (v,ck))
            elif h[0][0] < v:
                heapq.heappop(h)
                heapq.heappush(h,(v,ck))
        return list(sorted([ck for v, ck in h]))


print(Solution().topKFrequent([1,4,4,4,4,4,1,5,6,7,1,1,1,2,2,3],2))