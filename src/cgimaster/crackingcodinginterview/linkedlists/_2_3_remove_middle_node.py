from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def delete_middle_node(ll):
    if ll is None or ll.next is None: return None
    p,c,r = None,ll,ll
    while r is not None:
        p,c,r = c, c.next, r.next
        if r is not None: r = r.next
    p.next = c.next
    return ll

assert to_list(delete_middle_node(create([1,2,3]))) == [1,2]
assert to_list(delete_middle_node(create([1,2,3,4,5,6,7,8,9,10]))) == [1,2,3,4,5,7,8,9,10]
assert to_list(delete_middle_node(create([1]))) == []