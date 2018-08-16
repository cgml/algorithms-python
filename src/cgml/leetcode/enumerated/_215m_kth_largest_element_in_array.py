import heapq


class Solution:
    def findKthLargest(self, nums, k):
        h = []
        for item in nums:
            if len(h) == k:
                if h[0] < item:
                    heapq.heappop(h)
                    heapq.heappush(h, item)
            else:
                heapq.heappush(h, item)
        return h[0]

assert Solution().findKthLargest([9,8,7,6,5,4,3,2,1],3) == 7