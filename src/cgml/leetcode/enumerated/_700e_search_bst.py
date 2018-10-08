class Solution(object):
    def searchBST(self, root, val):
        if not root: return None
        if root.val == val: return root
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)