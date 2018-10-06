class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for n in range(left, right + 1):
            if self._selfdividing(n): result.append(n)
        return result

    def _selfdividing(self, n):
        k = n
        while k > 0:
            digit = k % 10
            if digit == 0: return False
            if n % digit != 0: return False
            k = k // 10
        return True