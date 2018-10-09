class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        R, C = len(matrix), len(matrix[0])
        result, r1,r2,c1,c2 = [], 0, R-1, 0, C-1
        while r1<=r2 and c1<=c2:
            for cidx in range(c1,c2+1): result.append(matrix[r1][cidx])
            for ridx in range(r1+1,r2+1): result.append(matrix[ridx][c2])
            if r1<r2:
                for cidx in range(c1,c2)[::-1]: result.append(matrix[r2][cidx])
            if c1<c2:
                for ridx in range(r1+1,r2)[::-1]: result.append(matrix[ridx][c1])
            r1, r2, c1, c2 = r1+1, r2-1, c1+1, c2-1
        return result