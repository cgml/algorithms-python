'''
Course Schedule
There are n courses to take, they are referred to by numbers from 0 to n-1. Some of them have prerequisites, e.g. courses A and B must be completed before course C can be taken (in other words, course C depends on A and B).
Find and return an ordering in which all the given courses can be taken while satisfying all the prerequisites. If there exists more than one such ordering, any one of them would be a correct answer. If no such ordering exists, return a special value.

Solution:
Topological sort on DAG with built in cycles detection

'''

def course_schedule(n, ps):
    graph = {}
    for v in range(n):
        graph[v] = []
    for p in ps:
        graph[p[0]] = graph.get(p[0], list()) + [p[1]]

    marked = set()
    visited = set()
    result = []

    def dfs(v):
        marked.add(v)
        visited.add(v)
        for v1 in graph[v]:
            if v1 in visited:
                return -1
            if v1 in marked: continue
            res = dfs(v1)
            if res == -1:
                return res
            result.append(v1)
        visited.remove(v)

    for v in graph:
        if v in marked: continue
        res = dfs(v)
        if res == -1:
            return [-1]
        result.append(v)

    return result