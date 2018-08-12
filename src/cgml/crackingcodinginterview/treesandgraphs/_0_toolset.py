class TreeNode:
    v, l, r, parent = None, None, None, None
    def __init__(self, v): self.v = v

def bst_with_parent(l):
    if not l: return None
    mididx = 1 if len(l) == 2 else int(len(l)/2)
    root, root.l, root.r = TreeNode(l[mididx]), bst_with_parent(l[0:mididx]), bst_with_parent(l[mididx + 1:])
    if root.l: root.l.parent = root
    if root.r: root.r.parent = root
    return root


def printbtree(n,spaces=""):
    if n == None: return
    printbtree(n.l, spaces+".")
    print(spaces,n.v)
    printbtree(n.r, spaces+ ".")

def reversetree(t):
    if not t: return None
    tr,tr.r,tr.l = TreeNode(t.v), reversetree(t.l), reversetree(t.r)
    if tr.r: tr.r.parent = tr
    if tr.l: tr.l.parent = tr
    return tr