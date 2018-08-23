def dfs(g,s,t,v=set()):
    if s==t: return True
    if s in v: return False
    v.add(s)
    for n in g.get(s,[]):
        if dfs(g,n,t,v): return True
    return False

g = {   '1': ['2', '3', '4', '12'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '13':[]
    }

assert dfs(g, s='1', t='12')
assert not dfs(g, s='12', t='13')
