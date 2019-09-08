class Solution1:
    def findMedianSortedArrays(self, x, y):
        Nx, Ny = len(x), len(y)
        if Nx > Ny: x, y, Nx, Ny = y, x, Ny, Nx
        l, r, M = 0, Nx, (Nx+Ny+1)//2
        while l <= r:
            pX = (r + l) // 2
            pY = M - pX
            if pX < Nx and x[pX] < y[pY-1]: l = pX + 1
            elif pX > 0 and x[pX-1] > y[pY]: r = pX - 1
            else:
                ml = max(float('-inf') if pX == 0 else x[pX - 1], float('-inf') if pY == 0 else y[pY - 1])
                mr = min(float('inf') if pX == Nx else x[pX], float('inf') if pY == Ny else y[pY])
                return ml if (Nx + Ny)%2 else (ml + mr) / 2























class Solution:
    def findMedianSortedArrays(self, X, Y):
        Nx, Ny = len(X), len(Y)
        if Nx > Ny: X, Y, Nx, Ny = Y, X, Ny, Nx

        l, r, Nhalf = 0, Nx, (Nx + Ny + 1) // 2
        while l <= r:
            xi = (l + r) // 2
            yi = Nhalf - xi

            if xi < Nx and Y[yi - 1] > X[xi]:  l = xi + 1 # xi is too small, must increase it
            elif xi > 0 and X[xi - 1] > Y[yi]: r = xi - 1 # xi is too big, must decrease it
            else: # xi is perfect
                if xi == 0: max_of_left = Y[yi - 1]
                elif yi == 0: max_of_left = X[xi - 1]
                else: max_of_left = max(X[xi - 1], Y[yi - 1])

                if (Nx + Ny) % 2 == 1: return max_of_left

                if xi == Nx: min_of_right = Y[yi]
                elif yi == Ny: min_of_right = X[xi]
                else: min_of_right = min(X[xi], Y[yi])

                return (max_of_left + min_of_right) / 2.0

print(Solution1().findMedianSortedArrays([1, 3], [2]), 2.0)
print(Solution1().findMedianSortedArrays([1, 2], [3, 4]), 2.5)
print(Solution1().findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]), 11)


