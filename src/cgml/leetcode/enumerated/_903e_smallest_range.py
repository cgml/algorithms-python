class Solution(object):
    def smallestRangeI(self, A, K):
        return max(max(A)-min(A)-2*K,0)