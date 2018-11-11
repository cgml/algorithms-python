class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = None
        if not matrix or not matrix[0]: return
        self.matrix, R, C = matrix, len(matrix), len(matrix[0])
        self.m = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
        for c in range(C):
            for r in range(R):
                self.m[r + 1][c + 1] = self.m[r][c + 1] + self.m[r + 1][c] - self.m[r][c] + self.matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # return self._brute_force(row1, col1, row2, col2)
        if not self.matrix: return 0
        return self.m[row2 + 1][col2 + 1] - self.m[row2 + 1][col1] - self.m[row1][col2 + 1] + self.m[row1][col1]

    def _brute_force(self, row1, col1, row2, col2):
        return sum([self.matrix[r][c] for r in range(row1, row2 + 1) for c in range(col1, col2 + 1)])