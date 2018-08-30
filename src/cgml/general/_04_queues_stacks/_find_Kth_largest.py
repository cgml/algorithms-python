import heapq

'''
TC: O(nlogk)
+SC: O(k)
'''
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for item in nums: #O(n)
            if len(h) == k:
                if h[0] < item:
                    heapq.heappop(h) #O(logk)
                    heapq.heappush(h, item) #O(logk)
            else:
                heapq.heappush(h, item) #O(logk)
        return h[0]


print(Solution().findKthLargest([9,8,7,6,5,4,3,2,1],3))