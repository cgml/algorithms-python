from cgimaster.crackingcodinginterview.linkedlists._0_toolset import *

def intersection_node(ll1,ll2):
    if ll1 is None or ll2 is None: return None
    p1,c1,cnt1,p2,c2,cnt2 = None,ll1,0,None,ll2,0
    while c1 is not None: p1,c1,cnt1 = c1,c1.next,cnt1+1
    while c2 is not None: p2,c2,cnt2 = c2,c2.next,cnt2+1
    if p1 is not p2: return None
    cn, c1, c2 = abs(cnt1-cnt2), ll1, ll2
    while c1 is not c2:
        if cnt1 > cnt2 and cn > 0: cn,c1 = cn-1,c1.next
        elif cnt1 < cnt2 and cn > 0: cn,c2 = cn-1,c2.next
        else: c1,c2=c1.next,c2.next
    return c1


ll1 = create([1,2,3,4,5,6,7,8,9,10])
ll2 = create([2,3,4,5])
get_node(ll2,5).next=get_node(ll1,6)

assert intersection_node(ll1,ll2).data == 6