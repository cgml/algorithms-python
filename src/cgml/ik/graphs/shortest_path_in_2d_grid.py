'''
Given 2d maze, find shortest path from start to goal.
@ - start
+ - goal
. - land
# - water
A-Z - doors
a-z - keys
'''
from collections import deque


def find_shortest_path(grid):
    if not grid:
        return None
    R, C = len(grid), len(grid[0])
    rs, cs = None, None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@':
                rs, cs = r, c
                break
        if rs: break

    def _check_cell(r1, c1, keys):
        if r1 < 0 or r1 >= R or c1 < 0 or c1 >= C:
            return None
        v = grid[r1][c1]
        if v == '#':
            return None
        if ord(v) >= ord('a') and ord(v) <= ord('z'):
            return keys | 1 << ord(v) - ord('a')
        if ord(v) >= ord('A') and ord(v) <= ord('Z'):
            return keys if keys & 1 << ord(v) - ord('A') else None
        return keys

    q = deque([(rs, cs, 0, [])])
    visited = set()
    while q:
        r, c, keys, p = q.popleft()
        if (r, c, keys) in visited:
            continue
        newp = p + [(r, c)]
        if grid[r][c] == '+':
            return newp
        visited.add((r, c, keys))
        for r1, c1 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            updated_keys = _check_cell(r1, c1, keys)
            if updated_keys is not None:
                q.append((r1, c1, updated_keys, newp))
    return None