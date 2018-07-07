def bibfs(g,s,t):
    q1,q2,v1,v2=[[s]],[[t]],set(),set()
    while q1 or q2:
        if q1:
            n1=q1.pop(0)
            if n1 in q2 or n1 in v2: return True
            if n1 not in v1: v1,q1 = v1.union([n1]), q1+g.get(n1,[])
                # v1.add(n1)
                # q1+=[v for v in g.get(n1,[])]
        if q2:
            n2=q2.pop(0)
            if n2 in q1 or n2 in v1: return True
            if n2 not in v2: v2,q2 = v2.union([n2]), q2+g.get(n2,[])
    return False

g = {   '1': ['2', '3', '4'],
        '2': ['1', '5', '6'],
        '3': ['1'],
        '4': ['1','7','8'],
        '5': ['2', '9', '10'],
        '6': ['2'],
        '7': ['4','11', '12'],
        '8': ['4'],
        '9': ['5'],
        '10':['5'],
        '11': ['7'],
        '12':['7'],
        '13':['14'],
        '14':['13'] }

print( bibfs(g, s='1', t='12') )
assert not bibfs(g, s='1', t='14')