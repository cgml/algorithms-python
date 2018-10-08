class Solution(object):
    def projectionArea(self, grid):
        gridv = list(zip(*grid))
        return sum([min(1,grid[r][c]) for r in range(len(grid)) for c in range(len(grid[0]))]) + \
               sum([max(gridv[c]) for c in range(len(gridv))]) + \
               sum([max(grid[r]) for r in range(len(grid))])
