'''
Goal: Is v connected to w in constant time. (Vertices v and w are connected if there is a path between them)

Adj. matrix is not good solution for large graphs
'''

class ConnectedComponents:
    marked = None
    cc = None
    _count = None

    def connected_components(self, G):
        self.marked = [False]*len(G)
        self.cc = [None]*len(G)
        self._count = 0
        for v in G:
            if not self.marked[v]:
                self.dfs(G, v)
                self._count += 1

    def dfs(self, G, v):
        if self.marked[v]: return
        self.marked[v] = True
        self.cc[v] = self._count
        for w in G[v]: self.dfs(G, w)

    def count(self):
        return self._count

    def connected(self, v, w):
        return self.cc[v]==self.cc[w]

    def component(self, v):
        return self.cc[v]