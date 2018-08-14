class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "<{}:{},{}>".format(self.val, "+" if self.left is not None else "-",
                                   "+" if self.right is not None else "-")

    def __repr__(self):
        return "<{}:{},{}>".format(self.val, "+" if self.left is not None else "-", "+" if self.right is not None else "-")

def build_btree(l):
    curlevel, curidx, curlevelstart = 1, 0, 0
    root,l = TreeNode(l[0]), l[1:]
    prevlevel = [root]
    while l:
        levelnodes,l, curlevel = l[:min(2*len(prevlevel),len(l))], l[min(2*len(prevlevel),len(l)):], curlevel+1
        newlevel = []
        while prevlevel and levelnodes:
            curroot = prevlevel.pop(0)
            if not curroot: continue
            if levelnodes and curroot:
                val = levelnodes.pop(0)
                if val:
                    curroot.left = TreeNode(val)
                    newlevel += [curroot.left]
            if levelnodes and curroot:
                val = levelnodes.pop(0)
                if val:
                    curroot.right = TreeNode(val)
                    newlevel += [curroot.right]
        prevlevel = newlevel
    return root