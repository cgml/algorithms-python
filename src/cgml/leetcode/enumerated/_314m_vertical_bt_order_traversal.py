# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from cgml.leetcode.enumerated.utils import *
import collections

class Solution:
    def verticalOrder(self, root):
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]



class SolutionDFS:
    def helper(self, t, mem, G, curidx):
        if t is None: return
        nodeidx = G['rootidx']+curidx
        print(G['rootidx'],nodeidx,curidx)
        if nodeidx < 0:
            G['rootidx'] = G['rootidx']+1
            mem.insert(0, [t.val])
        elif nodeidx >= len(mem): mem.append([t.val])
        else: mem[nodeidx].append(t.val)
        self.helper(t.left, mem, G, curidx-1)
        self.helper(t.right, mem, G, curidx+1)

    def verticalOrder(self, root):
        G, mem = {'rootidx':0}, []
        self.helper(root, mem, G, 0)
        return mem


print(Solution().verticalOrder(build_btree([3,9,20,None,None,15,7])))
assert SolutionDFS().verticalOrder(build_btree([3,9,20,None,None,15,7])) == [ [9], [3,15], [20], [7] ]