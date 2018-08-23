class Solution:
    def rob(self, h):
        """
        :type h: List[int]
        :rtype: int
        """
        if not h: return 0
        N = len(h)
        if N == 1: return h[0]
        m, m[1] = [0]*(N+1), h[0]
        for idx in range(2,N+1): m[idx]=max(h[idx-1]+m[idx-2],m[idx-1])
        return m[-1]

assert Solution().rob([2,7,9,3,1])==12