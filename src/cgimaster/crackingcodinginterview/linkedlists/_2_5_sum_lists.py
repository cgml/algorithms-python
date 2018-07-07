from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def reverse2(ll):
    if ll is None: return None
    p, c = None, ll
    while c is not None: p, c.next, c = c, p, c.next
    return p

def sum_lists(ll1,ll2):
    rll1, rll2 = reverse2(ll1), reverse2(ll2)
    out, cl1, cl2 = LLNode(0), rll1, rll2
    cbuf=out
    while cl1 is not None or cl2 is not None:
        if cl1 is not None: cbuf.data, cl1 = cbuf.data+cl1.data, cl1.next
        if cl2 is not None: cbuf.data, cl2 = cbuf.data+cl2.data, cl2.next
        cbuf.data, cbuf.next = cbuf.data % 10, LLNode(int(cbuf.data/10))
        cbuf = cbuf.next
    ll1 = reverse2(rll1)
    ll2 = reverse2(rll2)
    return reverse2(out)

print_ll(sum_lists(create([1,2,3,9,9,9]),create([9,9,9])))