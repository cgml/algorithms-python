# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        qp, pp, queue, en = [], [], [[root]], None
        while queue and (not qp or not pp):
            n = queue.pop(0)
            if n[-1].val == p.val: pp = list(n)
            if n[-1].val == q.val: qp = list(n)
            if n[-1].left: queue.append(n+[n[-1].left])
            if n[-1].right: queue.append(n+[n[-1].right])
        for pn, qn in zip(qp, pp):
            if pn.val != qn.val: break
            en = pn
        return en

class SolutionTX:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root in (None, p, q): return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: return root
        if left: return left
        else: return right