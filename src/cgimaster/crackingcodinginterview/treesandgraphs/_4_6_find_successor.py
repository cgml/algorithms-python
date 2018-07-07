from cgimaster.crackingcodinginterview.treesandgraphs._0_toolset import *

def successor(t, target):
    n = findnode(t,target)
    if not n: return None
    if not n.r: return n.parent if n.parent and n.parent.v >= n.v else None
    def minnode(n): return minnode(n.l) if n.l else n
    return minnode(n.r)

def findnode(t,target):
    if not t: return None
    if t.v == target: return t
    elif t.v > target: return findnode(t.l, target)
    else: return findnode(t.r, target)

t = bst_with_parent(sorted([1, 10, 11, 2, 3, 33, 7, 18, 23, 24, 12]))
printbtree(t)
assert successor(t,11).v == 12
assert successor(t,1).v == 2
assert successor(t,2).v == 3
assert not successor(t,33)