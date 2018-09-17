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

'''
Union Find
 Time Complexity - O(V log * V)

'''

import networkx as nx

class UF:
    def __init__(self, g):
        self.ids, self.sz = {}, {}
        for v in g: self.ids[v], self.sz[v] = v, 1

    def _root(self, p):
        while self.ids[p] != p:
            self.ids[p] = self.ids[self.ids[p]] # path compression
            p = self.ids[p]
        return p

    def find(self, p, q):
        return self._root(p) == self._root(q) # nodes are connected if have same roots

    def union(self, p, q):
        proot, qroot = self._root(p), self._root(q)
        if proot == qroot: return
        # put smaller tree below larger one and update size of larger one
        if self.sz[proot] <= self.sz[qroot]: self.ids[proot], self.sz[qroot] = qroot, self.sz[qroot]+self.sz[proot]
        else: self.ids[qroot], self.sz[proot] = proot, self.sz[proot]+self.sz[qroot]

g = nx.Graph()
g.add_nodes_from('0123456')
g.add_edges_from([
    ('0','7',{'weight':0.16}),
    ('2','3',{'weight':0.17}),
    ('1','7',{'weight':0.19}),
    ('0','2',{'weight':0.26}),
    ('5','7',{'weight':0.28}),
    ('1','3',{'weight':0.29}),
    ('1','5',{'weight':0.32}),
    ('2','7',{'weight':0.34}),
    ('4','5',{'weight':0.35}),
    ('1','2',{'weight':0.36}),
    ('4','7',{'weight':0.37}),
    ('0','4',{'weight':0.38}),
    ('6','2',{'weight':0.40}),
    ('3','6',{'weight':0.52}),
    ('6','0',{'weight':0.58}),
    ('6','4',{'weight':0.93})
])

if __name__ == '__main__':
    uf = UF(g)
    print(uf.find('0','7'),uf.find('7','3'))
    uf.union('0','7')
    uf.union('7','3')
    print(uf.find('0','3'))