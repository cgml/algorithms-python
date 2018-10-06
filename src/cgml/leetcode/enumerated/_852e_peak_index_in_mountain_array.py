class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A)-1
        while l < r:
            midx = (l+r) // 2
            if A[midx-1]/A[midx] < 1: l = midx+1
            else: r = midx -1
        return l if A[l] > A[l-1] else l-1