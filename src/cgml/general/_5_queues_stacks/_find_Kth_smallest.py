import heapq

'''
TC: O(nlogk)
+SC: O(k)

heapq - min heap. (to change it to max heap just add/retrieve reverse numbers)
'''
class Solution:
    def findKthLargest(self, nums, k):
        h = []
        for item in nums: #O(n)
            if len(h) == k:
                if h[0] < item:
                    heapq.heappop(h) #O(logk)
                    heapq.heappush(h, -item) #O(logk)
            else:
                heapq.heappush(h, -item) #O(logk)
        return -h[0]


print(Solution().findKthLargest([-9,8,7,6,5,4,3,2,1],3))