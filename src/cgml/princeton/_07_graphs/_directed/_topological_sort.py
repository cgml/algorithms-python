'''
Topological Sort works on DAGs only.

Problem example - Precedence scheduling:

    Goal: Given set of tasks to be completed with precedence constraints, in which order shall we schedule tasks
    Digraph model: vertex = task, edge precedence constraint

    Solution: DFS
'''

from collections import deque

class Soltion:
    order = None
    marked = None
    def dfs(self, g, v):
        self.marked[v]=True
        for vertex in sorted(g[v]):
            if not self.marked[vertex]: self.dfs(g,vertex)
        self.order.appendleft(v)

    def topologicalSort(self, g):
        self.order = deque([])
        self.marked = [False]*(len(g)+1)
        for vertex in sorted(g):
            if not self.marked[vertex]: self.dfs(g, vertex)
        return list(self.order)


g = {
    0:[1,2,5],
    1:[4],
    2:[],
    3:[2,4,5,6],
    4:[],
    5:[2],
    6:[0,4]
}

print(Soltion().topologicalSort(g))