class Solution:
    def minCostClimbingStairs(self, cost):
        if not cost: return 0
        m = [None] * len(cost)
        result = min(self._helper(cost, 0, m), self._helper(cost, 1, m))
        return result

    def _helper(self, cost, idx, m):
        if idx >= len(cost): return 0
        if m[idx] is not None: return m[idx]
        m[idx] = cost[idx] + min(self._helper(cost, idx + 1, m), self._helper(cost, idx + 2, m))
        return m[idx]


#Most Efficient
class SolutionTX:
    def minCostClimbingStairs(self, cost):
        old, current = cost[0], cost[1]
        for cst in cost[2:]: current, old = min(old, current) + cst, current
        return min(old, current)