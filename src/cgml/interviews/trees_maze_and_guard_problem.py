'''
Given a matrix of chars with 3 possible entries: 'O' for room, 'X' for wall and 'G' for guard,
return the set of rooms that are farthest from any guard.
The guards only move vertically and horizontally ( not diagonally).
'''

from collections import deque
import numpy as np

def _helper_bfs(maze, r, c):
    R = len(maze)
    C = len(maze[0])
    mem = [[float('inf')]*C for _ in range(R)]
    queue = [(r,c,0)]
    visited = set()
    for cr,cc,cnt in queue:
        if cr < 0 or cc < 0 or cr >= R or cc >= C: continue
        if (cr,cc) in visited: continue
        visited.add((cr,cc))
        if maze[cr][cc] == 'X':continue
        mem[cr][cc]=cnt
        queue.append((cr-1,cc,cnt+1))
        queue.append((cr,cc-1,cnt+1))
        queue.append((cr+1,cc,cnt+1))
        queue.append((cr,cc+1,cnt+1))
    return mem

def max_distance_from_guards(maze):
    R, C = len(maze), len(maze[0])
    mem = np.min(np.dstack([_helper_bfs(maze,r,c) for r in range(R) for c in range(C) if maze[r][c] == 'G']), axis=2)
    mem = np.vectorize(lambda x: x if x < float('inf') else -1)(mem)
    print(mem)
    maxdistance = np.max(mem)
    result = set([(r,c) for r in range(R) for c in range(C) if mem[r][c]==maxdistance])
    return result

maze = [
    ['O','O','O','X','O'],
    ['O','O','G','X','O'],
    ['O','O','O','X','G'],
    ['O','O','O','X','O'],
    ['O','O','G','O','O'],
    ['O','O','O','O','O'],
]

assert max_distance_from_guards(maze) == {(0,0),(2,0),(3,0),(5,0),(5,4)}