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

import heapq
from collections import defaultdict

def build_graph(edges):
    g = defaultdict(list)
    for l, r, cost in edges: g[l].append((r,cost))
    return g

def dijkstra(g, start, target):
    queue, distance_to, visited = [(0,[start])], {start:0}, set()
    while queue:
        cost, path = heapq.heappop(queue)
        if path[-1] == target: return (cost,path)
        if path[-1] in visited: continue
        visited.add(path[-1])
        for node, front_cost in g.get(path[-1],[]):
            if node in visited: continue
            if distance_to.get(node, float('inf')) > cost + front_cost:
                distance_to[node]=cost+front_cost
                heapq.heappush(queue,(cost+front_cost,path+[node]))
    return (float('inf'),None)


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

print("A -> E:")
print(dijkstra(build_graph(edges), "A", "E"))
print("F -> G:")
print(dijkstra(build_graph(edges), "F", "G"))
print("F -> Z:")
print(dijkstra(build_graph(edges), "F", "Z"))