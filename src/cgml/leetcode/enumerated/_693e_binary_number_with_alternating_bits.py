class Solution(object):
    def hasAlternatingBits(self, n):
        while n:
            prev, n = n & 1, n>>1
            if prev == n & 1: return False
        return True