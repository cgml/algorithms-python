from collections import deque


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1: return self._perimeter(grid, r, c)
        return 0

    def _perimeter(self, grid, r, c):
        R, C = len(grid), len(grid[0])
        result, visited, q = 0, set(), deque([(r, c)])
        while q:
            r, c = q.pop()
            if (r, c) in visited: continue
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                result += 1
            else:
                visited.add((r, c))
                q += [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
        return result