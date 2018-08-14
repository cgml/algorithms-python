from cgml.leetcode.enumerated.utils import *

class Solution:
    def sumNumbers(self, root):
        paths, curpath = [], []
        self.dfs(root, paths, curpath)
        result = self.sumup(paths)
        return result

    def sumup(self, paths):
        idx, carry, result = 0, 0, 0
        while paths or carry > 0:
            curval = carry
            for i in range(len(paths))[::-1]:
                curval += paths[i].pop(0).val
                if not paths[i]: paths.pop(i)
            curval, carry = curval % 10, int(curval / 10)
            result += curval * 10 ** idx
            idx += 1
        return result

    def dfs(self, node, paths, curpath):
        if node is None: return
        curpath = curpath+[node]
        if node.right is None and node.left is None: paths.append(curpath[::-1])
        self.dfs(node.left, paths, curpath)
        self.dfs(node.right, paths, curpath)


assert Solution().sumNumbers(build_btree([1,2,3])) == 25