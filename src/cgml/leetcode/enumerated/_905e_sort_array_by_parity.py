class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [None] * len(A)
        l, r = 0, len(A) - 1
        for idx, n in enumerate(A):
            if n % 2 == 0:
                result[l], l = n, l + 1
            else:
                result[r], r = n, r - 1
        return result
