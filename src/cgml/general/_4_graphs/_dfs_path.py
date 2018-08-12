def dfs(g,s,t,v=set()):
    if s==t: return [s]
    if s in v: return None
    v.add(s)
    for n in g.get(s,[]):
        path = dfs(g,n,t,v)
        if path is not None: return [s]+path

result = dfs(g = {
        '1': ['2', '3', '4', '12'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        },
    s='1',
    t='12')

assert result == ['1', '4', '7', '12']