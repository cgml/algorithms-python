class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for lidx in range(len(matrix)//2):
            #lidx = 1, N = 4, LN = 2, N-lidx-1 = 2
            #itemidx [1]
            for itemidx in range(lidx, N-lidx-1): # from beginning layer to end layer -1 e.g. if N = 10, L=1, [1,7] last element (10-1)-1 layer -1 element
                #itemidx = 1
                #iA (top horizontal), iB (right vertical top - down), #iC (down horizontal, right to left), #iD (left vertical, down to up)
                #iA -> iB -> iC -> iD -> iA
                iA = (lidx,itemidx) #1,1
                iB = (itemidx , N-lidx-1)
                iC = (N-lidx-1, N-1-itemidx)
                iD = (N-1 -itemidx, lidx)
                tmpiA=matrix[iA[0]][iA[1]] #store iA to tmpiA
                matrix[iA[0]][iA[1]]=matrix[iD[0]][iD[1]] #put iD to iA
                matrix[iD[0]][iD[1]]=matrix[iC[0]][iC[1]] #put iC to iD
                matrix[iC[0]][iC[1]]=matrix[iB[0]][iB[1]] #put iB to iC
                matrix[iB[0]][iB[1]]=tmpiA #matrix[tmpiA[0]][tmpiA[1]] #put tmpiA to iB