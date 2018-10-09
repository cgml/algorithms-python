class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return True
        R, C = len(matrix), len(matrix[0])
        for c in range(0, C):
            if not self._validate(matrix, r=0, c=c): return False
        for r in range(1, R):
            if not self._validate(matrix, r=r, c=0): return False
        return True

    def _validate(self, matrix, r, c):
        R, C = len(matrix), len(matrix[0])
        v = matrix[r][c]
        while r < R and c < C:
            if matrix[r][c] != v: return False
            r, c = r + 1, c + 1
        return True