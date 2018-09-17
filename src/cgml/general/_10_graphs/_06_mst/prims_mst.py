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

Kruskal's algorithm to compute MST
Works with Sparse Graphs

Time Complexity: O(E log E)
    heap add / delete O(log E) for E edges at most
Extra Space Complexity: O(E)
Eager implementation - maintain PQ with Vertices - +SC: O(V)

'''

import networkx as nx
from queue import PriorityQueue
from collections import deque
from cgml.general._10_graphs._03_connectivity_undigraphs.connected_components_uf import UF


def prims_mst(g):
    pq, mst, visited = PriorityQueue(), deque([]), set()

    def visit(v1):
        visited.add(v1)
        for v1, v2 in [(v1,v2) for v2 in g[v1] if v2 not in visited]:
            pq.put((g[v1][v2]['weight'], v1, v2))

    visit(list(g.nodes)[0])
    while pq.queue:
        w, v1, v2 = pq.get()
        if v1 in visited and v2 in visited: continue
        mst.append((v1, v2, w))
        if v1 not in visited: visit(v1)
        if v2 not in visited: visit(v2)

    return list(mst), sum([w for _ ,_ , w in mst])

if __name__ == '__main__':
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

    mst = prims_mst(g)
    print('MST: {}. Value {}'.format(*mst))