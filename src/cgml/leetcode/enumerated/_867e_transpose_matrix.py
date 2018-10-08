class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [r for r in zip(*A)]

print(Solution().transpose([[1,2],[3,4]]))