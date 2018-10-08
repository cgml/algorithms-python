"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self._helper(root, result)
        return result

    def _helper(self, node, result):
        if not node: return
        for n in node.children: self._helper(n, result)
        result.append(node.val)

