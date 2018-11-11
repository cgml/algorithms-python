from collections import deque


class Solution:
    def maxRectangle1Darray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums_neg = [-v if v < 0 else 0 for v in nums]
        nums_pos = [v if v > 0 else 0 for v in nums]
        return max(self._helper(nums_neg), self._helper(nums_pos))

    def _helper(self, nums):
        N = len(nums)
        mem, maxmem = deque([0 for _ in range(nums[0])]), [0] * N
        maxmem[0] = nums[0]
        for idx in range(1, N):
            while nums[idx] > len(mem): mem.append(idx)
            while nums[idx] < len(mem): mem.pop()
            if nums[idx] == 0: continue
            for idr in range(len(mem)):
                s1 = (idx - mem[idr] + 1) * (idr+1)
                maxmem[idx] = max(maxmem[idx], s1)
            # s1 = (idx - mem[nums[idx] - 1] + 1) * nums[idx]
            # s2 = (idx - mem[min(nums[idx - 1], nums[idx]) - 1] + 1) * min(nums[idx - 1], nums[idx])
            # maxmem[idx] = max(s1, s2)
        return max(maxmem)


print(Solution().maxRectangle1Darray([0, 2, 3, 4, 5, 4, 3, 2, 1]))
print(Solution().maxRectangle1Darray([1, 2, 3, 4, 5, 4, 3, 2, 1]))
print(Solution().maxRectangle1Darray([1, 2, 2, 1]))
print(Solution().maxRectangle1Darray([3, 0, 3, 5, 0]))
print(Solution().maxRectangle1Darray([1, 3, 4, 4, 0]))