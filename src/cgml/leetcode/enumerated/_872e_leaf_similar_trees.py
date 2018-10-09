# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        ls1, ls2 = [], []
        self._leaf_sequence(root1, ls1)
        self._leaf_sequence(root2, ls2)
        return ls1 == ls2

    def _leaf_sequence(self, node, ls1):
        if not node: return
        if not node.left and not node.right: ls1.append(node.val)
        if node.left: self._leaf_sequence(node.left, ls1)
        if node.right: self._leaf_sequence(node.right, ls1)
