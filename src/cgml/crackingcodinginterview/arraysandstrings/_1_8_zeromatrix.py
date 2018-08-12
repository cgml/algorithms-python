def zero_matrix(m):
    for r in range(1,len(m)):
        for c in range(1,len(m[0])):
            if m[r][c]==0:
                m[r][0], m[0][c] = 0, 0
    for r in range(0,len(m)):
        if m[r][0] == 0: zero_row(m,(r,0))
    for c in range(0,len(m[0])):
        if m[0][c] == 0: zero_col(m,(0,c))
    return m

def zero_row(m,z):
    for c in range(len(m[0])):
        m[z[0]][c]=0

def zero_col(m,z):
    for r in range(len(m)):
        m[r][z[1]]=0


def zero_matrix_additional_space(m):
    zidx = []
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c]==0: zidx.append((r,c))
    for z in zidx:
        zero_row(m,z)
        zero_col(m,z)
    return m



print(zero_matrix([[1,1,1],[1,1,1],[1,0,1]]))
assert zero_matrix([[1,1,1],[1,1,1],[1,0,1]]) == [[1,0,1],[1,0,1],[0,0,0]]