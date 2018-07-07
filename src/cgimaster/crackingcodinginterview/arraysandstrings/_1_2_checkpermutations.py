def check_perm(s1,s2):
    if s1 is None or s2 is None or len(s1) != len(s2): return False
    d = {}
    for c in s1: d[c]=d.get(c,0)+1
    for c in s2:
        if d.get(c,0)-1<0: return False
        updated = d.get(c,0)-1
        if updated > 0: d[c]=updated
        else: del d[c]

    return not d

assert not check_perm("aba","abc")
assert check_perm("aba","aab")
assert check_perm("","")
