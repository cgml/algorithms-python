def rotate_point(m,idx,L):
    N = len(m)
    tmp = m[L][idx]
    m[L][idx]=m[N-idx-1][L]
    m[N-idx-1][L]=m[N-L-1][N-idx-1]
    m[N-L-1][N-idx-1]=m[idx][N-L-1]
    m[idx][N-L-1]=tmp
    # m[L][idx],m[N-idx-1][L],m[N-L-1][N-idx-1],m[idx][N-L-1]=m[N-idx-1][L],m[N-L-1][N-idx-1],m[idx][N-L-1],m[L][idx]

def rotate_matrix(m):
    N = len(m)
    for L in range(int(N/2)):
        for idx in range(L,N-L-1):
            rotate_point(m,idx,L)
    return m

m1 = [[1,2,3],[4,5,6],[7,8,9]]
out1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
out2 = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

assert rotate_matrix(m1)==out1
assert rotate_matrix(m2)==out2
