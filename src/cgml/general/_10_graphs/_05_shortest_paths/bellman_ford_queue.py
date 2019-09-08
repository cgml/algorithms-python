from collections import defaultdict, deque
from sys import maxsize

def build_graph(edges):
    G, V = defaultdict(list), set()
    for v1,v2,w in edges:
        G[v1].append((v2,w))
        V.add(v1)
        V.add(v2)
    return G, V

def check_cycles_queue(graph, distance):
    for v1 in graph:
        for v2 in graph[v1]:
            c = graph[v1][v2]
            if distance[v2] > distance[v1]+c: return True
    return False

def build_path(previous):
    next = {}
    for k in previous: next[previous[k]] = k
    path = [next[None]]
    while path[-1] in next and next[path[-1]] not in path: path.append(next[path[-1]])
    return path

def bellman_ford_queue(G, V, start):
    idx, distance, previous = 0, {}, {}
    for node in V: distance[node], previous[node] = maxsize, None
    distance[start] = 0
    queue = deque([start])
    while queue:
        v1 = queue.pop()
        for v2, w in G[v1]:
            if distance[v2] > distance[v1] + w:
                distance[v2], previous[v2] = distance[v1] + w,  v1
                if v2 not in queue: queue.append(v2)
            idx += 1
            #if idx % len(V) == 0 and check_cycles_queue(G,distance): return (True, distance, previous, [])

    has_cycles = check_cycles_queue(G,distance)

    path = [] if has_cycles else build_path(previous)
    return (has_cycles, distance, previous, path)

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
print(bellman_ford_queue(G, V, 0))