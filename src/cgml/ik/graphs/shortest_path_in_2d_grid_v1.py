# Complete the function below.
from collections import deque


def find_shortest_path(grid):
    A = ord('A')
    Z = ord('Z')
    a = ord('a')
    z = ord('z')
    N = len(grid)
    M = len(grid[0])

    def _checkstate(cr, cc, ckeys):
        if cr < 0 or cr == N or cc < 0 or cc == M:
            return None
        if grid[cr][cc] == '#':
            return None
        o = ord(grid[cr][cc])
        if A <= o and o <= Z:
            if (1 << o - A) & ckeys != 0:
                return ckeys
            else:
                return None
        if a <= o and o <= z:
            ckeys = (1 << o - a) | ckeys
        return ckeys

    sr, sc = -1, -1

    for r in range(N):
        for c in range(M):
            if grid[r][c] == '@':
                sr, sc = r, c
                break
    path = []
    q = deque([(sr, sc, 0, [])])
    visited = set()
    while q:
        cr, cc, ckeys, cpath = q.popleft()
        if (cr, cc, ckeys) in visited:
            continue
        newpath = cpath + [(cr, cc)]
        visited.add((cr, cc, ckeys))
        if grid[cr][cc] == '+':
            return newpath
        for (nr, nc) in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
            updatedkeys = _checkstate(nr, nc, ckeys)
            if updatedkeys is not None and (nr, nc, updatedkeys) not in visited:
                q.append((nr, nc, updatedkeys, newpath))
    return None
