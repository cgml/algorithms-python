class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            cnt = cnt+1 if n & 1 == 1 else cnt
            n = n>>1
        return cnt
print(Solution().hammingWeight(2))