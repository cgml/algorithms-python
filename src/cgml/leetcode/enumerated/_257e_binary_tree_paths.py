# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        curpath = deque([])
        self.helper(root, curpath, result)
        return result

    def helper(self, root, curpath, result):
        if root is None: return
        curpath.append(str(root.val))
        if root.left is None and root.right is None:
            result.append('->'.join(list(curpath)))
        else:
            self.helper(root.left, curpath, result)
            self.helper(root.right, curpath, result)
        curpath.pop()