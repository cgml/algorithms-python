def hasCycle(N, M, edges):
    # Write your code here
    g = {n: set() for n in range(N)}
    for f, t in edges:
        g[f].add(t)
    parent, visited, ar, dep = {}, set(), {}, {}

    class TS:
        value = 0

    ts = TS()

    def dfs(v):
        ts.value += 1
        ar[v] = ts.value
        for n in g[v]:
            if n not in visited:
                visited.add(n)
                if dfs(n):
                    return True
            else:
                if not dep.get(n):
                    return True
        dep[v] = ts.value

    for v in g:
        if v not in visited:
            if dfs(v):
                return True
    return False