class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        lmax, curcnt = 0, -10**9
        while N > 0:
            if N & 1 == 1: lmax, curcnt = max(lmax, curcnt), 0
            curcnt, N = curcnt+1, N>>1
        return lmax