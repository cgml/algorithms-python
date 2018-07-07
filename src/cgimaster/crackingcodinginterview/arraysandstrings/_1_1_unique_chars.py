def all_unique_dict(s):
    d = {}
    for c in s:
        if d.get(c) != None: return False
        d[c]=c
    return True

def all_unique_sort(s):
    l = list(s); l.sort()
    ssorted = "".join(l)
    for idx in range(0,len(ssorted)-1):
        if ssorted[idx]==ssorted[idx+1]: return False
    return True


for f in [all_unique_dict,all_unique_sort]:
    print("checking {}".format(f.__name__))
    assert not f("abca")
    assert f("abc")
    assert f("abcA")
    assert f("abcA ")