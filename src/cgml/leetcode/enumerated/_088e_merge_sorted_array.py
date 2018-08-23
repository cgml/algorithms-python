class Solution:
    def merge(self, n1, n, n2, m):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not n1 or not n2: return
        if len(n1) != (m+n) or len(n2) != m: return
        n = len(n1)
        m = len(n2)
        nidx, tailidx, midx = n-m-1, n-1, m-1
        while midx >= 0:
            if nidx >= 0 and n1[nidx] > n2[midx]:
                n1[tailidx] = n1[nidx]
                tailidx -= 1
                nidx -= 1
            else:
                n1[tailidx]=n2[midx]
                tailidx -= 1
                midx -= 1