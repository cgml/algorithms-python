from cgml.leetcode.enumerated.utils import *
class Solution:
    def twosums(self, root, sums, t):
        if root is None: return False
        if sums.get(root.val) is not None: return True
        sums[t - root.val] = root.val
        return self.twosums(root.left, sums, t) or self.twosums(root.right, sums, t)

    def findTarget(self, root, t):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        sums = {}
        return self.twosums(root, sums, t)

    def findTargetBFS(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False


assert Solution().findTarget(build_btree([5,3,6,2,4,None,7]),9)