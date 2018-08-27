# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        md, mp = self.helper(root)
        return mp

    def helper(self, root):
        if root is None: return 0, 0
        lmd, lmp = self.helper(root.left)
        rmd, rmp = self.helper(root.right)
        mp = max(lmp, rmp, lmd + rmd)
        cd = max(lmd, rmd) + 1
        return cd, mp