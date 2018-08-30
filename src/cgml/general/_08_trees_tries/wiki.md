## DFS Implementation

Recursive Python implementation of DFS, which returns full path from initial to target vertex with Time Complexity O(n) and additional Space Complexity O(n)<br>
Input: A graph g - (can be represented as python dict with vertices as keys and list of adjacent vertices as values), s - initial vertex, t - target vertex, v - visited vertices (initially None)<br>
Output: Path from s to t as a list, or None if target vertex is unreachable from s<br>

    def dfs(g,s,t,v=None):
        if s==t: return [s]
        if v is None: v = set()
        if s in v: return None
        v.add(s)
        for n in g.get(s,[]):
            path = dfs(g,n,t,v)
            if path is not None: return [s]+path

Technically this implementation has Time Complexity O(n + k^2) due to path concatenation, where k is length of path. Though in practice the path is much smaller than a graph which makes k^2 << n, and overall time complexity is O(n). In case when graph has long paths it can be addressed by reversed concatenation with amortized time O(k) and additional final reverse operation with O(k). Where k by definition is less or equal n, which will guarantee linear time complexity.

    from collections import deque
    def dfs(g,s,t,v=None):
        if s==t: return deque([s])
        if v is None: v = set()
        if s in v: return None
        v.add(s)
        for n in g.get(s,[]):
            path = dfs(g,n,t,v)
            if path is not None:
                path.appendleft(s)
                return path

