# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        nroot, _ = self._helper(root, None, None)
        return nroot

    def _helper(self, node, nroot, ncur):
        if not node: return nroot, ncur
        nroot, ncur = self._helper(node.left, nroot, ncur)
        if nroot is None:
            ncur = nroot = TreeNode(node.val)
        else:
            ncur.right = TreeNode(node.val)
            ncur = ncur.right
        return self._helper(node.right, nroot, ncur)