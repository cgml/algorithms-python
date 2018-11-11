from collections import deque


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        R, C = len(matrix), len(matrix[0])

        for r in range(R): matrix[r][0] = int(matrix[r][0])
        for r in range(R):
            for c in range(1, C):
                matrix[r][c] = int(matrix[r][c])
                if matrix[r][c] > 0:
                    matrix[r][c] = matrix[r][c - 1] + matrix[r][c]
        maxes = [self._helper([matrix[r][c] for r in range(R)]) for c in range(C)]
        return max(maxes)

    def _helper(self, nums):
        N = len(nums)
        mem, maxmem, maxmem[0] = deque([0 for _ in range(nums[0])]), [0] * N, nums[0]
        for idx in range(1, N):
            while nums[idx] > len(mem): mem.append(idx)
            while nums[idx] < len(mem): mem.pop()
            if nums[idx] == 0: continue
            for idr in range(len(mem)):
                maxmem[idx] = max(maxmem[idx], (idx - mem[idr] + 1) * (idr + 1))
        return max(maxmem)



class SolutionOptimized:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n): height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans