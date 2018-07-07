def sudoku2_A(grid):
    for i in range(9):
        dv = {}
        dh = {}
        for j in range(9):
            if grid[i][j] != '.':
                if dh.get(grid[i][j], None) != None:
                    return False
                else:
                    dh[grid[i][j]] = True
            if grid[j][i] != '.':
                if dv.get(grid[j][i], None) != None:
                    return False
                else:
                    dv[grid[j][i]] = True

    for k in range(3):
        for m in range(3):
            dsq = {}
            for i in range(3):
                for j in range(3):
                    if grid[k * 3 + i][m * 3 + j] != '.':
                        if dsq.get(grid[k * 3 + i][m * 3 + j], None) != None:
                            return False
                        else:
                            dsq[grid[k * 3 + i][m * 3 + j]] = True
    return True


def sudoku2_B(grid):
    def unique(G):
        G = [x for x in G if x != '.']
        return len(set(G)) == len(G)

    def groups(A):
        B = list(zip(*A))
        for v in range(9):
            yield A[v]
            yield B[v]
            yield [A[v / 3 * 3 + r][v % 3 * 3 + c] for r in range(3) for c in range(3)]

        return all(unique(grp) for grp in groups(grid))


grid1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

grid2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

assert sudoku2_A(grid1)
assert not sudoku2_A(grid2)

assert sudoku2_B(grid1)
assert not sudoku2_B(grid2)