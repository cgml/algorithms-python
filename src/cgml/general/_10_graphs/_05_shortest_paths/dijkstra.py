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