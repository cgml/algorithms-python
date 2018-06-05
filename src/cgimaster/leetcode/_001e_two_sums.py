class Solution:
    def twoSum(self, nums, target):
        pairs = {}
        for i, n in enumerate(nums):
            if pairs.get(n) is not None:
                return [pairs.get(n), i]
            pairs[target - n] = i
        return []

assert Solution().twoSum([2,7,11,15], 9) == [0,1]