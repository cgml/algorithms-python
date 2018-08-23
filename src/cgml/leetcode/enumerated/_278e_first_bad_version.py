# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
K=10
N=50
versions = [False]*(K)+[True]*(N-K)
def isBadVersion(n):
    return versions[n]

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return None
        lidx, ridx = 1, n
        while lidx < ridx:
            midx = (ridx - lidx) // 2 + lidx
            if isBadVersion(midx): ridx = midx - 1
            else: lidx = midx + 1
        if lidx > 1 and isBadVersion(lidx-1): return lidx - 1
        elif isBadVersion(lidx): return lidx
        else: return lidx + 1

assert Solution().firstBadVersion(N)==K