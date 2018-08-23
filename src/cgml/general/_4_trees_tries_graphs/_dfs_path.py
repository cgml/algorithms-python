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

graph = {
        '1': ['2', '3', '4', '12'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }
result = list(dfs(g = graph, s='1', t='12'))
print(result)
assert result == ['1', '4', '7', '12']