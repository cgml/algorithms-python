class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]: return 0
        N = len(M)
        circles = list(range(N))

        for idr in range(1, N):
            for idc in range(0, idr):
                if M[idr][idc] == 1 and not self.connected(circles, idr, idc):
                    self.union(circles, idr, idc)
        components = set()
        for idx in range(N): components.add(self.root(circles, idx))
        return len(set(components))

    def connected(self, circles, idr, idc):
        return self.root(circles, idr) == self.root(circles, idc)

    def root(self, circles, idx):
        while circles[idx] != idx:
            circles[idx] = circles[circles[idx]]
            idx = circles[idx]
        return idx

    def union(self, circles, idr, idc):
        root_idr = self.root(circles, idr)
        root_idc = self.root(circles, idc)
        circles[root_idc] = root_idr