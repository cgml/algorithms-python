class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        while x or y:
            result += 0 if x & 1 == y & 1 else 1
            x, y = x>>1, y>>1
        return result