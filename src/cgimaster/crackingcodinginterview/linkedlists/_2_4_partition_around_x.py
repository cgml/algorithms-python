from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def partition_around_x(ll,x):
    if ll is None: return None
    c,ns,nx=ll,ll,ll
    while nx is not None and nx.data != x: nx = nx.next
    if nx.data != x: return ll
    ne = nx
    while c is not None:
        if c.data < nx.data: ns.next, ns = c, c.next
        else: ne.next, ne = c,c
        c = c.next
    ns.next, ne.next = nx, None

    return ll


def partition_around_x_opt(ll,x):
    if ll is None: return None
    pll, nl, nr, px, cx = None, ll, ll, ll, ll.next
    while cx is not None:
        if cx.data>x: px, cx = cx, cx.next
        elif cx.data<x:
            nl,nl.next,px.next,cx=cx,nl,cx.next,cx.next; if pll == None: pll = nl
        else: nr.next, nr.next.next, px.next, cx = cx, nr.next, cx.next, cx.next
    if ll.data > x: pll.next, px.next, px.next.next = ll.next, ll, None
    return nl

print_ll(partition_around_x_opt(create([7,8,9,5,1,2,3,4,5]),5))

#create([7,8,9,5,1,2,3,4,5])==[4,3,2,1,5,5,7,8,9]