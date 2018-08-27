# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        if root.left is not None:
            left = root.left
            rightmost = self.getrm(left)
            right = root.right
            root.left = None
            root.right = left
            rightmost.right = right
        self.flatten(root.right)

    def getrm(self, root):
        if not root or not root.right: return root
        return self.getrm(root.right)