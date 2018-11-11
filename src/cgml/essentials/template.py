from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

def build_graph(edges):
    G = defaultdict(defaultdict)
    for l, r, cost in edges: G[l][r]=cost
    return G

edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("C", "A", 1),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]

DWGdict = build_graph(edges)


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


'''
Template for implementation of core algorithms:

DATA STRUCTURES:
    
    PRIMITIVE: (5)
        Primes, Sqrt, Pow, Mult, Div
    
    PLAIN: (24)
        Two Pointer (reverse words)
        Search * Select: Binary Search, QuickSelect
        Patterns: KMP, Robin Karp,
        Sort: Quick, Merge, Radix, LSD, MSD
        UF
        Suffix Arrays
        Subsum / Subproduct / Avg. / Min / Max / Mult 
    
    1F: (2)
        Heap, Priority Queue
        
    K-V: (15)
        BST (Search, Closest, Prev/Next), Range Search, Segment Tree, Interval Tree
        BIT/Fenwick Tree
        KD-Tree, B-Tree
        RB-Tree
        Sweep-line - line intersections, Sweep-line - Rectangles intersection
        Hash Map (hash code, collisions), Bloom Filters
        Trie
        
    GRAPHS: (14)
        Traversal: DFS, BFS, Inter.  DFS
        Sort: Topological Sort
        Connectivity: UF, SCC - Kosuraju
        Shortest Paths: BFS, Topological Sort, Dijkstra, Bellman-Ford, A*
        MST: Kruskal's, Prim's
        Max-Flow/Min-Cut: Ford-Fulkerson (Edmund's - Karp), Bipartite Matchinng / Job Matching 
        
---
PARADIGMS:
    PRIMITIVES & STRINGS:
        Anagram search
        Median in Stream
    
    D&Q:
        TBD
    
    GREEDY:
        TBD
        
    Backtracking:
        N-Queens
        Sudoku check, Sudoku solve
        Paranthesis
            
    DP:
        Coin change
        Min edit distance
        Knapsack 0/1
        Stock Trading

    BRANCH & BOUND:
        TBD
'''

import heapq

def max_flow(G, s, t):
    '''

    :param G:
    :param s:
    :param t:
    :return: - maxflow int
    '''

def min_cut(G, s, t):
    '''

    :param G:
    :param s:
    :param t:
    :return: - min cut edges
    '''
    pass

def max_flow_min_cut_algorithm():
    draw_graph(DWGnet)
    max_flow(DWGnet, 'A', 'H')
    draw_graph(DWGnet)
    mincut_edges = min_cut(DWGnet, 'A','H')
    for v1, v2, c in mincut_edges: print('{} -> {} - capacity: {}'.format(v1, v2, c))

max_flow_min_cut_algorithm()