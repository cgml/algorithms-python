class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        vals = [i for i in range(n)]
        for p, q in edges:
            rootP = self.findRoot(p, vals)
            rootQ = self.findRoot(q, vals)
            if rootP == rootQ: return False
            vals[rootQ] = rootP
        return len(edges) == n - 1

    def findRoot(self, n, vals):
        while True:
            if vals[n] == n: return n
            n = vals[vals[n]]

assert Solution().validTree(5,[[0,1],[0,2],[0,3],[1,4]])