'''
Copyright 2018 Constantine Gurnov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import networkx as nx

from collections import deque

class TopologicalSort:
    order = None
    marked = None
    def dfs(self, g, v):
        self.marked[v]=True
        for vertex in g[v]:
            if not self.marked[vertex]: self.dfs(g,vertex)
        self.order.appendleft(v)

    def topologicalSort(self, g):
        self.order = deque([])
        self.marked = [False]*(len(g)+1)
        for vertex in g:
            if not self.marked[vertex]: self.dfs(g, vertex)
        return list(self.order)

class CCDiGraphKS:
    def __init__(self, g:nx.DiGraph):
        self.g, self.ids, self.count, visited = g, {}, 0, set()

        # self.reverseorder = self.reversesort(self.g)
        self.reverseorder = TopologicalSort().topologicalSort(self.g.reverse())

        def _dfs(v, ids, c):
            if v in visited: return
            visited.add(v)
            ids[v] = c
            for v2 in self.g[v]:
                _dfs(v2, ids, c)

        for v in self.reverseorder:
            if v in visited: continue
            _dfs(v, self.ids, self.count)
            self.count += 1
    #
    #
    # def reversesort(self, g):
    #     reverseg = g.reverse() #nx.DiGraph()
    #     reverseorder, visited = deque([]), set()
    #
    #     def ts_dfs(v):
    #         visited.add(v)
    #         for v2 in sorted(reverseg[v]):
    #             if not v2 in visited: ts_dfs(v2)
    #         reverseorder.appendleft(v)
    #
    #     for v in sorted(reverseg):
    #         if v in visited: continue
    #         ts_dfs(v)
    #     return list(reverseorder)

    def same_sc(self,p,q):
        return self.ids[p] == self.ids[q]

    def strong_components(self):
        return self.count

g = nx.DiGraph()
g.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11,12])
g.add_edges_from([
    (0,5),
    (2,0),
    (2,3),
    (3,2),
    (3,5),
    (4,2),
    (4,3),
    (5,4),

    (6, 8),
    (8, 6),

    (9,10),
    (9,11),
    (10, 12),
    (11, 12),
    (12, 9),

    (0,1),

    (6,0),
    (6,4),
    (6,9),
    (7,6),
    (7,9),

    (11,4),

])

ksg = CCDiGraphKS(g)
print(ksg.strong_components())
print(ksg.ids)
print(ksg.reverseorder)