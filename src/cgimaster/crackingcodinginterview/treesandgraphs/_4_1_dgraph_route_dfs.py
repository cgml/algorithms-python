def dfs(g,s,t):
    q,v = [s],set()
    while q:
        node = q.pop()
        if node==t: return True
        if node in v: continue
        q,v = q+list(reversed(g.get(node,[]))), v.union([node])
    return False

g = {   '1': ['2', '3', '4', '12'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '13':[]
    }


assert dfs(g,'1','12')
assert not dfs(g,'1','13')
