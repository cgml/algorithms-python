class Solution:
    def maxSubArrayLen(self, nums, k):
        index, l, sm = {}, 0, 0
        index[0] = -1
        for i, num in enumerate(nums):
            sm += num
            if sm - k in index:
                l = max(l, i - index[sm - k])
            if sm not in index:
                index[sm] = i
        return l

print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], k = 3))

class SolutionConsec(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curmax, cstart, curidx, csum = 0, 0, 0, 0
        while curidx < len(nums):
            while csum < k and curidx < len(nums): csum, curidx = csum+nums[curidx], curidx+1
            while csum > k and cstart <= len(nums): csum, cstart = csum-nums[cstart], cstart+1
            if csum == k: curmax = max(curmax, curidx-cstart)
            if curidx < len(nums): csum, curidx = csum+nums[curidx], curidx+1
        return curmax

import numpy as np
class SolutionDynamicTODO(object):
    def maxSubArrayLen(self, nums, k):
        mems = np.zeros((len(nums)+1,len(nums)+1))
        mem = np.zeros(len(nums))
        total = sum(nums)
        for idx in range(len(nums)): mem[idx]=total-nums[idx]

