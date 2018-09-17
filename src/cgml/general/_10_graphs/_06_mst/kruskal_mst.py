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
    build pq O(E)
    heap delete O(log E) for E edges
    uf - O(V log * V)

'''

import networkx as nx
from queue import PriorityQueue
from collections import deque
from cgml.general._10_graphs._03_connectivity_undigraphs.connected_components_uf import UF


def kruskal_mst(g):
    pq, mst = PriorityQueue(), deque([])
    for v1,v2 in g.edges: pq.put((g[v1][v2]['weight'],v1,v2))
    uf = UF(g)
    while pq.queue and len(mst) < len(g):
        w, v1, v2 = pq.get()
        if not uf.find(v1, v2):
            uf.union(v1,v2)
            mst.append((v1,v2,w))

    return list(mst), sum([w for _,_,w in mst])

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

mst = kruskal_mst(g)
print(mst)