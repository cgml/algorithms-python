import heapq
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        q, d = [], {}
        for n in nums:
            while q and q[0] < n: d[heapq.heappop(q)]=n
            heapq.heappush(q,n)
        return [d.get(k, -1) for k in findNums]