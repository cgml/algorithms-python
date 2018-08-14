from cgml.leetcode.enumerated.utils import *

class Solution:
    def _helper(self, node, t, curmin, curmax):
        if node is None: return curmin if abs(t - curmin) < abs(t - curmax) else curmax
        if node.val == t: return node.val
        elif t < node.val : return self._helper(node.left, t, curmin, node.val)
        else: return self._helper(node.right, t, node.val, curmax)

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self._helper(root,target, float('-inf'), float('inf'))

assert Solution().closestValue(root = build_btree([4,2,5,1,3]), target = 3.714286) == 4
