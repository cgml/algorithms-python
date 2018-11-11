class Solution:
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

class Solution2:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n: A, B, m, n = B, A, n, m

        l, r, half_len = 0, m, (m + n + 1) // 2
        while l <= r:
            i = (l + r) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                l = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                r = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

print(Solution().findMedianSortedArrays([1, 3],[2]), 2.0)
print(Solution().findMedianSortedArrays([1, 2],[3,4]), 2.5)
print(Solution().findMedianSortedArrays([1, 3, 8, 9, 15],[7,11,18,19,21,25]), 11)


