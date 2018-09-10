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
    visited = None
    def dfs(self, g, v):
        self.visited[v]=True
        for vertex, cost in g[v]:
            if not self.visited[vertex]: self.dfs(g, vertex)
        self.order.appendleft(v)

    def topologicalSort(self, g):
        self.order = deque([])
        self.visited = [False] * (len(g) + 1)
        for vertex in g:
            if not self.visited[vertex]: self.dfs(g, vertex)
        return list(self.order)

    def shortestPath(self, g, s):
        dist = {}
        for i in g: dist[i]=float('inf')
        dist[s] = 0
        stack = self.topologicalSort(g)

        while stack:
            i = stack.pop(0)
            for node, weight in g[i]:
                if dist[node] > dist[i] + weight: dist[node] = dist[i] + weight

        for i in g: print("{} - {}".format(i,dist[i]))


g = {
    0:[(1,2),(2,1),(5,1.5)],
    1:[(4,7)],
    2:[],
    3:[(2,3),(4,1),(5,2.5),(6,11)],
    4:[],
    5:[(2,4)],
    6:[(0,7),(4,3.5)]
}

print(Soltion().topologicalSort(g))
print(Soltion().shortestPath(g,3))

'''
[3, 6, 0, 5, 2, 1, 4]
0 - 18
1 - 20
2 - 3
3 - 0
4 - 1
5 - 2.5
6 - 11
None
'''