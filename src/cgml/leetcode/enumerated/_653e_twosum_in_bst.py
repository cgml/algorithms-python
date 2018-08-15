from cgml.leetcode.enumerated.utils import *
class Solution:
    def findTarget(self, root, t, sums=None):
        if root is None: return False
        if sums is None: sums = {}
        if root.val in sums: return True
        sums[t - root.val] = root.val
        return self.findTarget(root.left, t, sums) or self.findTarget(root.right, t, sums)

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