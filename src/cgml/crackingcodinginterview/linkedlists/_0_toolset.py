'''
Insert to head
Insert at K
Append to tail
Remove K
Remove head
Remove tail
Reverse
Get center
'''
class LLNode:
    data = None
    next = None
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "Node: <{}>".format(self.data)


def create(l):
    if len(l)==0: return None
    head = LLNode(l[0])
    curr = head
    for idx in range(1,len(l)):
        curr.next = LLNode(l[idx])
        curr = curr.next
    return head

def print_ll(ll):
    curr = ll
    while curr is not None:
        print(curr.data, end=''); curr = curr.next
    print()

def reverse(ll):
    prev, curr = None, ll
    while curr is not None: curr.next, prev, curr = prev, curr, curr.next
    return prev

def insert_head(ll,n):
    n.next = ll
    return n

def insert_at(ll,n,k):
    prev, curr, idx = None, ll, 0
    while curr is not None and idx<=k: prev, curr = curr, curr.next
    prev.next, n.next = n, prev.next
    return ll

def insert_tail(ll,n):
    prev, curr = None, ll
    while curr is not None: prev, curr = curr, curr.next
    prev.next = n
    return ll

def get_center(ll):
    if ll is None: return None,0,None,0
    prev,curr,mid,prevR,currR,total=None,ll,0,None,ll,0
    while currR is not None:
        prev,curr,mid,prevR,currR,total=curr,curr.next,mid+1,currR,currR.next,total+1
        if currR is not None: prevR,currR,total=currR,currR.next,total+1
    return {"mid":{"node":prev,"count":mid},"tail":{"node":prevR,"count":total}}

def remove_head(ll):
    if ll is None: return None
    return ll.next

def remove_at(ll,k):
    if ll is None: return None
    if k == 0: return remove_head(ll)
    prev, curr, idx = None, ll, 0
    while curr is not None and idx < k: prev, curr, idx = curr, curr.next, idx+1
    if curr is not None: prev.next = curr.next
    return ll

def remove_tail(ll):
    if ll is None or ll.next is None: return None
    prev, curr, next = None, ll, ll.next
    while next is not None: prev, curr, next = curr, next, next.next
    prev.next = None
    return ll

def to_list(ll):
    result, curr = [],ll
    while curr is not None: result, curr = result+[curr.data], curr.next
    return result

def get_tail(ll):
    p,c = None,ll
    while c is not None: p,c = c, c.next
    return p

def get_node(ll,data):
    if ll is None: return None
    c = ll
    while c is not None and c.data != data: c = c.next
    return c

assert to_list(create([1,2,3,4,5])) == [1,2,3,4,5]
assert to_list(reverse(create([1,2,3,4,5])))==[5,4,3,2,1]

assert get_center(create([1,2,3,4,5,6,7,8,9,10]))['mid']['node'].data == 5
assert get_center(create([1,2,3,4,5,6,7,8,9,10,11]))['mid']['node'].data == 6
assert get_center(create([1]))['mid']['node'].data == 1

assert to_list(remove_head(create([1,2,3,4,5,6,7,8,9,10,11]))) == [2,3,4,5,6,7,8,9,10,11]
assert to_list(remove_tail(create([1,2,3,4,5,6,7,8,9,10,11]))) == [1,2,3,4,5,6,7,8,9,10]
assert to_list(remove_at(create([1,2,3,4,5,6,7,8,9,10,11]),0)) == [2,3,4,5,6,7,8,9,10,11]
assert to_list(remove_at(create([1,2,3,4,5,6,7,8,9,10,11]),5)) == [1,2,3,4,5,7,8,9,10,11]
assert to_list(remove_at(create([1,2,3,4,5,6,7,8,9,10,11]),10)) == [1,2,3,4,5,6,7,8,9,10]