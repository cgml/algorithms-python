def findCriticalConnections(noOfServers, noOfConnections, connections):
    # Write your code here
    g = {s: set() for s in range(noOfServers)}
    for c in connections:
        g[c[0]].add(c[1])
        g[c[1]].add(c[0])

    cc = set()

    class TS:
        value = None

    ts = TS()
    ts.value = 0

    def dfs(v):
        ts.value += 1
        ar[v] = ts.value
        upper = ar[v]
        for n in g[v]:
            if n not in visited:
                visited.add(n)
                parent[n] = v
                upper = min(upper, dfs(n))
            else:
                if n != parent[v]:  # not parent node
                    upper = min(upper, ar[n])
        if upper == ar[v] and parent.get(v) != -1:
            cc.add((parent[v], v))
        ts.value += 1
        dep[v] = ts.value
        return upper

    root = 0
    parent, visited, ar, dep = {root: -1}, set(), {}, {}
    visited.add(root)
    dfs(root)
    return cc if cc else [[-1, -1]]