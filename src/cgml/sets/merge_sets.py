def merge_sets(s):
    r = []
    for setx in s:
        found = False
        for out in r:
            if out.intersection(setx):
                out.update(setx)
                found = True
                break
        if not found: r.append(setx)
    if len(r) != len(s):
        del s
        r = merge_sets(r)
    return r
assert merge_sets([{1,2,3},{3,4},{5,6,7}]) == [{1,2,3,4},{5,6,7}]
assert merge_sets([{1,2,3},{3,4},{5,6,7},{1,5}]) == [{1,2,3,4,5,6,7}]