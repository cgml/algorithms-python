from cgimaster.general._4_graphs._0_toolset import *


def bfs(g,start, target):
    front = [start]
    visited = set()
    while front:
        next_node = front.pop(0)
        if target == next_node: return target
        if next_node in visited: continue
        visited.add(next_node)
        front += [k for k in g.nodes[next_node].connections]
    return None


print(bfs(GraphUtils.ugraph_from_list([(1,2),(1,3),(1,4),(2,5),(5,7),(7,6),(6,8)]),1,8))

