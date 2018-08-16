# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from cgml.leetcode.enumerated.utils import *

class Solution:
    def helper(self, t, mem, depth):
        if t is None: return
        while len(mem) <= depth: mem.append([])
        mem[depth].append(t.val)
        self.helper(t.left, mem, depth+1)
        self.helper(t.right, mem, depth+1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mem = []
        self.helper(root, mem, 0)
        return mem

assert Solution().levelOrder(build_btree([3,9,20,None,None,15,7])) == [
  [3],
  [9,20],
  [15,7]
]
