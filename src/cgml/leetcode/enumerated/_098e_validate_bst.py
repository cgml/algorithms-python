from .utils import *

class Solution(object):
    def isValidBST(self, node, leftLimit=None, rightLimit=None):
        if node == None: return True
        if leftLimit is not None and node.val <= leftLimit: return False
        if rightLimit is not None and node.val >= rightLimit: return False
        return self.isValidBST(node.left,leftLimit,node.val) and self.isValidBST(node.right,node.val,rightLimit)


print(Solution().isValidBST(build_btree([5, 1, 4, None, None, 3, 6])))
print(Solution().isValidBST(build_btree([1, 1])))