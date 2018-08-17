import numpy as np
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        R = len(grid)
        C = len(grid[0])
        gmem, curisland = np.ones((R,C))*-1, 0

        def explore_new_island(grid, gmem, row, col, curisland):
            if row<0 or col<0 or row>=R or col>=C or grid[row][col] == "0" or gmem[row][col]>=0: return
            gmem[row][col]=curisland
            explore_new_island(grid,gmem,row-1,col,curisland)
            explore_new_island(grid,gmem,row,col-1,curisland)
            explore_new_island(grid,gmem,row+1,col,curisland)
            explore_new_island(grid,gmem,row,col+1,curisland)

        def explore(grid, gmem, row, col, curisland):
            if grid[row][col] == "0":
                gmem[row][col] = 0
                return curisland
            if gmem[row][col] > 0: return curisland
            explore_new_island(grid,gmem,row,col,curisland+1)
            return curisland+1

        for row in range(gmem.shape[0]):
            for col in range(gmem.shape[1]):
                curisland = explore(grid,gmem,row,col, curisland)
        print(gmem)
        return np.max(gmem)

def grid(s):
    result = []
    for l in s.split("\n"):
        if l.strip(): result.append([str(k) for k in list(l.strip())])
    return result

s1 = """
11110
11010
11000
00000
"""
s2 = """
11000
11000
00100
00011
"""

print(Solution().numIslands(grid(s1)))
print(Solution().numIslands(grid(s2)))
