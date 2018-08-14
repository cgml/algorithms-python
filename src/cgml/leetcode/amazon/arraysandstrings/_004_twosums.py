class Solution:
    def twoSum(self, nums, target):
        pairs = {}
        for i, n in enumerate(nums):
            if pairs.get(n) is not None:
                return [pairs.get(n), i]
            pairs[target - n] = i
        return []
