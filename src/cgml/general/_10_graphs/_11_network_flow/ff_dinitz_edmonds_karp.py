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
Maxflow / Mincut problem:
    Ford Fulkerson Algorithm implementation
    Dinitz, Edmond's - Karp version with 
    Best (Fattest) FS for Augmenting Path search

'''
import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

def augmenting_path(g, ug, s,t):
    q, visited = PriorityQueue(), set()
    q.put((-float('inf'),[s]))
    residual = float('inf')
    while q.queue:
        d, path = q.get()
        n = path[-1]
        if n in visited: continue
        visited.add(n)
        residual = min(residual, -d)
        if n == t: break
        for k in ug[n]:
            if k in visited: continue
            if g.has_edge(n,k) and g[n][k]['flow'] < g[n][k]['capacity']:
                d = g[n][k]['capacity']-g[n][k]['flow']
                q.put((-d, path + [k]))
            elif g.has_edge(k,n) and g[k][n]['flow'] > 0:
                d = g[k][path[-1]]['flow']
                q.put((-d, path+[k]))

    return (path, residual) if path[-1] == t else (path, None)

def ford_fulkerson(g,s,t):
    ug = g.to_undirected()
    maxflow = 0
    while True:
        path, residual = augmenting_path(g, ug, s, t)
        if not residual: break
        for v1, v2 in zip(path, path[1:]):
            if g.has_edge(v1,v2): g[v1][v2]['flow']+= residual
            else: g[v2][v1]['flow'] -= residual
        maxflow+=residual
    return maxflow

def mincut(g,s,t):
    path, residual = augmenting_path(g,g.to_undirected(),s,t)
    scut = sorted(path)
    mincutedges = [(v1,v2,g[v1][v2]['capacity']) for v1 in scut for v2 in g[v1] if v2 not in scut]
    return mincutedges

DWGnet = nx.DiGraph()
DWGnet.add_nodes_from('ABCDEFGH')
DWGnet.add_edges_from([
    ('A', 'B', {'capacity': 10, 'flow': 0}),
    ('A', 'C', {'capacity': 5, 'flow': 0}),
    ('A', 'D', {'capacity': 15, 'flow': 0}),

    ('B', 'C', {'capacity': 4, 'flow': 0}),
    ('B', 'E', {'capacity': 9, 'flow': 0}),
    ('B', 'F', {'capacity': 15, 'flow': 0}),

    ('C', 'D', {'capacity': 4, 'flow': 0}),
    ('C', 'F', {'capacity': 8, 'flow': 0}),

    ('D', 'G', {'capacity': 16, 'flow': 0}),

    ('E', 'F', {'capacity': 15, 'flow': 0}),
    ('E', 'H', {'capacity': 10, 'flow': 0}),

    ('F', 'G', {'capacity': 15, 'flow': 0}),
    ('F', 'H', {'capacity': 10, 'flow': 0}),

    ('G', 'C', {'capacity': 6, 'flow': 0}),
    ('G', 'H', {'capacity': 10, 'flow': 0})
])

layout = {
    'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
    'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
}

def draw_graph(graph):
    plt.figure(figsize=(12, 4))
    plt.axis('off')
    nx.draw_networkx_nodes(graph, layout, node_color='blue', node_size=500)
    nx.draw_networkx_edges(graph, layout, edge_color='black')
    nx.draw_networkx_labels(graph, layout, font_color='white')

    for u, v, e in graph.edges(data=True):
        label = '{} / {}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] < e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
        plt.text(x, y, label, size=14, color=color, horizontalalignment='center', verticalalignment='center')
    plt.show()

maxflow = ford_fulkerson(DWGnet, 'A', 'H')
draw_graph(DWGnet)
mincutedges = mincut(DWGnet, 'A', 'H')
print('Maxflow for graph: ', maxflow )
print('Mincut edges: ')
for v1, v2, c in mincutedges: print('{} -> {} - capacity: {}'.format(v1, v2, c))
