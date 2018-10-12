class Solution:
    def setZeroes(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not m or not m[0]: return m
        R, C = len(m), len(m[0])

        r0, c0 = False, False
        for r in range(R):
            if m[r][0] == 0:
                r0 = True
                break

        for c in range(C):
            if m[0][c] == 0:
                c0 = True
                break

        for r in range(1, R):
            for c in range(1, C):
                if m[r][c] == 0: m[r][0], m[0][c] = 0, 0

        for r in range(1, R):
            if m[r][0] == 0:
                for c in range(1, C): m[r][c] = 0
        for c in range(1, C):
            if m[0][c] == 0:
                for r in range(1, R): m[r][c] = 0

        if r0:
            for r in range(R): m[r][0] = 0
        if c0:
            for c in range(C): m[0][c] = 0

