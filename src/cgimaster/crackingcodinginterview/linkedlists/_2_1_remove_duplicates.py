from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def remove_duplicates(ll):
    if ll is None: return ll
    d, p, c = {}, None, ll
    while c is not None:
        if d.get(c.data) is not None: p.next, c = c.next, c.next
        else: d[c.data]=c; p,c=c,c.next
    return ll


assert to_list(remove_duplicates(create([1,2,3,4,1,1,2,7]))) == [1,2,3,4,7]
assert to_list(remove_duplicates(create([0,0,0,0,0,1,2,3,4]))) == [0,1,2,3,4]
