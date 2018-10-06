class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[0 if v else 1 for v in reversed(row)] for row in A]

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print('Expected Output: [[1,0,0],[0,1,0],[1,1,1]]')