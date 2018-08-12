from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def detect_loop(ll):
    if ll is None or ll.next is ll: return ll
    s,c,r = ll,ll,ll.next
    while c is not r: c,r = c.next, r.next.next
    c = c.next
    while s is not c: s,c = s.next, c.next
    return s


ll = create([1,2,3,4,5,6,7,8,9,10])
loop_node = ll.next.next.next.next
get_tail(ll).next = loop_node
assert detect_loop(ll) is loop_node