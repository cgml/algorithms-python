from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def return_kth_to_last(ll,K):
    if ll is None: return ll
    k,c,r = 0,ll,ll
    while k<K and r is not None: r,k = r.next, k+1
    if k<K: return None
    while r is not None: c,r = c.next, r.next
    return c
assert return_kth_to_last(create([0,1,2,3,4,5,6,7]), 2).data == 6
assert return_kth_to_last(create([0,1,2,3,4,5,6,7]), 12) == None