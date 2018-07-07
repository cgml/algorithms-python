from cgimaster.crackingcodinginterview.treesandgraphs._4_2_bst_from_sorted_array import *

def validate_bst(n,l=None, r=None):
    if not n: return True
    if l is not None and n.v <=l or r is not None and n.v >= r: return False
    return validate_bst(n.l,l,n.v) and validate_bst(n.r,n.v,r)

t = bst(sorted([1, 10, 11, 2, 3, 33, 7, 18, 23, 24, 12]))
assert validate_bst(t)
t.l.v=8
assert not validate_bst(t)
