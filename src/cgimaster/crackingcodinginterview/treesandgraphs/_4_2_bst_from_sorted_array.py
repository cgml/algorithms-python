from cgimaster.crackingcodinginterview.treesandgraphs._0_toolset import *

def bst(l):
    if not l: return None
    mididx = 1 if len(l) == 2 else int(len(l)/2)
    root, root.l, root.r = TreeNode(l[mididx]), bst(l[0:mididx]), bst(l[mididx + 1:])
    return root

bst(sorted([1, 10, 11, 2, 3, 33, 7, 23, 24, 12]))
#printbtree()
