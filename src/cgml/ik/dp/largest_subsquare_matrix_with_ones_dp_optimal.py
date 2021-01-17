def largest_sub_square_matrix(n, m, mat):
    # n, m = rows, cols
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 1:
                mat[i][j] = 1 + min(mat[i - 1][j], mat[i][j - 1], mat[i - 1][j - 1])
    max_len = 0
    for row in mat:
        max_len = max(max_len, max(row))
    return max_len