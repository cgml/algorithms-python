import heapq
import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def smallestRange(self, nums):
        pq = [(row[0], lidx, 0) for lidx, row in enumerate(nums)]
        heapq.heapify(pq)

        result = -1e9, 1e9
        right = max(row[0] for row in nums)
        while pq:
            left, lidx, iidx = heapq.heappop(pq)
            if right - left < result[1] - result[0]: result = left, right
            if iidx + 1 == len(nums[lidx]): return result
            v = nums[lidx][iidx + 1]
            right = max(right, v)
            heapq.heappush(pq, (v, lidx, iidx + 1))

nums = [[-51,-9,-3,1,1,7,10,11],
        [17,26,32,32,33,37],
        [5,45,88,90,91],
        [23,35,64,71,95,95,95,96],
        [-25,-15,-12,41],
        [20,30,31,32,40],
        [9,13],
        [-11,34,36,43,45,46],
        [86,97,99,100],
        [-4,37,38],
        [-2,72,74,76,80,90,91],
        [-14,12,26,32,32,32,33,33,35],
        [58,65,88,99],
        [-30,0,23,23,25,25,25,26],
        [-53,-26,-19,-4,18,41],
        [-7,13,15],[15,17,17,18],
        [56,58,62],
        [-17,-14,8,11,16,18,18,19,19,19,20],
        [6,58,70,74,74,75,75,75,75,76]]

# nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print('Actual:   ', Solution().smallestRange(nums))
# print('Expected: [20, 24]')
print('Expected: [11,86]')