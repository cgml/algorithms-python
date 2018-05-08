def rotateImageA(a):
    return [list(m[::-1]) for m in zip(*a)]

def rotateImageB(a):
    n = len(a)
    for i in range(0,n):
        for j in range(0, n):
            a[i][j] += (a[n-j-1][i] % 10**5) * (10**5)

    for i in range(0, n):
        for j in range(0, n):
            a[i][j] //= 10 ** 5

    return a

assert rotateImageA([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
assert rotateImageB([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]