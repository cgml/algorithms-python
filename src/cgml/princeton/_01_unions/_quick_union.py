from ._union_find import *

'''
Find: O(n)
Union: O(n) - worst
'''

class QuickUnion(UnionFind):

    def _root(self, p):
        while self.ids[p] != p: p = self.ids
        return p

    def find(self, p:int, q:int) -> bool:
        return self._root(p) == self._root(q)

    def union(self, p:int, q:int):
        proot = self._root(p)
        qroot = self._root(q)
        self.ids[proot] = qroot

'''
Modified version of quick union, where algorithm avoid building tall trees by counting number of elements in trees
And during union - smaller tree goes below bigger

Find: O(logn)
Union: O(logn)

'''

class WeightedQuickUnion(UnionFind):
    def __init__(self, N):
        super().__init__(N)
        self.sz = [1]*N

    def _root(self, p):
        while self.ids[p] != p: p = self.ids[p]
        return p

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p:int, q:int):
        proot = self._root(p)
        qroot = self._root(q)
        if proot == qroot: return
        if self.sz[proot] <= self.sz[qroot]: self.ids[proot], self.sz[qroot] = qroot, self.sz[qroot]+self.sz[proot]
        else: self.ids[qroot], self.sz[proot] = proot, self.sz[proot]+self.sz[qroot]


'''
WQUPC - almost linear in practice

Find: 
Union: O(N + M lg* N )
'''
class WeightedQuickUnionWithPathCompression(WeightedQuickUnion):
    def __init__(self, N):
        super().__init__(N)

    def _root(self, p):
        while self.ids[p] != p:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
