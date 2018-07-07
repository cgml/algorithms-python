from cgimaster.crackingcodinginterview.treesandgraphs._4_2_bst_from_sorted_array import *

def isbalanced(n):
    def isbal(n):
        if not n: return True, 0, 0
        b1, ma1, mi1 = isbal(n.l)
        if not b1: return False, 0, 0
        b2, ma2, mi2 = isbal(n.r)
        return b1 and b2 and abs(ma1 - mi2) <= 1 and abs(mi1 - ma2) <=1, max(ma1 + 1, ma2 + 1), min(mi1+1,mi2+1)
    return isbal(n)[0]

t = bst(sorted([1, 9, 10, 11, 2, 3, 33, 7, 18, 23, 24, 12]))

assert isbalanced(t)
t.l.l.l.r=TreeNode(1)
assert not isbalanced(t)