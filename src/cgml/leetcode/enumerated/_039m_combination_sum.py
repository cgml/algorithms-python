class Solution(object):
    def helper(self, candidates, target):
        r = []
        for i, c in enumerate(candidates):
            if c > target: break
            if c == target: r += [[target]]
            r += [[c] + z for z in self.helper(candidates[i:], target - c)]
        return r

    def combinationSum(self, candidates, target):
        return self.helper(sorted(candidates), target)


print(Solution().combinationSum([2,3,5], target = 8), "\n",[ [2,2,2,2], [2,3,3], [3,5] ])
