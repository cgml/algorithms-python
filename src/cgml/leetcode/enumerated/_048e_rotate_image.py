class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        LN = len(matrix)//2
        for lidx in range(LN):
            for itemidx in range(lidx, N-lidx-1):
                #TODO
                pass