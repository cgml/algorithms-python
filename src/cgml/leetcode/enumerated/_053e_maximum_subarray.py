class Solution:
    def maxSubArray(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not a: return 0
        N = len(a)
        m = [None]*N
        curmax = m[0] = a[0]
        for idx in range(1,N):
            m[idx] = max(a[idx],a[idx]+m[idx-1])
            if m[idx]>curmax: curmax = m[idx]
        return curmax


assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6