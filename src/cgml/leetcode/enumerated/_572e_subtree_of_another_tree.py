from cgml.leetcode.enumerated.utils import *
class Solution:
    def isEqual(self, s, t):
        if s is None and t is None: return True
        if s is None or t is None: return False
        print('compare: {}, {}'.format(s,t))
        result = s.val == t.val
        result = result and self.isEqual(s.right, t.right)
        result = result and self.isEqual(s.left, t.left)
        return result

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is None: return True
        if s is None or t is None: return False
        return self.isEqual(s,t) or self.isSubtree(s.right,t) or self.isSubtree(s.left,t)
s = build_btree([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2])
t = build_btree([1,None,1,None,1,None,1,None,1,None,1,2])
assert Solution().isSubtree(s,t)

