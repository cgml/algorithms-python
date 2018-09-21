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
import matplotlib.pyplot as plt
from queue import PriorityQueue

from collections import defaultdict

def floyd_warshall_apsp(g):
    N = len(g.nodes)
    A = [[[float('inf')] for k in range(N+1)] for j in range(N+1)]*(N+1)
    for v1 in g.nodes:
        A[v1][v1][0]=0
    for v1,v2 in g.edges:
        A[v1][v2]=g[v1][v2]['weight']

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                A[i][j][k-1]=min(A[i][j][k-1],A[i][k][k-1]+A[k][j][k-1])
    cycles = False
    for v in g:
        if A[v][v][N] < 0:
            cycles = True
            break
    return A if not cycles else None

g2 = nx.DiGraph()
g2.add_nodes_from([0,1,2,3,4,5])
g2.add_edges_from([
    (0, 1, {'weight': 0}),
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

print(floyd_warshall_apsp(g2))