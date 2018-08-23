from cgml.leetcode.enumerated.utils import *

class Solution:
    def helper(self, left, right):
        if left is None and right is None: return True
        if left is None or right is None: return False
        return left.val == right.val and self.helper(left.right, right.left) and self.helper(left.left, right.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        return self.helper(root.left, root.right)


assert Solution().isSymmetric(build_btree([1,2,2,3,4,4,3]))