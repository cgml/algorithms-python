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
from collections import defaultdict

def build_graph(edges):
    G, V = defaultdict(defaultdict), set()
    for v1,v2,w in edges:
        G[v1][v2]=w
        V.add(v1)
        V.add(v2)
    return G, V

edges = [
(0, 1, -1)
,(0, 2, 4)
,(1, 2, 3)
,(1, 3, 2)
,(1, 4, 2)
,(3, 2, 5)
,(3, 1, 1)
,(4, 3, -3)
]
G, V = build_graph(edges)



def check_cycle(graph, distance):
    for v1 in graph:
        for v2 in graph[v1]:
            c = graph[v1][v2]
            if distance[v2] > distance[v1]+c: return True
    return False

def build_path(graph,prev):
    next = {}
    for v in prev: next[prev[v]]=v #create dict with inverse previous
    path = [next[None]] #init path with start node. must be equal to 's'
    #execute while last element of the path is in next (not none?),
    #and next mapped node not already in path (to avoid cycles)
    total_cost = 0
    while path[-1] in next and next[path[-1]] not in path:
        path, total_cost = path+[next[path[-1]]], total_cost+graph[path[-1]][next[path[-1]]]
    return path, total_cost


def bellman_ford(graph, vertices, s):
    distance, prev = {}, {}
    for v in vertices: distance[v], prev[v] = float('inf'), None
    distance[s]=0

    for _ in range(len(vertices)):
        for v1 in graph:
            for v2 in graph[v1]:
                c = graph[v1][v2]
                if distance[v2] > distance[v1]+c: distance[v2], prev[v2] = distance[v1]+c, v1

    neg_cycle = check_cycle(graph, distance)
    path = ([], 0) if neg_cycle else build_path(graph,prev)
    return neg_cycle, distance, path

print(bellman_ford(G, V, 0))