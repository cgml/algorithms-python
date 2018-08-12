def bfs(g,s,t):
    q,v = [s],set()
    while q:
        node = q.pop(0)
        if node==t: return True
        if node in v: continue
        q,v = q+g.get(node,[]), v.union([node])
    return False

g = {   '1': ['2', '3', '4', '12'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '13':[]
    }


assert bfs(g,'1','12')
assert not bfs(g,'1','13')
