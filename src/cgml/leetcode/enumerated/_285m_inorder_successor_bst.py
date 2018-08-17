# Definition for a binary tree node.
from cgml.leetcode.enumerated.utils import *


class Solution(object):
    def helper(self, node, p, rightparent):
        if node is None: return None
        if node.val == p.val: return self.helper_successor(node.right) or rightparent
        return self.helper(node.left, p, node) or self.helper(node.right, p, rightparent)

    def helper_successor(self, node):
        if node is None: return None
        return self.helper_successor(node.left) or node

    def inorderSuccessor(self, root, p):
        return self.helper(root.left, p, root) or self.helper(root.right, p, None) or self.helper(root, p, None)

class SolutionLong(object):
    def helper(self, node, t, rightparent):
        if node is None: return None
        if node.val == t:
            if node.right:
                return self.helper_successor(node.right)
            else:
                return rightparent
        result = self.helper(node.left, t, node)
        if result: return result
        result = self.helper(node.right, t, rightparent)
        return result

    def helper_successor(self, node):
        print('helper successor ',node)
        if node is None: return None
        if node.left: return self.helper_successor(node.left)
        else: return node


    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None: return None
        t = p.val
        if root.val == t: return self.helper_successor(root.right)
        result = self.helper(root.left, t, root)
        if result:
            return result
        else:
            return self.helper(root.right, t, None)

print(Solution().inorderSuccessor(build_btree([2,1]),TreeNode(1)))
# print(Solution().inorderSuccessor(build_btree([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(2)))
