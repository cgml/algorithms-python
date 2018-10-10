# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if not root: return []
        q, result = [root], []
        while q:
            result.append(sum([n.val for n in q]) / float(len(q)))
            q = [x for y in [[n.left, n.right] for n in q] for x in y if x]
        return result

