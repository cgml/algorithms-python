import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        visited, R, C, marea = set(), len(grid), len(grid[0]), 0
        for r in range(R):
            for c in range(C):
                if (r,c) in visited: continue
                if grid[r][c]:
                    carea, q = 0, collections.deque([(r,c)])
                    while q:
                        cr, cc = q.popleft()
                        if (cr,cc) in visited: continue
                        visited.add((cr,cc))
                        if cr < 0 or cr >= R or cc < 0 or cc >= C or not grid[cr][cc]: continue
                        carea+=1
                        q+=[(cr-1,cc),(cr,cc-1),(cr+1,cc),(cr,cc+1)]
                    marea = max(marea,carea)
                else: visited.add((r,c))
        return marea